import modules.classification_foods as cf

food_name = input("食べ物の名前を入力してください: ")

response = cf.classify_food(food_name)
print(response)
is_japanese = response["is_japanese"]
print(isinstance(is_japanese, bool))
