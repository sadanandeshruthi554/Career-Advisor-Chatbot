from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Create client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",  # ✅ latest working model
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"