#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def user():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<hello>')
def user(hello):
    return f'<h1>Profile for {hello}</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
