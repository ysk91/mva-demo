import config
from zipcode_api import ZipcodeApi
from openai_api import OpenAi

OPENAI_API_KEY = config.OPENAI_API_KEY
GPT_MODEL = config.GPT_MODEL

zipcode_api = ZipcodeApi()
address = zipcode_api.get().json()

prompt = f"{address}の特産品を教えてください。"
gpt_responce = OpenAi(OPENAI_API_KEY).post(GPT_MODEL, prompt)
content = gpt_responce['choices'][0]['message']['content']

print(content)
