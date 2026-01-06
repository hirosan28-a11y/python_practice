import random
from flask import Flask

# ランダムに表示する名言の一覧 --- (①)
quotes = [
    "沈黙を突き詰めるとシンプルになる - スティーブ・ジョブズ",
    "完璧を目指すよりまずは実行することが重要である - マーク・ザッカーバーグ",
    "ビジョンには固執し、詳細には柔軟に - ジェフ・ベゾス",
    "人生がどんなに困難に見えても、必ずできることがある - スティーブン・ホーキング",
    "早めに失敗しよう、できるだけ多く失敗しよう - ケント・ベック",
    "未来を予測する最良の方法は、未来を創ることだ - ピーター・ドラッカー"
]

# Flaskのオブジェクトを作成 --- (②)
app = Flask(__name__)

# ルートURLにアクセスした時の処理 --- (③)
@app.route("/")
def index():
    # ランダムな数値を生成し名言を取り出す --- (④)
    num = random.randint(0, 5)
    msg = quotes[num]

    # HTMLに数字と名言を埋め込んで返す --- (⑤)
    html = f"""
    <html><meta charset="UTF-8"><body>
    <div style="text-align: center; border: 1px solid; padding: 2em;">
        <h1>[ {num + 1} ]</h1>
        <p>{msg}</p>
    </div>
    <a href="/">→ 更新する</a>
    </body></html>
    """
    return html

if __name__ == "__main__":
    # Flaskサーバを起動 --- (⑥)
    app.run(host="127.0.0.1", port=8888, debug=True)
