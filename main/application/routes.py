from flask import Flask, json, jsonify, response, jsonify, url_for, request, requests, render_template
import json
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    return render_template('index.html')

@app.route('/number', methods=['GET', 'POST'])

def number():
    formData = request.form.get ('input')
    formData = int(formData)
    fizzBuzz = requests.post(f'http//converter:5001/number/{formData}')
    factorial = requests.post(f'http://factorial:5002/number/{formData}')
    return render_template('output.html', originalInput=formData, threeFive=fizzBuzz, reversePrime=factorial)