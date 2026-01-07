from flask import Flask, request

app = Flask(__name__)

# トップページ：入力フォームを表示
@app.route("/")
def show_form():
    return """
    <h2>BMI判定</h2>
    <form action="/bmi">
        身長(cm)：<input type="text" name="height" value=""><br><br>
        体重(kg)：<input type="text" name="weight" value=""><br><br>
        <input type="submit" value="計算">
    </form>
    """

# BMI計算ページ
@app.route("/bmi")
def bmi_calc():
    try:
        # 入力値を取得
        height = float(request.args.get("height"))
        weight = float(request.args.get("weight"))

        # BMI計算
        height_m = height / 100
        bmi = weight / (height_m * height_m)

        # 判定
        if bmi < 18.5:
            result = "痩せ型"
        elif bmi < 25:
            result = "標準体重"
        elif bmi < 30:
            result = "肥満（軽）"
        else:
            result = "肥満（重）"

        # 結果表示
        return f"""
        <h2>BMI判定結果</h2>
        <p>BMI：{bmi:.1f}</p>
        <p>判定：{result}</p>
        <a href="/">戻る</a>
        """

    except:
        return """
        <p>入力に誤りがあります。</p>
        <a href="/">戻る</a>
        """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888, debug=True)
