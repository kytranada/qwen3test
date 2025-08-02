import requests
import ollama
import time
import psutil
import os

OLLAMA_BASE_URL = "http://localhost:11434/api/generate"

def query_model(model_name, prompt):
    """Query the Ollama model and return response with additional metrics"""
    start_time = time.time()
    
    process = psutil.Process(os.getpid())
    initial_cpu_percent = process.cpu_percent()
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    
 
    first_token_time = None

    response_text = ""
    
    try:
        stream = ollama.generate(model=model_name, prompt=prompt, stream=True)
        
        for chunk in stream:
            if first_token_time is None:
                first_token_time = time.time() - start_time
            response_text += chunk.get('response', '')
            
    except Exception as e:
        return {
            "response": f"Error: {str(e)}", 
            "token_count": 0, 
            "first_token_time": 0,
            "cpu_percent": 0,
            "memory_mb": 0
        }
    
    final_cpu_percent = process.cpu_percent()
    final_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    token_count = len(response_text.split())
    
    return {
        "response": response_text,
        "token_count": token_count,
        "response_length": len(response_text),
        "first_token_time": first_token_time or (time.time() - start_time),
        "cpu_percent": final_cpu_percent - initial_cpu_percent,
        "memory_mb": final_memory - initial_memory
    }
