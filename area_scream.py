import modules.zipcode_api
import modules.openai_api

zipcode = modules.zipcode_api

zcode = input('郵便番号を入力してください: ')
address = zipcode.get(zcode).json()

prompt = f"""
{address}のエリアに応じて出力を変えてください。
ただし、出力は必ず1文字の数字であること。
エリア: 出力する値 の対応表は以下です。
関東: 1,
関西: 2,
その他: 3
"""

gpt = modules.openai_api
gpt_responce = gpt.post(prompt, temperature=0.0)
area = gpt.content(gpt_responce)

if area == '1':
    print('関東〜〜〜〜〜！！！')
elif area == '2':
    print('関西〜〜〜〜〜！！！')
elif area == '3':
    print('その他〜〜〜〜〜！！！')
else:
    print('エラーが発生しました。')
