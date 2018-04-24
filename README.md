# connect-four

Framework to run a Connect 4 competition.

Folder structure:
- server: This is a server application that runs a Connect4 game via the /game endpoint which takes two urls (player1_url and player2_url) and hits each one for a move until there's a winner or tie.
- client: There's a python and JavaScript example here to implement the /move function which takes in the board state, the player, and the list of available move columns and responds with the column to move.
- ui: This is a way to visualize a game. It works by hitting the server's /game endpoint directly and plotting the results.

Getting started:

```sh
~ git clone https://github.com/dangoldin/connect-four.git
~ cd connect-four

# May want to run inside a virtualenv if you're comfortable with it
~ pip install -r requirements.txt

# Running the server
~ cd server
~ python app.py

# Running the python client
~ cd client/python
~ python app.py

# Running the JavaScript client
~ cd client/js
~ npm install
~ node app.js

# Running the UI
~ cd ui
~ yarn start
```

To test that everything works run each of the above in a separate tab and then test by running the following:

```sh
~ curl http://localhost:8090/game\?player1_url\=http://localhost:8091/move\&player2_url\=http://localhost:3000/move
```
