# じゃんけんゲーム
# randomモジュールの取り込み
import random

# 手をリストで表現
hand = ["グー", "チョキ", "パー", "ゲーム終了"]

print("=== じゃんけんしましょう！ ===")

while True:
    # コンピュータの手を決定
    com = random.randint(0, 2)

    # ユーザの手を入力してもらう
    print("手を選んでください")
    for i, desc in enumerate(hand):   # enumerate関数(P.095)でインデックス番号も表示
        print(i, desc)                # 数値とじゃんけんの手の対応を説明

    you = int(input("出す手を数値で入力: "))

    if you == 3:
        break
    if you < 0 or you > 2:
        print("0から3の間で入力してね")
        continue

    # 手を表示
    print("----")
    print("自分:", hand[you])
    print("相手:", hand[com])
    input("---") #この「　input("---")　」は、じゃんけんの直後、一旦止めるため
    # じゃんけんの勝敗を判定する
    j = (you - com + 3) % 3

    if j == 0:
        print("あいこ")
    elif j == 1:
        print("負け(ToT)")
    else:
        print("勝ち!!")

print("終了")
input("...")
