#!/usr/bin/python3
from flask import Flask

"With Flask web application, display route for 'Hello HBNB'"


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
