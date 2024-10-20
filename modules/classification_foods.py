import re

import yaml

import modules.openai_api as gpt
import modules.github_api as github

with open("foods.yml") as f:
    foods = yaml.safe_load(f)

root_keys = list(foods.keys())


def is_japanese(food):
    for item in foods["japanese"]:
        if re.search(re.escape(item), food):
            return True
    return False


def append_food_list(country, food):
    # checkoutしたあとのfoods.ymlを読み込む
    with open("foods.yml") as f:
        foods = yaml.safe_load(f)

    if food not in foods[country]:
        foods[country].append(food)
        with open("foods.yml", "w", encoding="utf-8") as f:
            yaml.dump(foods, f, allow_unicode=True)
        return True
    else:
        return False


def classify_food(food_name):
    prompt = f"""
{food_name}が日本食かどうかを判別し、<<is_japanese>>としてbool値を出力します。
出力は[出力形式]で示した通りのJSON形式で返します。
is_japanese = Trueの場合、{food_name}から日本食であることを判別できる箇所を<<japanese_keyword>>として出力します。

[is_japaneseの判別基準と出力値]
日本食: True
それ以外: False

[出力形式]
is_japanese: bool
japanese_keyword: <<japanese_keyword>>

[例]
food_name: "巻き寿司"
output: "is_japanese": True, "japanese_keyword": "寿司"

food_name: "ピザ"
output: "is_japanese": False, "japanese_keyword": ""
"""
    response = gpt.post(prompt, temperature=0.0, json=True)
    response_content = gpt.content(response, as_json=True)
    return response_content


def push_to_master_list(country, japanese_keyword):
    current_branch = github.get_current_branch()
    github.checkout_and_pull("master/add_japanese_food")
    appendance = append_food_list(country, japanese_keyword)
    if appendance:
        commit_message = f"Add {japanese_keyword} to foods.yml"
        github.commit_and_push_to_branch(
            "master/add_japanese_food", commit_message, "foods.yml"
        )
    github.checkout_and_pull(current_branch)
