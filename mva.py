import modules.openai_api
import modules.github_api
import modules.issue

gpt = modules.openai_api
github = modules.github_api
issue = modules.issue

purpose = input("目的を入力してください: ")
data = input("データを入力してください: ")

prompt = f"""
[命令]
[目的]を達成するためのpythonコードを作成してください。
出力はpythonコードのみとし、説明文や結果などの説明はしないでください。

[目的]
{purpose}

[データ]
{data}

[出力の制限 #  最重要事項]
[出力結果]は`exec([出力結果])`で実行されます。
この処理に適したプレーンなテキスト形式で出力してください。
マークダウンのためのコードブロックは不要です。
処理を実行した結果を返り値として返すようにしてください。
"""

gpt_responce = gpt.post(prompt, temperature=0.7, json=False)
python_code = gpt.content(gpt_responce)

print(python_code)
is_execute = input("このコードを実行しますか？(y/n): ")

if is_execute.upper() in ["Y", "YES"]:
    exec_globals = {}
    exec(python_code, exec_globals)
    result = exec_globals.get("result", None)
    print(result)
else:
    print("処理を終了します。")

if result:
    is_record_issue = input("このコードをGitHub Issueに記録しますか？(y/n): ")

    if is_record_issue.upper() in ["Y", "YES"]:
        issue.record(purpose, python_code)
else:
    print("処理に失敗しました。")
