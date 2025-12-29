
fruits = {"Banana":300, "Mango":400, "Fish":240, "Carrot":180}

for name in fruits.keys():
    price = fruits[name]
    s = "{0}は、{1}円です。".format(name, price)
    print(s)
