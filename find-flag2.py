
foodstuff = ["Banana",  "Fish", "Carrot", "cabbage"]

flag_found = False
for food in foodstuff:
    if food == "Mango":
        flag_found = True
        break

if flag_found:
    print("マンゴーが入っています")
else:
    print("ありません。")
