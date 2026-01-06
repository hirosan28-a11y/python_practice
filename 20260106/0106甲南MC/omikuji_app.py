from flask import Flask, render_template
import random

app = Flask(__name__)

omikuji = [
    "大吉",
    "吉",
    "中吉",
    "小吉",
    "末吉",
    "凶",
    "大凶"
]

@app.route("/")
def index():
    # 初回アクセスは結果なし
    return render_template("index.html", result=None)

@app.route("/draw")
def draw():
    # おみくじを引く
    result = random.choice(omikuji)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
