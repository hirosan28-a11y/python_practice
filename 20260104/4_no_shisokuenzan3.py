enzan = ['*', '+', '-', '/']

for i in enzan:
    for j in enzan:
        for k in enzan:
            expression = "4" + i + "4" + j + "4" + k + "4"
            # "4*4*4*4"
            result = eval(expression)  # 文字列を計算する関数
            print(expression + " =", result)
