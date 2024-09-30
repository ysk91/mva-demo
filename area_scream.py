import subprocess
import modules.zipcode_api
import modules.openai_api
import modules.github_api

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

github = modules.github_api

modules_list = subprocess.run(['ls', 'modules'], capture_output=True, text=True).stdout.splitlines()

modules_contents = []
for module in modules_list:
    content = github.get_module_contents(module)
    if content != None: modules_contents.append(content)

prompt = f"""
[命令]
発生したエラーを解析し、原因と改善策を<<body>>に記述してください。
bodyの内容を簡単にまとめ、<<title>>としてください。
結果をJSON形式で出力してください。
JSONに含める項目は[出力項目]の通りです。

[出力項目]
title: <<title>>
body: <<body>>

[モジュール]
{modules_contents}
"""

gpt_responce = gpt.post(prompt, temperature=0.7)
body = gpt.content(gpt_responce)

issue_title = body.title
issue_body = body.text

new_issue = github.create_issue(issue_title, issue_body)
