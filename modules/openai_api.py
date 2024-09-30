import requests
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
        }
    )
    return response.json()

def content(response):
    return response['choices'][0]['message']['content']
