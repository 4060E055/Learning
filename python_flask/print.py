from flask import Flask, request, jsonify, render_template
import poker as p
import fabo as f

# 把原路徑(static_folder)修改成新路徑static_url_path
# 更改完之後  只能透過「http://10.1.0.226:4998/static2/mylove.jpg」來存取圖片
app = Flask(__name__, static_url_path="/static2", static_folder="./static")


# ---------GET方式----------------
@app.route("/")  # 預設進入首頁
def heelo():
    return "it's string"


@app.route("/heelo1/<username>")  # 設定網址連結的函數
def heelo1(username):  # 傳參數進去，會根據網址變動
    return f"<h1>your name is {username}<h1>"

#模板需要創建一個「templates」的目錄，把模板放進去
@app.route("/heelo2/<username>")  # 設定網址連結的函數
def heelo2(username):  # 傳參數進去，會根據網址變動
    # 套用模板輸出變數，多個變數後面就一直「,」加過去
    return render_template('index.html', username=username, userage=22)


@app.route("/add/<x>/<y>")
def add(x, y):
    # return int(x)+int(y) #回傳的一定要是字串不能是數字 會error
    return str(int(x) + int(y))


# 傳遞「?」後面的參數
## /hello_get?username=Allen&userage=22
@app.route("/hello_get")
def hello_get():
    username = request.args.get("username")
    userage = request.args.get("userage")

    if username == None or userage == None:  # 防呆 預防傳入空值
        return "Who are you?"

    return "<h1>Hello {}, you are {} years old.<h1>".format(username, userage)


# ---------以上參數送出都是GET方式----------------


# ---------POST方式----------------
@app.route("/hello_post", methods=["GET", "POST"])  # 預設只有GET
def hello_post():
    # form 後面沒有指定送出的話，預設就是送給自己
    outStr = """
    <form action="/hello_post" method="POST">
        <label>What's your name?</label>
        <input name="username">
        <button>Sumit</button>
    </form>
    """

    method = request.method  # 回傳GET or POST
    if method == "POST":
        username = request.form.get("username")
        outStr += """<h1>Hello {}<hi>""".format(username)
    elif method == "GET":
        username = request.args.get("username")
        outStr += """<h1>Hello {}<hi>""".format(username)

    return outStr


# 查詢費事數列第幾項
# url= http://10.1.0.226:4998/getFabo?n=6
## /getFabo?n=3
@app.route("/getFabo")
def getFabo():
    n = request.args.get("n")
    result = f.Func(int(n))  # 丟進去要是數值
    return str(result)  # 丟出來要是字串


# 發牌code: input玩家人數，output每人的撲克牌
## /poker?player=5
@app.route("/poker")
def poker():
    player = int(request.args.get("player"))
    result = p.poker(player)

    return jsonify(result)  # 漂亮輸出json


#
# @app.route('/hello_mylove')
# def hello_mylove():
#     outStr="""
#     <link href="/static/css.mystyle.css" rel="stylesheet" type="text/css>
#     """

# ---------以上參數送出都是POST方式----------------
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4998)  # debug=True 可以讓他自動套用到網頁(需F5網頁)
