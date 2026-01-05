#年齢を聞き、年代を答えるプログラム

age = int(input("年齢はおいくつですか？"))
if age <=10:
    print("幼年です")
elif age <=20:
    print("少年です")
elif age <=30:
    print("青年です")

elif age <=40:
    print("壮年です")

elif age <=50:
    print("中年です")

elif age <=60:
    print("塾年です")

elif age <=65:
    print("高年です")

elif age >65:
    print("老年です")
    
