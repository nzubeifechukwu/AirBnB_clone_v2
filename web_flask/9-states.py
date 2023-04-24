#!/usr/bin/python3
'''Start a Flask web application
'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/states', strict_slashes=False)
def get_states():
    '''Get all states in `states`
    '''
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_state(id):
    '''Get all cities with the same state_id as a given state id
    '''
    states = storage.all(State)
    return render_template('9-states.html', id=id, states=states)


@app.teardown_appcontext
def close_session(exception=None):
    '''Remove the current SQLAlchemy Session
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')