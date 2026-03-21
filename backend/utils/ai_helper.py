import requests
import json
import os
from backend.config import Config

def call_groq_ai(prompt, model="llama-3.3-70b-versatile"):
    api_key = Config.GROQ_API_KEY
    if not api_key:
        print("⚠️ Error: GROQ_API_KEY not found in configuration.")
        return None
        
    try:
        response = requests.post(
            Config.GROQ_API_URL, 
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": model, 
                "messages": [{"role": "user", "content": prompt}], 
                "temperature": 0.3, 
                "response_format": {"type": "json_object"}
            }, 
            timeout=10
        )
        if response.status_code == 200: 
            return json.loads(response.json()['choices'][0]['message']['content'])
        print(f"❌ Groq API Error: {response.status_code} - {response.text}")
        return None
    except Exception as e:
        print(f"❌ Groq AI Error: {e}")
        return None
