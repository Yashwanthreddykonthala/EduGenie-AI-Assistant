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

# Global model instance
model = genai.GenerativeModel("models/gemini-2.5-flash")

def get_learning_recommendations(topic: str) -> str:
    """
    Generate a structured, progressive learning roadmap for a given topic.
    """
    prompt = f"""
You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics, order of learning, and resources (books, websites, videos).
Include beginner, intermediate, and advanced levels if needed.
"""
    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text
        elif hasattr(response, "parts") and response.parts:
            return response.parts[0].text
        else:
            return "❌ Could not extract content from Gemini response."
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"❌ Error occurred: {str(e)}"
