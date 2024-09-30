import os
import modules.zipcode_api
import modules.openai_api
import modules.github_api
import modules.rescue_issue

zipcode = modules.zipcode_api
gpt = modules.openai_api
github = modules.github_api
rescue_issue = modules.rescue_issue

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

gpt_responce = gpt.post(prompt, temperature=0.0)
area = gpt.content(gpt_responce)

try:
    if area == '1':
        print('関東〜〜〜〜〜！！！')
    elif area == '2':
        print('関西〜〜〜〜〜！！！')
    elif area == '3':
        print('その他〜〜〜〜〜！！！')
except Exception as e:
    script_path = os.path.basename(__file__)
    rescue_issue.rescue_issue(e, script_path)
