import modules.openai_api as gpt
import modules.github_api as github
import modules.issue as issue

purpose = input("目的を入力してください: ")
data = input("データを入力してください: ")
script_path = input("対象スクリプトのパスを入力してください: ")

script = github.get_file_contents(script_path) if script_path else None

prompt = f"""
[命令]
[目的]を達成するためのpythonコードを作成してください。
[スクリプト]がある場合は、そのコードに対するを参考にしてください。
出力はpythonコードのみとし、説明文や結果などの説明はしないでください。

[目的]
{purpose}

[データ]
{data}

[スクリプト]
{script}

[出力の制限] #  最重要事項
[出力結果]は`exec([出力結果])`で実行されます。
この処理に適したプレーンなテキスト形式で出力してください。
マークダウンのためのコードブロックは不要です。
処理を実行した結果を返り値として返すようにしてください。
"""

gpt_response = gpt.post(prompt, temperature=0.7, json=False)
python_code = gpt.content(gpt_response)

try:
    print(python_code)

    if not script_path:
        is_execute = input("このコードを実行しますか？(y/n): ")

        if is_execute.upper() in ["Y", "YES"]:
            exec_globals = {}
            exec(python_code, exec_globals)
            result = exec_globals.get("result", None)
            print(result)
        else:
            print("処理を終了します。")

    is_record_issue = input("このコードをGitHub Issueに記録しますか？(y/n): ")

    if is_record_issue.upper() in ["Y", "YES"]:
        issue.record(purpose, python_code, script_path)
except Exception as e:
    issue.rescue(e)
