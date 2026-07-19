import os
import re
import json
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

def clean_json_block(text: str) -> str:
    """
    Remove Markdown ```json code fences using DOTALL regex substitution.
    """
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()

def generate_quiz(text: str) -> list:
    """
    Generate 3 MCQs from a passage using Gemini and return a list of JSON objects.
    """
    try:
        model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")
        
        prompt = f"""
You are an advanced educational quiz generator.

Here is the input text/topic:
"{text}"

If the input is a short keyword, phrase, or topic name (e.g., "ML", "Artificial Intelligence", "Solar System"), use your broad general knowledge to generate 3 deep, conceptual, and challenging multiple-choice questions about that subject.
If the input is a longer passage, base the questions on the content of the passage.

CRITICAL CONSTRAINTS:
1. Do NOT generate silly meta-questions about the input string itself (e.g., do NOT ask about character counts, spelling, capitalization, first/last letters, or exact string matches of the keyword).
2. The questions must test for deep comprehension, reasoning, and conceptual understanding of the underlying educational subject matter (e.g., if the topic is "ML", ask about supervised learning, algorithms, neural networks, or datasets).
3. Each question must include:
   - A "question" probing deep aspects of the subject.
   - A list of 4 plausible "options".
   - A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON** inside a list:
[
  {{
    "question": "Deep conceptual question here...",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "Correct Option text"
  }}
]
"""
        response = model.generate_content(prompt)
        quiz_text = response.text.strip()
        
        # Clean markdown code blocks if any
        cleaned_text = clean_json_block(quiz_text)
        
        # Parse text to JSON list of questions
        quiz_data = json.loads(cleaned_text)
        return quiz_data
        
    except Exception as e:
        print(f"Error generating quiz: {e}")
        return []
