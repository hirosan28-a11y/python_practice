import os # 1～3行目までは、プログラムと同じフォルダにあるテキストを読み込むためのプログラム(テキストには記載なし)
current_path = os.path.dirname(__file__)
os.chdir(current_path)

# file: src/c4/for-lines.py

with open("mt7_7.txt", encoding="utf-8") as tf:
    for line in tf:
        print(line)
