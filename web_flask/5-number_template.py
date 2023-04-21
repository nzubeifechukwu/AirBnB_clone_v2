#!/usr/bin/python3
'''Start a Flask web application listening on 0.0.0.0, port 5000
'''
from flask import Flask, render_template

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


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    '''Display some variable text at the given route
    '''
    new_text = ''
    for c in text:
        if c != '_':
            new_text = new_text + c
        else:
            new_text = new_text + ' '
    return 'C {}'.format(new_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text='is cool'):
    '''Display some variable text at the given route
    '''
    new_text = ''
    for c in text:
        if c == '_':
            new_text = new_text + ' '
        else:
            new_text = new_text + c
    return 'Python {}'.format(new_text)


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    '''Display that `n` is a number if that is true
    '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_template(n):
    '''Render a template if n is an integer
    '''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
