import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generate_completion(prompt, model="gpt-4.1-nano", temperature=0.3):
    url = "https://api.euron.one/api/v1/euri/chat/completions"
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OPENAI_API_KEY is not set in environment variables.")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],  # ✅ fixed spelling
        "temperature": temperature,  # ✅ fixed spelling
        "max_tokens": 500
    }

    res = requests.post(url, headers=headers, json=data)
    res_json = res.json()

    # ✅ Debug log in case of error
    if 'choices' not in res_json:
        raise RuntimeError(f"API Error: {res_json}")

    return res_json['choices'][0]['message']['content']
