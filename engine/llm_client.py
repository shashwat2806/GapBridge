
import requests
from config import OLLAMA_URL, MODEL_NAME

def query_mistral(prompt):
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    r.raise_for_status()
    return r.json()["response"].strip()