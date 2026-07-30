from transformers import pipeline

# Load pre-trained NLP pipeline
nlp_pipeline = pipeline("sentiment-analysis")

def analyze_resume_text(text: str):
    result = nlp_pipeline(text)
    word_count = len(text.split())
    skills_found = [word for word in ["python", "machine learning", "sql", "api"] if word in text.lower()]
    score = min(100, len(skills_found) * 20 + (10 if word_count > 50 else 5))
    
    return {
        "skills": skills_found,
        "score": f"{score}%",
        "sentiment": result[0]["label"],
        "recommendation": "Strong profile for tech role!" if score >= 40 else "Needs more skills mentioned."
    }
  
