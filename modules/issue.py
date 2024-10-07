import subprocess
import traceback
import re
from modules import config
import modules.openai_api as gpt
import modules.github_api as github

REPOSITORY = config.REPOSITORY


def rescue(e):
    traceback_details = traceback.format_tb(e.__traceback__)
    file_pattern = f'{REPOSITORY}/([^"]+)"'
    script = re.search(file_pattern, traceback_details[0]).group(1)
    error_script = github.get_contents(script)

    modules_list = subprocess.run(
        ["ls", "modules"], capture_output=True, text=True
    ).stdout.splitlines()
    modules_contents = []
    for module in modules_list:
        content = github.get_module_contents(module)
        if content is not None:
            modules_contents.append(content)

    prompt = f"""
[命令]
[エラー内容]を解析し、原因と改善策を<<comment>>に記述してください。
<<comment>>の内容を簡単にまとめ、<<title>>としてください。
結果をJSON形式で出力してください。
JSONに含める項目は[出力項目]の通りです。

[<<comment>>の形式]
## 発生エラー
```
{traceback_details}
```
(発生したエラーについて説明)

## 原因
(エラーについて、発生箇所と原因を説明
特に、本エラーは[エラーが発生したスクリプト]を実行した際に発生したものです。
このスクリプト内で、[エラー内容]が発生する箇所を特定しつつ、[モジュール]が原因である可能性も考慮してください)

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
{f"{type(e).__name__}: {e}"}

[エラーが発生したスクリプト]
{error_script}

[モジュール]
{modules_contents}
"""

    #  TODO modelをo1に変更したらうまくいくかもしれない
    gpt_response = gpt.post(prompt, temperature=0.7, json=True)
    body = gpt.content_for_json(gpt_response)
    issue_title = body["title"]
    issue_body = body["comment"]
    # github.create_issue(issue_title, issue_body)
    print(issue_title) #  デバック用
    print(issue_body) #  デバック用
    print(script) #  デバック用


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
