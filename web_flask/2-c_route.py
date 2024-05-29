#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displays 'C' followed by the value of the text variable."""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
