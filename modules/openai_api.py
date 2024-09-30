import requests
import json
from modules import config

# https://platform.openai.com/docs/overview

OPENAI_API_KEY = config.OPENAI_API_KEY
GPT_MODEL = config.GPT_MODEL

def post(prompt, temperature=0.7):
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {OPENAI_API_KEY}',
        },
        json={
            'model': GPT_MODEL,
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
            "temperature": temperature,
            "response_format": {"type": "json_object"}
        }
    )
    return response.json()

def content(response):
    content = response['choices'][0]['message']['content']
    return json.loads(content) if content else None
