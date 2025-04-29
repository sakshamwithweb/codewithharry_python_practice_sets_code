# Explore the ‘Flask’ module and create a web server using Flask & Python.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/game")
def hello_gamer():
    return "<h1>Hello, Gamers!</h1>"


app.run()