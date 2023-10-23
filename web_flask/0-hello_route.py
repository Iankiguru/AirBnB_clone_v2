#!/usr/bin/python3
<<<<<<< HEAD
"""
script that starts a Flask web application
"""

=======
''' starts a Flask web app '''
>>>>>>> 4e10c68ef1015c66984f502d24854df87331ab7d
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

=======
def hello_world():
    """ returns 'Hello HBNB' """
    return 'Hello HBNB!'


>>>>>>> 4e10c68ef1015c66984f502d24854df87331ab7d
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
