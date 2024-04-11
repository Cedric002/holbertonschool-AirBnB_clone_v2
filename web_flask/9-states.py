#!/usr/bin/python3
"With Flask web application, display route for 'states'"

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def state(id):
    state = storage.get("State", id)
    if state is None:
        return render_template('404.html'), 404
    return render_template('9-state.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)