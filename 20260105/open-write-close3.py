import os # 1～3行目までは、プログラムと同じフォルダにあるテキストを読み込むためのプログラム(テキストには記載なし)
current_path = os.path.dirname(__file__)
os.chdir(current_path)

# file: src/c4/open-write-close.py

# (1)ファイルを開く
a_file = open("test.txt", mode="w", encoding="utf-8")

# (2)ファイルに書き込む
a_file.write("私は失敗したことがない。\n")
a_file.write("ただ、一万通りの方法を\n見つけただけだ。\n")
a_file.write(" - トーマス・エジソン\n")

# (3)ファイルを閉じる
a_file.close()
