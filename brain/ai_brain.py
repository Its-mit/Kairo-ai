# ai_brain.py
from groq import Groq
import os
import json
from dotenv import load_dotenv
from brain.personality import (
    get_name,
    get_greeting,
    get_wake_word
)

# Load .env file
load_dotenv()

# Get API key securely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found. Check your .env file")

# Initialize client
client = Groq(api_key=GROQ_API_KEY)

# Simple memory to store the conversation context
conversation_history = []

def ask_ai(prompt):
    global conversation_history
    
    system_prompt = f"""
    You are KAIRO AI.
    User name is {get_name()}.
    Call the user {get_greeting()} sometimes naturally.
    Wake word is {get_wake_word()}.
    Be friendly, smart, emotional, and concise.
    """

    # Start with the system prompt
    messages = [{"role": "system", "content": system_prompt}]
    
    # Append past conversation (limit to last 6 messages to save tokens/speed)
    messages.extend(conversation_history[-6:])
    
    # Append the new user prompt
    messages.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        ai_response = response.choices[0].message.content.strip()
        
        # Save this interaction to history so Kairo remembers it for next time
        conversation_history.append({"role": "user", "content": prompt})
        conversation_history.append({"role": "assistant", "content": ai_response})

        return ai_response

    except Exception as e:
        print("ERROR:", e)
        return "AI not available"

def get_smart_intent(command):
    prompt = f"""
    Analyze this voice command: "{command}"
    Return ONLY a raw JSON object. Do not use Markdown formatting or text.
    
    Rules:
    1. If the user wants to play music or a video, intent is "PLAY_SONG", target is the song/video name.
    2. If the user wants to open an app or website (without playing a specific song), intent is "OPEN", target is the app/website name.
    3. If the user wants to write an essay, report, notepad note, or draft an email, intent is "WRITE_CONTENT", target is the application ('notepad', 'word', 'mail'), and topic is what to write about.
    4. Identify the browser if specifically mentioned (brave, chrome). Otherwise output "default".
    5. If it's a general question, greeting, or conversation, intent is "AI", target is the full command.

    Format required:
    {{
        "intent": "PLAY_SONG" | "OPEN" | "WRITE_CONTENT" | "AI",
        "target": "song name / app name / full command",
        "browser": "brave" | "chrome" | "default",
        "topic": "only used if WRITE_CONTENT to describe the essay/mail subject"
    }}
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0 # Zero temperature for strict formatting
        )
        
        raw_text = response.choices[0].message.content.strip()
        
        # Clean up in case the LLM adds markdown backticks (```json)
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:-3]
        elif raw_text.startswith("```"):
            raw_text = raw_text[3:-3]
            
        return json.loads(raw_text.strip())
        
    except Exception as e:
        print("Intent Parsing Error:", e)
        # Fallback to general conversation if the parser fails
        return {"intent": "AI", "target": command, "browser": "default"}