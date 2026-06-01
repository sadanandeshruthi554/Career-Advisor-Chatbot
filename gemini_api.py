from google import genai
import os
import time

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def get_response(prompt):
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt
            )
            return response.text

        except Exception as e:
            if "503" in str(e):
                time.sleep(5)
                continue

            return f"Error: {str(e)}"

    return "⚠️ Gemini is currently busy. Please try again later."
