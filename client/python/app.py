#! /usr/bin/env python3

from flask import Flask
from flask import request
from flask import jsonify

import random

app = Flask(__name__)

@app.route("/move", methods=['POST'])
def move():
    content = request.get_json()
    board = content['board']
    player = content['player']
    available_columns = content['available_columns']
    return jsonify({
        'column': random.choice(available_columns),
    })

app.run(host='0.0.0.0', port=8091, debug=True)
