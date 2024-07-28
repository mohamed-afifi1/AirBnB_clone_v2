#!/usr/bin/python3
"""
hello in flask app
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Return a friendly greeting."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Return a friendly greeting for HBNB."""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """return c and text given in route"""
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_is(text="is cool"):
    """return python and text given in route"""
    text = text.replace('_', ' ')
    return 'Python ' + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
