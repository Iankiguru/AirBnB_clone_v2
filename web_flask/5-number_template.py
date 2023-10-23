#!/usr/bin/python3
<<<<<<< HEAD
"""
script that starts a Flask web application
"""

=======
''' starts a Flask web app '''
>>>>>>> 4e10c68ef1015c66984f502d24854df87331ab7d
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def index():
    """returns Hello HBNB!"""
=======
def hello_world():
    """ returns 'Hello HBNB' """
>>>>>>> 4e10c68ef1015c66984f502d24854df87331ab7d
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """returns HBNB"""
=======
    """ returns 'HBNB' """
>>>>>>> 4e10c68ef1015c66984f502d24854df87331ab7d
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
<<<<<<< HEAD
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')
=======
    """ displays C followed by value of text passed """
    return 'C {}'.format(text.replace('_', ' '))
>>>>>>> 4e10c68ef1015c66984f502d24854df87331ab7d


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
<<<<<<< HEAD
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

=======
def python_route(text='is cool'):
    """ displays Python followed by value of text """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ returns '<n> is a number' only if n is an integer """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' displays HTML page only if n is an integer '''
    return render_template('5-number.html', n=n)


>>>>>>> 4e10c68ef1015c66984f502d24854df87331ab7d
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
