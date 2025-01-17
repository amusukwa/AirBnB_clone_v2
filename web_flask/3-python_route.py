#!/usr/bin/python3
"""
This module defines a Flask web application with specified routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Route handler for the home page.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for /hbnb.

    Returns:
        str: Message indicating HBNB.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route handler for /c/<text>.

    Args:
        text (str): The text variable.

    Returns:
        str: displays "C " followed by the value of the text variable.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Route handler for /python/<text> with a default value of "is cool".

    Args:
        text (str): The text variable.

    Returns:
        str:displays "Python " followed by the value of the text variable.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
