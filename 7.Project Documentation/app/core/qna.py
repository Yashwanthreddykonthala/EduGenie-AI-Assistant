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

def answer_question_with_gemini(question: str) -> str:
    """
    Send a question to Gemini and return its answer as plain text.
    """
    try:
        model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")
        prompt = f"Answer the following question in a concise, direct, and short manner (keep it brief and under 2-3 sentences if possible):\n\n{question}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"
