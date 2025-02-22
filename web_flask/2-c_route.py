#!/usr/bin/python3
'''Start a Flask web application listening on 0.0.0.0, port 5000
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Display some text at the given route
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display some text at the give route
    '''
    return 'HBNB'


@app.route('/c/<text>')
def show_text(text):
    '''Display some variable text at the given route
    '''
    new_text = ''
    for c in text:
        if c != '_':
            new_text = new_text + c
        else:
            new_text = new_text + ' '
    return 'C {}'.format(new_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
