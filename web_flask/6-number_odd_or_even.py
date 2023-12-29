#!/usr/bin/python3
"""
This module defines a Flask web application with specified routes.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Route handler for the home page.

    Returns:
        str: Greeting message for the home page.
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
        str: displaying "C " followed by the value of the text variable.
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
        str: displays "Python " followed by the value of the text variable.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route to display "n is a number" only if n is an integer.

    Args:
        n (int): The number.

    Returns:
        str: Message indicating whether n is a number.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    Route for /number_template/<n> to display an HTML page with an H1 tag.

    Args:
        n (int): The number.

    Returns:
        str: Rendered HTML template.
    """
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    """
    Route for /number_odd_or_even/<n> to display page  indicating even or odd.

    Args:
        n (int): The number.

    Returns:
        str: Rendered HTML template.
    """
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', number=n, parity='even' if n % 2 == 0 else 'odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
