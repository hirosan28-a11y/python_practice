from itertools import permutations, product
from fractions import Fraction

def apply(op, a, b):
    """a (op) b を計算。割り算の0除算は None を返す。"""
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return None if b == 0 else a / b
    raise ValueError("unknown op")

def four_fours_results():
    nums = [Fraction(4), Fraction(4), Fraction(4), Fraction(4)]
    ops = ['+', '-', '*', '/']

    results = set()

    # 4つの数の並び（同じ4でも、形としては順序を総当たりしてOK）
    for a, b, c, d in set(permutations(nums, 4)):
        # 3つの演算子の並び
        for op1, op2, op3 in product(ops, repeat=3):

            # カッコの付け方（2項演算3回＝5通り）
            # 1) ((a op1 b) op2 c) op3 d
            r1 = apply(op1, a, b)
            if r1 is not None:
                r2 = apply(op2, r1, c)
                if r2 is not None:
                    r3 = apply(op3, r2, d)
                    if r3 is not None:
                        results.add(r3)

            # 2) (a op1 (b op2 c)) op3 d
            r1 = apply(op2, b, c)
            if r1 is not None:
                r2 = apply(op1, a, r1)
                if r2 is not None:
                    r3 = apply(op3, r2, d)
                    if r3 is not None:
                        results.add(r3)

            # 3) (a op1 b) op3 (c op2 d)  ※左右に分ける形
            left = apply(op1, a, b)
            right = apply(op2, c, d)
            if left is not None and right is not None:
                r3 = apply(op3, left, right)
                if r3 is not None:
                    results.add(r3)

            # 4) a op1 ((b op2 c) op3 d)
            r1 = apply(op2, b, c)
            if r1 is not None:
                r2 = apply(op3, r1, d)
                if r2 is not None:
                    r3 = apply(op1, a, r2)
                    if r3 is not None:
                        results.add(r3)

            # 5) a op1 (b op2 (c op3 d))
            r1 = apply(op3, c, d)
            if r1 is not None:
                r2 = apply(op2, b, r1)
                if r2 is not None:
                    r3 = apply(op1, a, r2)
                    if r3 is not None:
                        results.add(r3)

    return results

def main():
    results = four_fours_results()

    # 整数だけ欲しい場合（問題文の「数字」だと通常は整数を想定）
    integers = sorted({int(x) for x in results if x.denominator == 1})

    print("作れる整数の個数:", len(integers))
    print("作れる整数一覧:")
    print(integers)

    # 参考：分数も含めて全部見たい場合（コメント外す）
    # all_vals = sorted(results)
    # print("分数も含む結果の個数:", len(all_vals))
    # print(all_vals)

if __name__ == "__main__":
    main()
