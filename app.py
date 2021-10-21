from flask import Flask, render_template, request
from get_data import get_klines


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        list = {"15m":"15MIN","1h":"1HOUR","4h":"4HOUR","1d":"1DAY","1min":"1MIN"}
        return render_template('index.html', ticker_list=list)
    else:
        coin_data = get_klines(request.form['selection'])
        return render_template('main.html', coin_data=coin_data)

@app.route("/settings")
def settings():
    return "settings"
