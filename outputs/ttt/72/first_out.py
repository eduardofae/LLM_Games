import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.player = 1  # 1 for player 1, 2 for player 2
        self.winner = None

    def play(self, row, col):
        if self.board[row, col] == 0 and self.winner is None:
            self.board[row, col] = self.player
            self.check_winner()
            self.player = 3 - self.player  # Switch player

    def check_winner(self):
        # Check rows
        for i in range(3):
            if np.all(self.board[i, :] == self.player):
                self.winner = self.player
                return

        # Check columns
        for j in range(3):
            if np.all(self.board[:, j] == self.player):
                self.winner = self.player
                return

        # Check diagonals
        if np.all(self.board.diagonal() == self.player):
            self.winner = self.player
            return

        if np.all(np.flipud(self.board).diagonal() == self.player):
            self.winner = self.player
            return

        # Check draw
        if np.all(self.board != 0):
            self.winner = 0

    def print_board(self):
        for row in self.board:
            print(" | ".join(["." if x == 0 else "X" if x == 1 else "O" for x in row]))
            print("-" * 7)

    def is_finished(self):
        return self.winner is not None

    def get_winner(self):
        return self.winner


if __name__ == "__main__":
    game = Jdv()

    while not game.is_finished():
        game.print_board()
        row, col = map(int, input("Player {}: Enter row and column (e.g. 0 1): ".format(game.player)).split())
        game.play(row, col)

    game.print_board()

    winner = game.get_winner()
    if winner == 0:
        print("Draw!")
    else:
        print("Player {} wins!".format(winner))
