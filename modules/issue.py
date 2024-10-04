import subprocess
import modules.openai_api
import modules.github_api

gpt = modules.openai_api
github = modules.github_api


def rescue(e, script_path):
    modules_list = subprocess.run(
        ["ls", "modules"], capture_output=True, text=True
    ).stdout.splitlines()
    repository_contents = []
    repository_contents.append(script_path)
    for module in modules_list:
        content = github.get_module_contents(module)
        if content is not None:
            repository_contents.append(content)

    prompt = f"""
[命令]
[エラー内容]を解析し、原因と改善策を<<comment>>に記述してください。
<<comment>>の内容を簡単にまとめ、<<title>>としてください。
結果をJSON形式で出力してください。
JSONに含める項目は[出力項目]の通りです。

[<<comment>>の形式]
## 発生エラー
```
{e}
```
(発生したエラーについて説明)

## 原因
(エラーについて、発生箇所と原因を説明
特に、本エラーは[モジュール]内の{script_path}を実行した際に発生したものです。
このファイル内で、[エラー内容]が発生する箇所を特定しつつ、他のファイルが原因である可能性も考慮してください)

## 改善策
(エラーを解消するために、どのファイルに対してどのような修正を行うべきかを記述)

### 対象ファイル
（修正すべきファイルのパスを記載）

### 修正内容
（修正後のコードを記載）

[出力項目]
title: <<title>>
comment: <<comment>>

[エラー内容]
{e}

[モジュール]
{repository_contents}
"""

    #  TODO modelをo1に変更したらうまくいくかもしれない
    gpt_response = gpt.post(prompt, temperature=0.7, json=True)
    body = gpt.content_for_json(gpt_response)
    issue_title = body["title"]
    issue_body = body["comment"]
    github.create_issue(issue_title, issue_body)


def record(purpose, python_code, script_path=None):
    issue_title = purpose
    issue_body = f"""
## 対象スクリプト
{script_path}

```python
## 実装コード
{python_code}
```
"""

    github.create_issue(issue_title, issue_body)
