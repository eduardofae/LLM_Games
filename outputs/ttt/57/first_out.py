import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1

    def play(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = self.player
            self.player *= -1

    def check_winner(self):
        for i in range(3):
            # Check rows
            if np.all(self.board[i, :] == self.player):
                return self.player
            # Check columns
            if np.all(self.board[:, i] == self.player):
                return self.player
        # Check diagonals
        if np.all(np.diagonal(self.board) == self.player):
            return self.player
        if np.all(np.flip(np.diagonal(self.board), axis=0) == self.player):
            return self.player
        # Check draw
        if np.all(self.board != 0):
            return 0
        return None

    def __str__(self):
        return "\n".join([" ".join([str(x) for x in row]) for row in self.board])

if __name__ == "__main__":
    game = Jdv()
    while True:
        print(game)
        row, col = map(int, input("Enter row and column: ").split())
        game.play(row, col)
        winner = game.check_winner()
        if winner is not None:
            if winner == 0:
                print("Draw!")
            else:
                print(f"Player {winner} wins!")
            break
