import yaml

import modules.classification_foods as cf
import modules.github_api as github
import modules.openai_api as gpt

with open("foods.yml") as f:
    foods = yaml.safe_load(f)

food_name = input("食べ物の名前を入力してください: ")
is_japanese_food = cf.is_japanese(food_name)

#  OpenAI API資料料を削減するため、はじめにfoods.ymlに日本食のキーワードが含まれているかを確認する
if is_japanese_food:
    print("入力された食べ物は日本食です。")
else:
    response = cf.classify_food(food_name)
    response_content = gpt.content(response, as_json=True)
    country = response_content["country"]
    japanese_keyword = response_content["japanese_keyword"]
    if country == "japanese":
        print("入力された食べ物は日本食です。")
        cf.append_japanese_food(japanese_keyword)
        commit_message = f"Add {japanese_keyword} to foods.yml"
        github.commit_and_push_to_branch(
            "test/cf_test", commit_message
        )
    else:
        print("入力された食べ物は日本食ではありません。")
