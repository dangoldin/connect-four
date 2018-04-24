import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      player1Url: 'http://localhost:8091/move',
      player2Url: 'http://localhost:3001/move',
      player1: 1,
      player2: 2,
      currentPlayer: null,
      board: [],
      gameOver: false,
      message: '',
      stepSize: 500
    };

    this.play = this.play.bind(this);
    this.handlePlayer1UrlChange = this.handlePlayer1UrlChange.bind(this);
    this.handlePlayer2UrlChange = this.handlePlayer2UrlChange.bind(this);
    this.handleStepSizeChange = this.handleStepSizeChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handlePlayer1UrlChange(event) {
    this.setState({player1Url: event.target.value});
  }

  handlePlayer2UrlChange(event) {
    this.setState({player2Url: event.target.value});
  }

  handleStepSizeChange(event) {
    this.setState({stepSize: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    this.initBoard();
    this.playAutomatedGame();
  }

  // Starts new game
  initBoard() {
    // Create a blank 6x7 matrix
    let board = [];
    for (let r = 0; r < 6; r++) {
      let row = [];
      for (let c = 0; c < 7; c++) { row.push(null) }
      board.push(row);
    }

    this.setState({
      board,
      currentPlayer: this.state.player1,
      gameOver: false,
      message: ''
    });
  }

  togglePlayer() {
    return (this.state.currentPlayer === this.state.player1) ? this.state.player2 : this.state.player1;
  }

  playAutomatedGame() {
    const player1url = encodeURIComponent(this.state.player1Url);
    const player2url = encodeURIComponent(this.state.player2Url);
    const stepSize = this.state.stepSize;

    fetch("http://localhost:8090/game?player1_url=" + player1url+"&player2_url=" + player2url)
    .then(res => res.json())
    .then(
      (result) => {
        let play = this.play;
        let timer = 0;
        for (let m of result['moves']) {
          setTimeout(function(){
            play(m['column']);
          }, timer);
          timer += stepSize;
        }
      },
      (error) => {
        this.setState({
          message: 'Failed to fetch moves'
        });
      }
    )
  }

  play(c) {
    if (!this.state.gameOver) {
      // Place piece on board
      let board = this.state.board;
      for (let r = 5; r >= 0; r--) {
        if (!board[r][c]) {
          board[r][c] = this.state.currentPlayer;
          break;
        }
      }

      // Check status of board
      let result = this.checkAll(board);
      if (result === this.state.player1) {
        this.setState({ board, gameOver: true, message: 'Player 1 (red) wins!' });
      } else if (result === this.state.player2) {
        this.setState({ board, gameOver: true, message: 'Player 2 (yellow) wins!' });
      } else if (result === 'draw') {
        this.setState({ board, gameOver: true, message: 'Draw game.' });
      } else {
        this.setState({ board, currentPlayer: this.togglePlayer() });
      }
    } else {
      this.setState({ message: 'Game over. Please start a new game.' });
    }
  }

  checkVertical(board) {
    // Check only if row is 3 or greater
    for (let r = 3; r < 6; r++) {
      for (let c = 0; c < 7; c++) {
        if (board[r][c]) {
          if (board[r][c] === board[r - 1][c] &&
              board[r][c] === board[r - 2][c] &&
              board[r][c] === board[r - 3][c]) {
            return board[r][c];
          }
        }
      }
    }
  }

  checkHorizontal(board) {
    // Check only if column is 3 or less
    for (let r = 0; r < 6; r++) {
      for (let c = 0; c < 4; c++) {
        if (board[r][c]) {
          if (board[r][c] === board[r][c + 1] &&
              board[r][c] === board[r][c + 2] &&
              board[r][c] === board[r][c + 3]) {
            return board[r][c];
          }
        }
      }
    }
  }

  checkDiagonalRight(board) {
    // Check only if row is 3 or greater AND column is 3 or less
    for (let r = 3; r < 6; r++) {
      for (let c = 0; c < 4; c++) {
        if (board[r][c]) {
          if (board[r][c] === board[r - 1][c + 1] &&
              board[r][c] === board[r - 2][c + 2] &&
              board[r][c] === board[r - 3][c + 3]) {
            return board[r][c];
          }
        }
      }
    }
  }

  checkDiagonalLeft(board) {
    // Check only if row is 3 or greater AND column is 3 or greater
    for (let r = 3; r < 6; r++) {
      for (let c = 3; c < 7; c++) {
        if (board[r][c]) {
          if (board[r][c] === board[r - 1][c - 1] &&
              board[r][c] === board[r - 2][c - 2] &&
              board[r][c] === board[r - 3][c - 3]) {
            return board[r][c];
          }
        }
      }
    }
  }

  checkDraw(board) {
    for (let r = 0; r < 6; r++) {
      for (let c = 0; c < 7; c++) {
        if (board[r][c] === null) {
          return null;
        }
      }
    }
    return 'draw';
  }

  checkAll(board) {
    return this.checkVertical(board) || this.checkDiagonalRight(board) || this.checkDiagonalLeft(board) || this.checkHorizontal(board) || this.checkDraw(board);
  }

  componentWillMount() {
    this.initBoard();
  }

  componentDidMount() {
    // this.playAutomatedGame();
  }

  render() {
    return (
      <div className="App">
        <form onSubmit={this.handleSubmit}>
          <div>
            <input placeholder="player 1 url" className="playerEntry" type="text" value={this.state.player1Url} onChange={this.handlePlayer1UrlChange} />
          </div>
          <div>
            <input placeholder="player 2 url" className="playerEntry" type="text" value={this.state.player2Url} onChange={this.handlePlayer2UrlChange} />
          </div>
          <div>
            <input placeholder="speed" className="playerEntry" type="text" value={this.state.stepSize} onChange={this.handleStepSizeChange} />
          </div>

          {/* <div className="button" onClick={() => {this.initBoard(); this.playAutomatedGame();}}>
            New Game
          </div> */}
          <input type="submit" value="Go" />
        </form>

        <table>
          <thead>
          </thead>
          <tbody>
            {this.state.board.map((row, i) => (<Row key={i} row={row} play={this.play} />))}
          </tbody>
        </table>

        <p className="message">{this.state.message}</p>
      </div>
    );
  }
}

const Row = ({ row, play }) => {
  return (
    <tr>
      {row.map((cell, i) => <Cell key={i} value={cell} columnIndex={i} play={play} />)}
    </tr>
  );
};

const Cell = ({ value, columnIndex, play }) => {
  let color = 'white';
  if (value === 1) {
    color = 'red';
  } else if (value === 2) {
    color = 'yellow';
  }

  return (
    <td>
      <div className="cell" onClick={() => {play(columnIndex)}}>
        <div className={color}></div>
      </div>
    </td>
  );
};

export default App;
