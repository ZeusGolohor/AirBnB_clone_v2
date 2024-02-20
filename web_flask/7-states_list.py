#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

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
        pass


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    for state in states:
        del state._sa_instance_state
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_ses(self):
    """
    A method to tear down a sesssion.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
