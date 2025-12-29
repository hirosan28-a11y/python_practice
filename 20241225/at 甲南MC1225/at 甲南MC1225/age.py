#年齢を聞き、年代を答えるプログラム

age = int(input("年齢はおいくつですか？"))
if age <=10:
    print("幼年です")
if 10 < age <=20:
    print("少年です")
if 20 < age <=30:
    print("青年です")

if 30 < age <=40:
    print("壮年です")

if 40 < age <=50:
    print("中年です")

if 50 < age <=60:
    print("塾年です")

if 60 < age <=65:
    print("高年です")

if age >65:
    print("老年です")
    
