#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask
from flask import render_template

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


@app.route('/python')
@app.route('/python/<text>', strict_slashes=False)
def pyt(text='is cool'):
    """
    Defines the python route.
    """
    pro_text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<n>', strict_slashes=False)
def num(n):
    try:
        n = int(n)
        return f'{n}'
    except Exception:
        pass


@app.route('/number_template/<n>', strict_slashes=False)
def num_temp(n):
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except Exception:
        pass


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def even_odd(n):
    try:
        n = int(n)
        return render_template('6-number_odd_or_even.html', n=n)
    except Exception:
        return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
