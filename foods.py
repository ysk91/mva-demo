import yaml as yml
import modules.openai_api as gpt
import modules.classification_foods as cf

with open("foods.yml") as f:
    foods = yml.safe_load(f)

input = input("食べ物の名前を入力してください: ")
key = cf.is_japanese(input)

if key:
    print("入力された食べ物は日本食です。")
else:
    response = cf.classify_food(input)
    country = gpt.content(response, as_json=True)["country"]
    japanese_keyword = gpt.content(response, as_json=True)["japanese_keyword"]
    if country == "japanese":
        print("入力された食べ物は日本食です。")
        cf.append_japanese_food(japanese_keyword)
    else:
        print("入力された食べ物は日本食ではありません。")
