import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.player = 1

    def move(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = self.player
            self.player *= -1  # Switch player

    def check_winner(self):
        for i in range(3):
            # Check rows
            if np.all(self.board[i, :] == self.player):
                return self.player

            # Check columns
            if np.all(self.board[:, i] == self.player):
                return self.player

        # Check diagonals
        if np.all(self.board.diagonal() == self.player) or np.all(np.flip(self.board).diagonal() == self.player):
            return self.player

        # Check for draw
        if np.all(self.board != 0):
            return 0

        return None

    def play(self):
        while True:
            # Get player move
            row, col = map(int, input("Enter row and column (0-2): ").split())

            # Make move
            self.move(row, col)

            # Check for winner or draw
            winner = self.check_winner()
            if winner is not None:
                if winner == 0:
                    print("Draw")
                else:
                    print(f"Player {winner} wins")
                break

            # Print board
            print(self.board)


if __name__ == "__main__":
    jdv = Jdv()
    jdv.play()
