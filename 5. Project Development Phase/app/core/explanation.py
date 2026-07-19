from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the improved model for explanations
explain_tokenizer = AutoTokenizer.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
explain_model = AutoModelForSeq2SeqLM.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")

def explain_topic(topic: str) -> str:
    """
    Generate a concise, beginner-friendly explanation for a given topic
    using manual tokenization and sequence generation.
    """
    input_text = f"Provide a detailed, thorough, step-by-step, and very long explanation of the concept '{topic}' for a student. Write multiple paragraphs. Ensure the response is detailed and comprehensive."
    try:
        inputs = explain_tokenizer(input_text, return_tensors="pt")

        outputs = explain_model.generate(
            **inputs,
            min_new_tokens=220,
            max_new_tokens=400,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.2,
            do_sample=True
        )

        explanation = explain_tokenizer.decode(outputs[0], skip_special_tokens=True)
        return explanation
    except Exception as e:
        return f"[Explanation Module Error] Failed to explain '{topic}': {str(e)}"
