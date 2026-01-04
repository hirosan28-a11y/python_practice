import qrcode

# 文字を入力
text = input("QRコードにしたい文字を入力してください：")

# QRコードを生成
img = qrcode.make(text)

# ファイルに保存
img.save("input_qrcode.png")

print("QRコードを input_qrcode.png として保存しました。")
