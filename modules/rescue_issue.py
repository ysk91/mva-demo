import subprocess
import modules.openai_api
import modules.github_api

gpt = modules.openai_api
github = modules.github_api

def rescue_issue(e, script_path):
    modules_list = subprocess.run(['ls', 'modules'], capture_output=True, text=True).stdout.splitlines()

    repository_contents = []
    repository_contents.append(script_path)
    for module in modules_list:
        content = github.get_module_contents(module)
        if content != None: repository_contents.append(content)

    prompt = f"""
[命令]
[エラー内容]を解析し、原因と改善策を<<comment>>に記述してください。
<<comment>>の内容を簡単にまとめ、<<title>>としてください。
結果をJSON形式で出力してください。
JSONに含める項目は[出力項目]の通りです。

[<<comment>>の形式]
## 発生エラー
(発生したエラーについて説明)

## 原因
(エラーについて、発生箇所と原因を説明)

## 改善策
(エラーを解消するために、どのファイルに対してどのような修正を行うべきかを記述)

[出力項目]
title: <<title>>
comment: <<comment>>

[エラー内容]
{e}

[モジュール]
{repository_contents}
"""

    gpt_responce = gpt.post(prompt, temperature=0.7, json=True)
    body = gpt.content_for_json(gpt_responce)
    issue_title = body['title']
    issue_body = body['comment']

    github.create_issue(issue_title, issue_body)


def record_issue(purpose, python_code):
    issue_title = purpose
    issue_body = f"""
```python
{python_code}
```
"""

    github.create_issue(issue_title, issue_body)
