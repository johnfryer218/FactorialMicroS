from flask import Flask, response, jsonify, url_for
import json
from flask import json
import sys
from flask import jsonify

app = Flask(__name__)

@app.route('/number/<input>', METHODS=['GET', 'POST'])

def factorial(n):
    try:
        n = int(float(input("Enter a non-negative integer: ")))
        if n < 0:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)