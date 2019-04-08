import os
from flask import Flask, request, url_for, render_template, redirect
from config import sqlite
from models import sfmodel
import secrets

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def start():
    url = "/home/%s"%(secrets.token_urlsafe(32),)
    return redirect(url, code=302)

@app.route('/home/<sessid>', methods=['GET', 'POST'])
def home(sessid):
    wrong = ""
    usersObj = sfmodel.Users()
    if request.method == 'POST':
        login = request.form["username"]
        password = request.form["password"]
        usersObj.authenticateUser(login, password, sessid)
        wrong = "Invalid username or password."

    user = usersObj.getUserFromSessionToken(sessid)
    if user is None:
        return render_template("login.html", msg=wrong)
    else:
        return render_template("welcome.html", name=user)
    

@app.route("/login", methods=['POST'])
def login():
    sizeImg = request.form['size']
    os.system('convert static/img/bones.png -resize '+sizeImg+'% static/img/bones.png')
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

