from flask import Flask
from flask import render_template, request, jsonify
import re


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    app.debug = True
    app.run()