import numpy as np

class Board:
    def __init__(self):
        self.game_board = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def print_board(self):
        for row in self.game_board:
            print(' '.join(row))

    def get_player_move(self):
        while True:
            try:
                row, col = map(int, input("Enter row and column (1-3): ").split())
                if not (1 <= row <= 3 and 1 <= col <= 3 and self.game_board[row - 1, col - 1] == ' '):
                    print("Invalid move. Try again.")
                    continue
                return row - 1, col - 1
            except ValueError:
                print("Invalid input. Try again.")

    def check_winner(self):
        # Check rows
        for row in self.game_board:
            if np.all(row == row[0]) and row[0] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if np.all(self.game_board[:, col] == self.game_board[0, col]) and self.game_board[0, col] != ' ':
                return self.game_board[0, col]

        # Check diagonals
        if np.all(self.game_board.diagonal() == self.game_board[0, 0]) and self.game_board[0, 0] != ' ':
            return self.game_board[0, 0]
        if np.all(np.flip(self.game_board).diagonal() == self.game_board[0, 2]) and self.game_board[0, 2] != ' ':
            return self.game_board[0, 2]

        # No winner yet
