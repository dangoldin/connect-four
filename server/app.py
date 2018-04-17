#! /usr/bin/env python3

from flask import Flask
from flask import request

from connect4 import Connect4

import requests

app = Flask(__name__)

@app.route("/game", methods=['GET'])
def run_game():
    player1_url = request.args.get('player1_url')
    player2_url = request.args.get('player2_url')
    print (player1_url, 'vs', player2_url)

    b = Connect4()

    while True:
        # TODO: Actually fill this out with real payload
        p1_column = requests.get(player1_url)
        b.move(p1_column, '1')
        if b.winner('1'):
            print('Player 1 wins')
            print(b.toString())
            return True

        p2_column = requests.get(player2_url)
        b.move(p2_column, '2')
        if b.winner('2'):
            print('Player 2 wins')
            print(b.toString())
            return True

app.run(host='0.0.0.0', port=8090, debug=True)

# curl http://localhost:8090/game\?player1_url\=dasdsa\&player2_url\=dasdsadas