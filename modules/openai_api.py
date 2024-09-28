import requests

# https://platform.openai.com/docs/overview

class OpenAi:
    def __init__(self, api_key):
        self.api_key = api_key

    def post(self, model, prompt, temperature=0.7):
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.api_key}',
            },
            json={
                'model': model,
                'messages': [
                    {'role': 'user', 'content': prompt}
                ],
                "temperature": temperature,
            }
        )
        return response.json()

    def content(self, response):
        return response['choices'][0]['message']['content']
