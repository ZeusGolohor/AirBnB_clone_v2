#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Defines the index method for the app.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Defines the hbnb method for the app.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Defines the hbnb method for the app.
    """
    pro = text.replace('_', ' ')
    return f"C {pro}"


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def pyt(text='is cool'):
    """
    Defines the python route.
    """
    pro_text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
