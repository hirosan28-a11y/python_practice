def factorial(n):
    # 終了条件
    if n == 0:
        return 1
    # 再帰処理
    return n * factorial(n - 1)

# 実行
print(factorial(7))
