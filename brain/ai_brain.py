import requests

def ask_ai(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": f"You are Kairo AI, a smart assistant. Give short helpful answers.\nUser: {prompt}",
                "stream": False
            }
        )

        return response.json()['response']

    except Exception as e:
        print("ERROR:", e)
        return "AI not available"