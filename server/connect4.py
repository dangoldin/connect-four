#! /usr/bin/env python3

class Connect4:
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height

        self.board = [['0' for x in range(height)] for y in range(width)]

    def column_full(self, column):
        return all(val != '0' for val in self.board[column])

    def move(self, column, player):
        if self.column_full(column):
            return False
        else:
            self.board[column][self.board[column].index('0')] = player
            return True

    def get_available_columns(self):
        return [col for col in range(self.width) if not self.column_full(col)]

    def winner(self, player):
        # Horizontal
        for i in range(self.height - 3):
            for j in range(self.width - 3):
                if self.board[j][i] == player and \
                    self.board[j+1][i] == player and \
                    self.board[j+2][i] == player and \
                    self.board[j+3][i] == player:
                    return True

        # Vertical
        for i in range(self.height - 3):
            for j in range(self.width - 3):
                if self.board[j][i] == player and \
                    self.board[j][i+1] == player and \
                    self.board[j][i+2] == player and \
                    self.board[j][i+3] == player:
                    return True

        # /
        for i in range(self.height - 3):
            for j in range(self.width - 3):
                if self.board[j][self.height - i - 1] == player and \
                    self.board[j+1][self.height - i - 2] == player and \
                    self.board[j+2][self.height - i - 3] == player and \
                    self.board[j+3][self.height - i - 4] == player:
                    return True

        # \
        for i in range(self.height - 3):
            for j in range(self.width - 3):
                if self.board[j][i] == player and \
                    self.board[j+1][i+1] == player and \
                    self.board[j+2][i+2] == player and \
                    self.board[j+3][i+3] == player:
                    return True

        return False

    def get_board_state(self):
        # Normalize the board state to make it easier to read
        s = [['0' for x in range(self.width)] for y in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                s[i][j] = self.board[j][self.height - i - 1]
        return s

    def __str__(self):
        s = ''
        for i in range(self.height):
            for j in range(self.width):
                s += self.board[j][self.height - i - 1] + ' '
            s += "\n"
        return s
