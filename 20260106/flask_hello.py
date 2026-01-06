from flask import Flask

# Flaskのオブジェクトを作成（①）
app = Flask(__name__)

# ルートURLにアクセスした時の処理（②）
@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    # Flaskサーバを起動（③）
    app.run(host="0.0.0.0", port=8888, debug=True)
