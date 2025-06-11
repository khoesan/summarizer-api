from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
summarizer = pipeline("summarization", model="khoesan/summarizer-t5")

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(data: TextInput):
    summary = summarizer(data.text, max_length=150, min_length=40, do_sample=False)
    return {"summary": summary[0]['summary_text']}
