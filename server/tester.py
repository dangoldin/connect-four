#! /usr/bin/env python3

import requests

wins = {1: 0, 2: 0}
for i in range(10):
    player1_url = 'http%3A%2F%2Flocalhost%3A8091%2Fmove-jlima'
    player2_url = 'http%3A%2F%2Flocalhost%3A8091%2Fmove'

    r = requests.get('http://localhost:8090/game?player1_url='+player1_url+'&player2_url='+player2_url)

    winner = r.json()['winner']
    wins[winner] += 1

print(wins)
