import os
current_path = os.path.dirname(__file__)
os.chdir(current_path)
# 1～3行目までは、プログラムと同じフォルダにあるテキストを読み込むためのプログラム(テキストには記載なし)


# (1)テキストファイルを開く
a_file = open("mt7_72.txt", encoding="sjis")

# (2)テキストを読む
s = a_file.read()

# (3)ファイルを閉じる
a_file.close()

# 結果を表示する
print(s)
