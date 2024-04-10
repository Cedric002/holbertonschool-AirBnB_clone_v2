#!/usr/bin/python3
"With Flask web application, display route for 'Hello HBNB'"
"Other route for display 'HBNB'"
"Other route for display 'C + text', then other route for 'python + text'"

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

