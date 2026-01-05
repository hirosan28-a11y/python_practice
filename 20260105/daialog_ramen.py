# ダイアログを表示するために必要なモジュール
import TkEasyGUI as eg # 以降はTkEasyGUIを eg とする

# ラーメンに関する質問ダイアログを表示
ans = eg.popup_yes_no("ラーメンは好きですか？")
if ans == "Yes":
    eg.popup("私も好きです！")
else:
    eg.popup("本当？！ラーメン好きじゃない人もいるんですね。")
    