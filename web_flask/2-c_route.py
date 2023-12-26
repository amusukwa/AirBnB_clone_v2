#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

def home():
    """
    Route handler for the home page.

    Returns:
        str: Greeting message for the home page.
    """
    return 'Hello HBNB!'

def hbnb():
    """
    Route handler for /hbnb.

    Returns:
        str: Message indicating HBNB.
    """
    return 'HBNB'

def c_route(text):
    """
    Route handler for /c/<text>.

    Args:
        text (str): The text variable.

    Returns:
        str: Message displaying "C " followed by the value of the text variable.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
