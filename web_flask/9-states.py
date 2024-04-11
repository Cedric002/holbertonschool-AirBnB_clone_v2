#!/usr/bin/python3
"With Flask web application, display route for 'cities_by_states'"

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/cities_by_states')
def cities_by_states():
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>')
def state_cities(id):
    state = storage.get('State', id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', state=None)

@app.teardown_appcontext
def remove_session(exception=None):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)