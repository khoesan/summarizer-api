from fastapi import FastAPI, Request
from transformers import pipeline
import os

app = FastAPI()
summarizer = None

@app.on_event("startup")
def load_model():
    global summarizer
    summarizer = pipeline("summarization", model="khoesan/summarizer-tf5")

@app.post("/summarize")
async def summarize(request: Request):
    global summarizer
    if summarizer is None:
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    
    data = await request.json()
    result = summarizer(data["text"])
    return {"summary": result[0]["summary_text"]}
