import requests

OLLAMA_BASE_URL = "http://localhost:11434/api/generate"

def query_model(model_name, prompt):
    try:
        response = requests.post(OLLAMA_BASE_URL, json={
            "model": model_name,
            "prompt": prompt,
            "stream": False
        })
        if response.status_code == 200:
            return response.json().get("response", "❌ No response")
        else:
            return f"❌ Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Exception: {str(e)}"
