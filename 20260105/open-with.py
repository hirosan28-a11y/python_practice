# file: src/c4/open-with.py

import os # 3～5行目までは、プログラムと同じフォルダにあるテキストを読み込むためのプログラム(テキストには記載なし)
current_path = os.path.dirname(__file__)
os.chdir(current_path)


with open("test2.txt", mode="w", encoding="utf-8") as f:
    f.write("私は失敗したことがない。\n")
    f.write("ただ、一万通りの方法を\n見つけただけだ。\n")
