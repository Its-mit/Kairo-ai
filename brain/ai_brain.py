from openai import OpenAI

client = OpenAI(api_key="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")

def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Kairo AI, a helpful personal assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return "Error connecting to AI"