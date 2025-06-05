# OpenRouter is a fast and secure open-source router for AI models and endpoints.


# 02_openrouter/openrouter_example.py
import requests

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": "Bearer <YOUR_API_KEY>",
    "Content-Type": "application/json"
}
data = {
    "model": "mistralai/mixtral-8x7b",
    "messages": [
        {"role": "user", "content": "Hello, OpenRouter!"}
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
