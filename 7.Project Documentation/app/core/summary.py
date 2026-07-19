import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment configuration
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise EnvironmentError(
        "Missing GEMINI_API_KEY. Please set it in your .env file."
    )

# Configure the API key globally
genai.configure(api_key=GEMINI_API_KEY)

def summarize_text(text: str) -> str:
    """
    Condense a long passage of text into a concise version.
    """
    try:
        model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")
        prompt = f"Summarize the following text in simple language:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in Summary: {e}"
