#!/usr/bin/python3
"With Flask web application, display route for 'Hello HBNB'"
"Other route for display 'HBNB'"
"Other route for display 'C + text', then other route for 'python + text'"
"Other route for determines whether the written text is a number"
"Other route for display in h1 a number based on what the user writes in URL"

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C %s" % text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python %s" % text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return "%d is a number" % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
