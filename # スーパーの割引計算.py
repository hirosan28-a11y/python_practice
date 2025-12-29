# スーパーの割引計算

def calcValue(who, hour, count, value):
    '''あるスーパーでの割引計算を行う関数'''
    info =  "割引なし"
    # 14時に商品を3つ以上で1割引き
    if (hour == 14) and (count >= 3):
      value *= 0.9
        info = "1割引き"
    # 15降に商品を5つ以上で2割引き
    elif (hour== 15) and (count >= 5):
        value *= 0.8
        info = "2割引き"
    # 結果を表示
    value = int(value)
    print("{0}さんは{1}={2}円").format(who, info, value)
calcValue("田中", 15, 3, 1200)
calcValue("佐藤", 14, 5, 2000)
calcValue("鈴木", 15, 8, 5400)