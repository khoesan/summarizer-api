from fastapi import FastAPI, Request
from transformers import pipeline
import os

app = FastAPI()

summarizer = pipeline("summarization", model="khoesan/summarizer-t5")  # atau distilbart kalau crash

@app.get("/")
def root():
    return {"message": "Summarizer API is running"}

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    summary = summarizer(data["text"])
    return {"summary": summary[0]["summary_text"]}
