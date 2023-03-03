import os
import random
import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/dog')
def get_random_dog():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
