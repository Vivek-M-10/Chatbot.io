import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        if not response.text:
            return "⚠️ No response from Gemini."
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {e}"
