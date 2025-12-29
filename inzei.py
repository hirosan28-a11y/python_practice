def calc_royalty(price, sales, per):
    rate = per / 100
    ro = int(price * sales * rate)
    return ro

price = int(input("定価は？"))
sales = int(input("発行部数は？"))
per = float(input("印税率(%)は？"))

# 結果を表示する
v = calc_royalty(price, sales, per)  # 関数を呼び出す
print("印税額は", v, "円です。")