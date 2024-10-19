import yaml

import modules.classification_foods as cf

with open("foods.yml") as f:
    foods = yaml.safe_load(f)

food_name = input("食べ物の名前を入力してください: ")
is_japanese_food = cf.is_japanese(food_name)

#  OpenAI API使用料を削減するため、はじめにfoods.ymlに日本食のキーワードが含まれているかを確認する
if is_japanese_food:
    print("入力された食べ物は日本食です。")
else:
    response = cf.classify_food(food_name)
    country = response[0]
    japanese_keyword = response[1]
    if country == "japanese":
        print("入力された食べ物は日本食です。")
        cf.push_to_master_list(country, japanese_keyword)
    else:
        print("入力された食べ物は日本食ではありません。")
