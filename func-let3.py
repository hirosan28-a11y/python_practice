# 引数に関数を要求する関数を定義
def calc_5_3(func):
    return func(5, 3)

result = calc_5_3(lambda a, b: a * b)
print(result)   # 表示結果 → 15

# 引数に他の関数を指定する --- (3)
result = calc_5_3(lambda a, b: a + b)
print(result)   # 表示結果 → 8