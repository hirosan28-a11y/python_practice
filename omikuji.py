import random

omikuji = [
    "大吉",
    "吉",
    "中吉",
    "小吉",
    "末吉",
    "凶",
    "大凶"]

i = random.randint(0, len(omikuji) - 1)

print(omikuji[i])
