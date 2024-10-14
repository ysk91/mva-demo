import yaml as yml

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

print(input in foods['japanese'])
