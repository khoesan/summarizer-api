from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/khoesan/summarizer-t5"
HF_TOKEN = "hf_YourAccessTokenHere"  # Buat di huggingface.co/settings/tokens

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

class InputText(BaseModel):
    text: str

@app.post("/summarize")
def summarize(input: InputText):
    payload = {"inputs": input.text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
