import os
import modules.zipcode_api
import modules.openai_api
import modules.github_api
import modules.issue

zipcode = modules.zipcode_api
gpt = modules.openai_api
github = modules.github_api
issue = modules.issue

zcode = input("郵便番号を入力してください: ")
address = zipcode.get(zcode).json()

prompt = f"""
{address}のエリアに応じて<<area>>をjson形式で出力してください。
ただし、<<area>>は必ず1文字の数字であること。
エリア: <<area>> の対応表は以下です。
関東: 1,
関西: 2,
その他: 3

[出力項目]
area: <<area>>
"""

gpt_response = gpt.post(prompt, temperature=0.0, json=True)
area = int(gpt.content_for_json(gpt_response)["area"])

try:
    if area == 1:
        print("関東〜〜〜〜〜！！！")
    elif area == 2:
        print("関西〜〜〜〜〜！！！")
    elif area == 3:
        area / 0  # ゼロ除算エラーを発生させる
except Exception as e:
    script_path = os.path.basename(__file__)
    issue.rescue(e, script_path)
