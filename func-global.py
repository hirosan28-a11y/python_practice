# 関数の外側でvalueに100を代入
value = 100

def changeValue():
    # valueをグローバル宣言
    global value

    value = 20
    
changeValue()
print("value=",value)
