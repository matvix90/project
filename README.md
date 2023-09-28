# project
cs50-final-project

#### Video Demo:  https://youtu.be/ueMjsCG1xFY

#### Description:

<img src="./static/hacker_game.jpg" width="500" height="auto">

Hack Game 

The project is created with flask (framework python) and sqlite3 for the backend and with bootstrap5 (framework html) and css for the frontend.
It is used to understand what the vulnerabilities of a website may be and to learn about the various types of attacks.

There are 3 levels:
1- In the level 1 the login page have a vulnerability that can use to enter with SQL Injection. In the app you can find some advice on how to pass the level.
2- In the level 2 the login page doesn't have a vulnerability and can be pass only with Bruteforce attack. In helpers.py you cand find some fuctions which may be right for you!
3- In the level 3 you can see how to implement a simple map with folium lib. The map was rendered in the app as an iframe and there is a marker position that show your   
   latitude and longitude with ip position.

Understanding App

app.py
The file app.py is made up of 4 level functions (level1, level2, level3, finish), then there are start function that provide to set users table(database SQL) and about function that provide to give advice to finish the game. 

helpers.py
In the file helpers.py you may find some functions:
- Function that performs a Bruteforce attack against a login page.
- Function login required to ask session in some page of the app.
- Function that provides geolocalization.

requirements.txt
File where you may find all libraries used in the app.

static/
Directory where you may find some images used in the app.

templates/
Directory where you may find html files (make with bootstrap) witch is rendered on the app. 