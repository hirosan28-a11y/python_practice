# file: src/c4/find.py

import os # 3～5行目までは、プログラムと同じフォルダにあるテキストを読み込むためのプログラム(テキストには記載なし)
current_path = os.path.dirname(__file__)
os.chdir(current_path)

# テキストからキーワードを探す
key = "find"

with open("mt7_7.txt", mode="r",encoding="utf-8") as tf:
    # 1行ずつファイルを読む
    for i, line in enumerate(tf):
        # 文字列 key が行に含まれるか？
        if line.find(key) >= 0:
            print(line.find(key,31))
            print(i + 1, ":", line)
