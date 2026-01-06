from flask import Flask, request

app = Flask(__name__)

# ルートURLにアクセスした時の処理
@app.route("/")
def show_form():
    # フォームを表示
    return """
    <form action="/calc">
        <input type="text" name="v1" value="5">
        <input type="text" name="v2" value="10">
        <input type="submit" value="計算">
    </form>
    """

# /calc にアクセスした時の処理
@app.route("/calc")
def calc():
    # パラメータを取得
    v1 = int(request.args.get("v1"))
    v2 = int(request.args.get("v2"))

    # 足し算して結果を表示
    answer = v1 + v2
    return f"<h1>{v1} + {v2} = {answer}</h1>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888, debug=True)
