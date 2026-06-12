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
    1. Play music/video -> intent is "PLAY_SONG", target is the song/video name.
    2. Open an app/website -> intent is "OPEN", target is the app/website name.
    3. Close/exit an app -> intent is "CLOSE", target is the app name (or "current" if unspecified).
    4. Maximize/enlarge window -> intent is "MAXIMIZE", target is the app name (or "current" if unspecified).
    5. Minimize/hide window -> intent is "MINIMIZE", target is the app name (or "current" if unspecified).
    6. Write/draft document/email -> intent is "WRITE_CONTENT", target is the app name, topic is the subject to write about.
    7. For basic info, time, date, searching, or chatting -> intent is "AI", target is the full command.
    
    Format required:
    {{
        "intent": "PLAY_SONG" | "OPEN" | "CLOSE" | "MAXIMIZE" | "MINIMIZE" | "WRITE_CONTENT" | "AI",
        "target": "clean target name or 'current'",
        "browser": "brave" | "chrome" | "default",
        "topic": "topic if WRITE_CONTENT, else empty"
    }}
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0 # Zero temperature for strict formatting
        )
        
        raw_text = response.choices[0].message.content.strip()
        
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:-3]
        elif raw_text.startswith("```"):
            raw_text = raw_text[3:-3]
            
        return json.loads(raw_text.strip())
        
    except Exception as e:
        print("Intent Parsing Error:", e)
        return {"intent": "AI", "target": command, "browser": "default", "topic": ""}