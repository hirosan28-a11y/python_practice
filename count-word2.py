# 単語出現回数をカウント
text = """
keep on asking, and it will be given you:
keep on seeking,and you will find;
keep on knoking, and it will be opened to you;
for everyone knocking, it will be opened.
"""
#単語を区切る
text = text.replace(";", "") # :を削除
text = text.replace(",", "") # ,を削除
text = text.replace(".", "") # .を削除
words = text.split() # 空白で区切ってリストを作成

print(words)
