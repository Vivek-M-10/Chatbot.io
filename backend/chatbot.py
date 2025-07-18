import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        if not response.text:
            return "⚠️ No response from Gemini."
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    print("💬 Gemini Chat (type 'exit' or 'quit' to stop)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("👋 Goodbye!")
            break
        print("Gemini:", ask_gemini(user_input))
