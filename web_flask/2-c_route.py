#!/usr/bin/python3
"""
This module defines a simple Flask web application.
"""
from flask import Flask

app = Flask(__name__)

# Route for the home page


@app.route('/', strict_slashes=False)
def home():
    """
    Route handler for the home page.

    Returns:
        str: Greeting message for the home page.
    """
    return 'Hello HBNB!'

# Route for /hbnb


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for /hbnb.

    Returns:
        str: Message indicating HBNB.
    """
    return 'HBNB'


# Route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route handler for /c/<text>.

    Args:
        text (str): The text variable.

    Returns:
        str:displays "C " followed by the value of the text variable.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
