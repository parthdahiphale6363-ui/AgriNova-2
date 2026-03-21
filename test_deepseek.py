import requests
import json

# Your DeepSeek API key
DEEPSEEK_API_KEY = "sk-514ec***********************3f52"  # Replace with your actual full key
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

def test_deepseek():
    print("🔍 Testing DeepSeek API connection...")
    
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say 'Hello from DeepSeek' if you can hear me"}
        ],
        "temperature": 0.3,
        "max_tokens": 100
    }
    
    try:
        print("📡 Sending request to DeepSeek...")
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=10)
        
        print(f"📊 Response Status: {response.status_code}")
        print(f"📝 Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ SUCCESS! DeepSeek API is working!")
            print(f"🤖 Response: {result['choices'][0]['message']['content']}")
            return True
        else:
            print(f"❌ ERROR: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_deepseek()