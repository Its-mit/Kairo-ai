# ai_brain

from groq import Groq
import os
from dotenv import load_dotenv

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
                {"role": "system", "content": "You are Kairo AI. Give short, helpful answers."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("ERROR:", e)
        return "AI not available"