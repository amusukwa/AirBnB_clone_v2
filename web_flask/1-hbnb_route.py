#!/usr/bin/python3
"""
This module defines a simple Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Route for the home page.
    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route for /hbnb.
    Returns:
        str: A message indicating HBNB.
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
