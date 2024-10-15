import requests
import json
from modules import config

# https://platform.openai.com/docs/overview

OPENAI_API_KEY = config.OPENAI_API_KEY
GPT_MODEL = config.GPT_MODEL


def post(prompt, model=GPT_MODEL, temperature=0.7, json=False):
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
    }

    if json:
        data["response_format"] = {"type": "json_object"}

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        },
        json=data,
    )
    return response.json()


def content(response, as_json=False):
    content = response["choices"][0]["message"]["content"]
    if content is None:
        return None
    return json.loads(content) if as_json else content


# Hack
# OpenAI APIをJSONモードで使用する場合、プロンプト内でJSONで出力するように指示する必要がある。
# {'error': {'message': "'messages' must contain the word 'json' in some form,
#  to use 'response_format' of type 'json_object'.",
#  'type': 'invalid_request_error', 'param': 'messages', 'code': None}}
# その際、出力形式でキーと値を指定する。
# contentから任意の値を使用するには、取得したJSON形式の値に対してキーで抜き出す。
# JSON内の値は文字列であることに注意する。
