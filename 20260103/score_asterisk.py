# 名前と点数のデータ
scores = {
    "山田": 70,
    "佐藤": 90,
    "山本": 30,
    "田中": 50
}

# 表示
for name, score in scores.items():
    stars = "*" * (score // 10)
    print(f"{name} {stars}")
