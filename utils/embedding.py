import os
from dotenv import load_dotenv
import requests
import numpy as np

# Load environment variables from .env file
load_dotenv()

def generate_embeddings(text, model="text-embedding-3-small"):
    url ="https://api.euron.one/api/v1/euri/embeddings"
    
    #api_key = os.getenv("OPENAI_API_KEY")
    api_key =os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OPENAI_API_KEY not found in environment variables.")
    #print(os.getenv("OPENAI_API_KEY"))
        
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {"input": text, "model": model}

    try:
        response = requests.post(url, headers=headers, json=payload)
    except requests.exceptions.Timeout:
        print("Request timed out!")
        return None
    except Exception as e:
        print("Request failed:", str(e))
        return None

    if response.status_code != 200:
        print("Error:", response.text)
        return None
    return np.array(response.json()['data'][0]['embedding'])
