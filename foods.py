import yaml

import modules.classification_foods as cf

with open("foods.yml") as f:
    foods = yaml.safe_load(f)

food_name = input("文章を入力してください: ")
is_japanese_food = cf.is_japanese(food_name)

#  OpenAI API使用料を削減するため、はじめにfoods.ymlに日本食のキーワードが含まれているかを確認する
if is_japanese_food:
    print("入力された文章に日本食が含まれています。")
else:
    response = cf.classify_food(food_name)
    is_japanese = response["is_japanese"]
    japanese_keyword = response["japanese_keyword"]
    if is_japanese:
        print("入力された文章に日本食が含まれています。")
        cf.push_to_master_list("japanese", japanese_keyword)
    else:
        print("入力された文章に日本食は含まれていません。")
