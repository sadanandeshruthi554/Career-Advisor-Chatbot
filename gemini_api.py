from google import genai
import os
import time
from dotenv import load_dotenv

load_dotenv()

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
            error_message = str(e)

            if "503" in error_message:
                time.sleep(5)
                continue

            return f"Error: {error_message}"

    return "⚠️ Gemini is currently busy. Please try again after a few minutes."
