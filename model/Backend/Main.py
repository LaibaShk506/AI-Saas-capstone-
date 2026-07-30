from fastapi import FastAPI
from pydantic import BaseModel
from model.analyzer import analyze_resume_text

app = FastAPI(title="AI Resume & Content Analyzer API")

class TextPayload(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "API is running!"}

@app.post("/analyze")
def analyze(data: TextPayload):
    analysis_result = analyze_resume_text(data.text)
    return {"status": "success", "data": analysis_result}
  
