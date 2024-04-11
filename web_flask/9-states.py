#!/usr/bin/python3
"With Flask web application, display route for 'states'"

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/cities_by_states')
def cities_by_states():
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)