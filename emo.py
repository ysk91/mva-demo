import modules.issue as issue
import modules.openai_api as gpt

user_input = input("あなたの感情を表現する文を入力してください: ")

prompt = f"""
[ユーザーインプット]を感情分析して、喜怒哀楽のいずれかの感情に分類してください。
分類した感情を<<emotion>>として出力してください。
<<emotion>>は[<<emotion>>一覧]から1つだけ選んでください。
出力形式はJSON形式で、項目は[出力項目]に従ってください。

[ユーザーインプット]
"{user_input}"

[<<emotion>>一覧]
- 喜: 嬉しい気持ち
- 怒: 怒っている気持ち
- 哀: 悲しい気持ち
- 楽: 楽しんでいる気持ち
- 不明: 感情が特定できない
- ゼロ除算: ゼロ除算する指示が入力された

[出力項目]
emotion: <<emotion>>
"""

try:
    gpt_response = gpt.post(prompt, temperature=0.0, json=True)
    emotion = gpt.content(gpt_response, as_json=True)["emotion"]

    if emotion == "喜":
        print("あなたは嬉しい気持ちですね！")
    elif emotion == "怒":
        print("あなたは怒っていますね！")
    elif emotion == "哀":
        print("あなたは悲しい気持ちですね。")
    elif emotion == "楽":
        print("あなたは楽しんでいますね！")
    elif emotion == "ゼロ除算":
        100 / 0
    else:
        print("感情が特定できませんでした。")
except Exception as e:
    issue.rescue(e)
