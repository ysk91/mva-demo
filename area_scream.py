import config
from zipcode_api import ZipcodeApi
from openai_api import OpenAi

OPENAI_API_KEY = config.OPENAI_API_KEY
GPT_MODEL = config.GPT_MODEL

zipcode_api = ZipcodeApi()
address = zipcode_api.get().json()

prompt = f"""
{address}のエリアに応じて出力を変えてください。
ただし、出力は必ず1文字の数字であること。
エリア: 出力する値 の対応表は以下です。
関東: 1,
関西: 2,
その他: 3
"""

gpt = OpenAi(OPENAI_API_KEY)
gpt_responce = gpt.post(GPT_MODEL, prompt, 0.0)
area = gpt.content(gpt_responce)

if area == '1':
    print('関東〜〜〜〜〜！！！')
elif area == '2':
    print('関西〜〜〜〜〜！！！')
elif area == '3':
    print('その他〜〜〜〜〜！！！')
else:
    print('エラーが発生しました。')
