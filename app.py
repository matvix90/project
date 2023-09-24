from flask import Flask, flash, redirect, render_template, request, abort, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from cs50 import SQL

from random import choices
from string import digits

from helpers import login_required, get_location

import folium

# Configure application
app = Flask(__name__)

# Configure secret Key
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure database
db = SQL("sqlite:///data.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def start():

    # Forget any user_id
    session.clear()

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

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            abort(403)

        user = db.execute("SELECT * FROM users WHERE name = '%s'" % (username))

        if len(user) != 1:
            abort(403)
        
        # Remember which user has logged in
        session["user_id"] = user[0]["name"]

        flash("Welcome ")
        flash(session["user_id"])

        return redirect("/level2")

    else:
        return render_template("level1.html")


@app.route('/level2', methods=['GET', 'POST'])
@login_required
def level2():
    """Level 2 -- Bruteforce"""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            abort(403)

        user = db.execute("SELECT * FROM users WHERE name = ?", username)

        if len(user) != 1 or not check_password_hash(user[0]["pass"], password):
            abort(403)

        return redirect("/level3")

    else:
        
        return render_template("level2.html")


@app.route("/level3")
#@login_required
def level3():
    """Level 3"""
    p = get_location()
    lat = p["lat"]
    lon = p["lon"]

    # Embed a map as an iframe on a page.
    m = folium.Map([lat, lon], zoom_start=12)

    folium.Marker(
        location=[lat, lon],
        tooltip="You are here!",
        popup="Yuo",
        icon=folium.Icon(icon="cloud"),
    ).add_to(m)

    # Set the iframe width and height
    m.get_root().width = "50%"
    iframe = m.get_root()._repr_html_()
    
    return render_template("level3.html", iframe=iframe)
    

@app.route("/about")
def about():
    """About Levels"""
    return render_template("about_levels.html")


@app.route("/finish")
@login_required
def finish():
    """Finish game"""
    return render_template("finish.html")
