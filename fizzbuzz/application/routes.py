from flask import Flask, response, jsonify, url_for
import json
from flask import json
import sys
from flask import jsonify

app = Flask(__name__)

@app.route('/number/<input>', methods=['GET', 'POST'])
def fizzBuzz(input):
    fizBuzz = ''
    try:
        input = int(float(input))
    except ValueError:
        return "Value error: please enter a number"
    if input % 3 == 0 and input % 5 == 0:
        fizzBuzz = 'fizz buzz'
    elif input % 3 == 0:
        fizzBuzz = 'fizz'
    elif input % 5 == 0:
        fizzBuzz = 'buzz'
    else:
        return input
    return fizzBuzz
#json object will be passed back so need to work with that