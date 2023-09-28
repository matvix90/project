# project
Hack Game

#### Video Demo:  [Youtube Video](https://youtu.be/ueMjsCG1xFY)

#### Description:

<img src="./static/hacker_game.jpg" width="500" height="auto">

The project is created with flask (framework python) and sqlite3 for the backend and with bootstrap5 (framework html) and css for the frontend.
It is used to understand what the vulnerabilities of a website may be and to learn about the various types of attacks.

There are 3 levels:
- In the level 1 the login page have a vulnerability that can use to enter with SQL Injection. In the app you can find some advice on how to pass the level.
- In the level 2 the login page doesn't have a vulnerability and can be pass only with Bruteforce attack. In helpers.py you cand find some fuctions which may be right for you!
- In the level 3 you can see how to implement a simple map with folium lib. The map was rendered in the app as an iframe and there is a marker position that show your   
   latitude and longitude with ip position.

# Table of Contents
1. [Background](#background)
1. [Running](#running)
1. [Understending](#understanding)
1. [Hints](#hints)
1. [Resources](#resources)


## Background

If you want understand how the app work you have to learn what is the SQL Injection and Bruteforce.
Here is a short summary:

- #### SQL Injection: 
SQL injection (SQLi) is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. This can allow an attacker to view data that they are not normally able to retrieve. This might include data that belongs to other users, or any other data that the application can access. In many cases, an attacker can modify or delete this data, causing persistent changes to the application's content or behavior.
In some situations, an attacker can escalate a SQL injection attack to compromise the underlying server or other back-end infrastructure. It can also enable them to perform denial-of-service attacks.

- #### Bruteforce: 
A brute force attack is a hacking method that uses trial and error to crack passwords, login credentials, and encryption keys. It is a simple yet reliable tactic for gaining unauthorized access to individual accounts and organizations’ systems and networks. The hacker tries multiple usernames and passwords, often using a computer to test a wide range of combinations, until they find the correct login information.
The name "brute force" comes from attackers using excessively forceful attempts to gain access to user accounts. Despite being an old cyberattack method, brute force attacks are tried and tested and remain a popular tactic with hackers.


## Running

To run the server to render the app use the command:

```python

flask run

```


## Understanding

+ #### app.py
   The file app.py is made up of 4 level functions (level1, level2, level3, finish), then there are start function that provide to set users table(database SQL) and about function that provide to give advice to finish the game. 

+ #### helpers.py
   In the file helpers.py you may find some functions:
   - Function that performs a Bruteforce attack against a login page.
   - Function login required to ask session in some page of the app.
   - Function that provides geolocalization.

+ #### requirements.txt
   File where you may find all libraries used in the app.

+ #### static/
   Directory where you may find some images used in the app.

+ #### templates/
   Directory where you may find html files (make with bootstrap) witch is rendered on the app. 


## Hints

To execute SQL Injection you can use a sql query like that:

```sql

' OR 'a'='a';--

```

To execute Bruteforce attack you can use something like that:

```python

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

```

## Resources

- #### SQL Injection: [SQLInjection](https://portswigger.net/web-security/sql-injection)

- #### Bruteforce: [Bruteforce](https://www.fortinet.com/it/resources/cyberglossary/brute-force-attack)

- #### Geolocation: [Geolocation](https://python-visualization.github.io/folium/latest/)