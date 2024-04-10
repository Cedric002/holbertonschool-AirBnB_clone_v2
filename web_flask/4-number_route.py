#!/usr/bin/python3

from flask import Flask

"With Flask web application, display route for 'Hello HBNB'"
"Other route for display 'HBNB'"
"Other route for display 'C + text', then other route for 'python + text'"
"Other route for determines whether the written text is a number"
"Other route for display in h1 a number based on what the user writes in URL"


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '%d is a number' % n


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
