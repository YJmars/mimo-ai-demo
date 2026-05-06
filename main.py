# MiMo API Demo (for GitHub proof)
import os
import requests
from dotenv import load_dotenv

def call_mimo_api(prompt: str) -> dict:
    load_dotenv()
    api_key=os.getenv("MIMO_API_KEY")
    if not api_key:
        return {"error": "MIMO_API_KEY not set"}

    url = "https://api.xiaomimimo.com/v1/chat"
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data={
        "model": "mimo-v2-pro",
        "prompt": prompt,
        "temperature": 0.7
    }
    try:
        res=requests.post(url, json=data, headers=headers, timeout=30)
        return res.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print("=== MiMo API Demo ===")
    result=call_mimo_api("Hello, MiMo!")
    print(result)
