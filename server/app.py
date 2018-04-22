#! /usr/bin/env python3

from flask import Flask
from flask import request
from flask import jsonify

from connect4 import Connect4

import requests

app = Flask(__name__)

@app.route("/game", methods=['GET'])
def run_game():
    player1_url = request.args.get('player1_url')
    player2_url = request.args.get('player2_url')
    print (player1_url, 'vs', player2_url)

    b = Connect4()

    moves = []
    while True:
        p1_response = requests.post(
            url=player1_url,
            json={
                'board': b.get_board_state(),
                'player': 1,
                'available_columns': b.get_available_columns(),
                })
        p1_column = p1_response.json()['column']
        moves.append({'player': 1, 'column': p1_column})
        b.move(p1_column, 1)
        if b.winner(1):
            print('Player 1 wins')
            print(str(b))
            return jsonify({
                'winner': 1,
                'moves': moves,
            })

        p2_response = requests.post(
            url=player2_url,
            json={
                'board': b.get_board_state(),
                'player': 2,
                'available_columns': b.get_available_columns(),
                })
        p2_column = p2_response.json()['column']
        moves.append({'player': 2, 'column': p2_column})
        b.move(p2_column, 2)
        if b.winner(2):
            print('Player 2 wins')
            print(str(b))
            return jsonify({
                'winner': 2,
                'moves': moves,
            })

app.run(host='0.0.0.0', port=8090, debug=True)

# curl http://localhost:8090/game\?player1_url\=http://localhost:8091/move\&player2_url\=http://localhost:8091/move
