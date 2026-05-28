# ai_brain

from groq import Groq
import os
from dotenv import load_dotenv
from brain.personality import (
    get_name,
    get_greeting,
    get_wake_word
)
system_prompt = f"""
You are KAIRO AI.

User name is {get_name()}.

Call the user {get_greeting()} sometimes naturally.

Wake word is {get_wake_word()}.

Be friendly, smart, emotional, and concise.
"""

# Load .env file
load_dotenv()

# Get API key securely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found. Check your .env file")

# Initialize client
client = Groq(api_key=GROQ_API_KEY)


def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("ERROR:", e)
        return "AI not available"