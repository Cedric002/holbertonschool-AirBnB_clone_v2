#!/usr/bin/python3
"With Flask web application, display route for HBNB web static"

from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def display_html():
    "display State, Amenity and City"
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    cities = storage.all(City).values()
    return render_template(
        "10-hbnb_filters.html", states=states, amenities=amenities, cities=cities)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
