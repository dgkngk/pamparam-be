from flask import Flask, render_template
from get_data import get_klines


app = Flask(__name__)

@app.route("/")
def index():
    coin_data = get_klines()
    #coin_data = {"chigga":{"k":123,"d":123,"s":"nigga"},"dhigga":{"k":123,"d":123,"s":"nigga"},"thigga":{"k":123,"d":123,"s":"nigga"}}
    return render_template('index.html', coin_data=coin_data)

@app.route("/settings")
def settings():
    return "settings"

@app.route("/deneme")
def deneme():
    return "deneme"