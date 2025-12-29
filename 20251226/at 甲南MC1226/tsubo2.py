#繰り返し坪数を調べるプログラム
while True:
    user = input("坪数は？")
    if user =="" or user == "q": break # 修正点
    tsubo = float(user)
    m2 = tsubo * 3.31
    s = "{0}坪は、{1}㎡です".format(tsubo, m2)
    print(s)

                
