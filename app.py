#!/usr/bin/env python3

from flask import Flask
from flask import render_template

from os import getcwd

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"

@app.route("/index")
def index(name=None):
	return render_template("index.html", name=name)

if __name__ == "__main__":
	app.run(debug=True)
