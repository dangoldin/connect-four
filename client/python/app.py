#! /usr/bin/env python3

from flask import Flask
from flask import request
from flask import jsonify

import random

from copy import deepcopy

app = Flask(__name__)

from connect4 import Connect4

def transform_board(board):
    height = len(board)
    width  = len(board[0])

    new_board = [[0 for x in range(height)] for y in range(width)]
    for i in range(width):
        for j in range(height):
            new_board[i][j] = board[height - j - 1][i]

    return new_board

@app.route("/move-random", methods=['POST'])
def move_random():
    content = request.get_json()
    board = content['board']
    player = content['player']
    other_player = 2 if player == 1 else 1
    available_columns = content['available_columns']

    return jsonify({
        'column': random.choice(available_columns),
    })

@app.route("/move-first", methods=['POST'])
def move_first():
    content = request.get_json()
    board = content['board']
    player = content['player']
    other_player = 2 if player == 1 else 1
    available_columns = content['available_columns']

    return jsonify({
        'column': available_columns[0],
    })

@app.route("/move", methods=['POST'])
def move():
    content = request.get_json()
    board = content['board']
    player = content['player']
    other_player = 2 if player == 1 else 1
    available_columns = content['available_columns']

    # Check for win
    for avail_col in available_columns:
        new_board = transform_board(board)
        b = Connect4()
        b.set_board(new_board)
        b.move(avail_col, player)
        if b.winner(player):
            return jsonify({
                'column': avail_col,
            })

    # Block opponent
    for avail_col in available_columns:
        new_board = transform_board(board)
        b = Connect4()
        b.set_board(new_board)
        b.move(avail_col, other_player)
        if b.winner(other_player):
            return jsonify({
                'column': avail_col,
            })

    # Block opponent + 1
    bad_cols = set()
    for avail_col in available_columns:
        new_board = transform_board(board)
        b = Connect4()
        for opp_avail_col in b.get_available_columns():
            b.set_board(deepcopy(new_board))
            b.move(avail_col, player)
            b.move(opp_avail_col, other_player)

            if b.winner(other_player):
                bad_cols.add(avail_col)

    # First column that won't let other player win
    non_winning_avail_columns = [a for a in available_columns if a not in bad_cols]

    if len(non_winning_avail_columns) > 0:
        return jsonify({
            'column': non_winning_avail_columns[0],
        })

    # Losing is better than crashing
    return jsonify({
            'column': available_columns[0],
        })

def near_win(board, player, available_columns, done=False):
    height, width = len(board), len(board[0])
    board = list(reversed(board))
    for i in range(width):
        for j in range(height - 3):
            if (board[j][i] == player
                    and board[j+1][i] == player
                    and board[j+2][i] == player):
                if i in available_columns:
                    return i

    for i in range(width - 3):
        for j in range(height):
            if (board[j][i] == player and
                    board[j][i+1] == player and
                    board[j][i+2] == player):
                if i+3 in available_columns:
                    return i+3

    for i in range(width - 3):
        for j in range(height - 3):
            if (board[j][width - i - 1] == player and
                    board[j+1][width - i - 2] == player and
                    board[j+2][width - i - 3] == player and
                    board[j+2][width - i - 4] != 0):
                if width-i-4 in available_columns:
                    return width-i-4

    for i in range(width - 3):
        for j in range(height - 3):
            if (board[j][i] == player and
                    board[j+1][i+1] == player and
                    board[j+2][i+2] == player and
                    board[j+2][i+3] != 0):
                if i+3 in available_columns:
                    return i+3
    if done:
        return random.choice(available_columns)
    else:
        return near_win(board, 3-player, available_columns, done=True)

@app.route("/move-jlima", methods=['POST'])
def move_jlima():
    content = request.get_json()
    board = content['board']
    player = content['player']
    available_columns = content['available_columns']

    return jsonify({
        'column': near_win(board, player, available_columns)
    })

app.run(host='0.0.0.0', port=8091, debug=True)
