import yaml as yml
import modules.openai_api as gpt

with open("foods.yml") as f:
    foods = yml.safe_load(f)

input = input("食べ物の名前を入力してください: ")

prompt = f"""
{input}がどこの国の料理かを判別し、<<country>>として出力します。
出力は[出力形式]で示した通りのJSON形式で返します。
countryは[出力値]からいずれかの値を取ります。

[出力値]
日本食: japanese
フレンチ: french
それ以外: other

[出力形式]
country: <<country>>
"""

if input in foods['japanese']:
    print("入力された食べ物は日本食です。")
elif input in foods['french']:
    print("入力された食べ物はフレンチです。")
else:
    gpt_response = gpt.post(prompt, temperature=0.0, as_json=True)
    country = gpt.content_for_json(gpt_response)["country"]
    if country == "japanese":
        print("入力された食べ物は日本食です。")
    elif country == "french":
        print("入力された食べ物はフレンチです。")

