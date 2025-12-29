# 動物の最高時速（km/h）
animal_speed_dict = {
    "チーター": 110,
    "トナカイ": 80,
    "シマウマ": 60,
    "ライオン": 58,
    "キリン": 50,
    "ラクダ": 40
}

# 東京から各都市までの距離（km）
distance_dict = {
    "名古屋": 350.6,
    "大阪": 507.5,
    "静岡": 183.7
}

# 表示順を固定
cities = ["名古屋", "大阪", "静岡"]

# 時間計算
def calc_time(dist, speed):
    return round(dist / speed, 1)

# 罫線
line = "+--------+" + "+------" * len(cities) + "+"

# ヘッダ
print(line)
print("|動物名前|", end="")
for city in cities:
    print(f"{city:^6}|", end="")
print()
print(line)

# 本体
for animal, speed in animal_speed_dict.items():
    # 動物名を全角4文字（8桁）に揃える
    name = animal.ljust(4, "　")
    print(f"|{name}|", end="")

    for city in cities:
        t = calc_time(distance_dict[city], speed)
        print(f"{t:>6}|", end="")
    print()

print(line)
