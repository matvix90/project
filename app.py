from flask import Flask, flash, redirect, render_template, request, abort, session
from werkzeug.security import check_password_hash, generate_password_hash

from cs50 import SQL

from random import choices
from string import digits

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQL("sqlite:///data.db")

@app.route("/")
def start():

    db.execute("DELETE FROM users")
    username = "admin"
    password = ''.join(choices(digits, k=4))
    print(password)
    password = generate_password_hash(password)
    db.execute("INSERT INTO users (name, pass) VALUES (?, ?)", username, password)

    return render_template("start.html")


@app.route('/level1', methods=['GET', 'POST'])
def level1():
    """Level 1 -- SQL Injection -- ' OR 'a'='a';--"""

    session.clear()

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            abort(403)

        user = db.execute("SELECT * FROM users WHERE name = '%s'" % (username))

        if len(user) != 1:
            abort(403)

        flash(user[0]["name"])

        return redirect("/level2")

    else:
        return render_template("level1.html")


@app.route('/level2', methods=['GET', 'POST'])
def level2():
    """Level 2 -- Bruteforce"""

    session.clear()

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            abort(403)

        user = db.execute("SELECT * FROM users WHERE name = ?", username)

        if len(user) != 1 or not check_password_hash(user[0]["pass"], password):
            abort(403)

        return redirect("/finish")

    else:
        return render_template("level2.html")
    

@app.route("/about")
def about():
    """About Levels"""
    return render_template("about_levels.html")


@app.route("/finish")
def finish():
    """Finish game"""
    return render_template("finish.html")
