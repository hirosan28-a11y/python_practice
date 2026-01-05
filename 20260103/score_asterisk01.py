# 名前と点数のデータ
test = {
    "山田": 70,
    "佐藤": 90,
    "山本": 30,
    "田中": 50
}

# 表示
for name, point in test.items():
    point = int(point / 10)
    point_bar = "*" * point
    print(name,point_bar)
