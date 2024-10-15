import re

import yaml

import modules.openai_api as gpt

with open("foods.yml") as f:
    foods = yaml.safe_load(f)

root_keys = list(foods.keys())


def is_japanese(food):
    for item in foods["japanese"]:
        if re.search(re.escape(item), food):
            return True
    return False


def append_japanese_food(food):
    if food not in foods["japanese"]:
        foods["japanese"].append(food)
        with open("foods.yml", "w", encoding="utf-8") as f:
            yaml.dump(foods, f, allow_unicode=True)


def classify_food(food_name):
    prompt = f"""
{food_name}がどこの国の料理かを判別し、<<country>>として出力します。
出力は[出力形式]で示した通りのJSON形式で返します。
countryは[出力値]からいずれかの値を取ります。
このとき、{food_name}が日本食の場合は日本食であることを判別できる箇所を<<japanese_keyword>>として出力します。

[出力値]
日本食: japanese
それ以外: other

[出力形式]
country: <<country>>
japanese_keyword: <<japanese_keyword>>

[例]
food_name: "巻き寿司"
output: "country": "japanese", "japanese_keyword": "寿司"

food_name: "ピザ"
output: "country": "other", "japanese_keyword": ""
"""
    response = gpt.post(prompt, temperature=0.0, json=True)
    response_content = gpt.content(response, as_json=True)
    country = response_content["country"]
    japanese_keyword = response_content["japanese_keyword"]
    return [country, japanese_keyword]
