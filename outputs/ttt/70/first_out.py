import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1
        self.winner = 0

    def play(self, x, y):
        if self.winner != 0:
            print("Game over!")
            return

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Invalid move.")
            return

        if self.board[x, y] != 0:
            print("Space already occupied.")
            return

        self.board[x, y] = self.player

        if self._check_winner():
            self.winner = self.player
            print(f"Player {self.player} wins!")
        else:
            self.player = 3 - self.player

    def _check_winner(self):
        # Check rows
        for i in range(3):
            if np.all(self.board[i, :] == self.player):
                return True

        # Check columns
        for j in range(3):
            if np.all(self.board[:, j] == self.player):
                return True

        # Check diagonals
        if np.all(self.board.diagonal() == self.player):
            return True
        if np.all(np.flip(self.board).diagonal() == self.player):
            return True

        # Check if there are no more free spaces
        if np.all(self.board != 0):
            print("Draw!")
            return True

        return False


if __name__ == "__main__":
    jdv = Jdv()

    while jdv.winner == 0:
        x = int(input("Player 1, enter the x coordinate: "))
        y = int(input("Player 1, enter the y coordinate: "))
        jdv.play(x, y)

        if jdv.winner == 0:
            x = int(input("Player 2, enter the x coordinate: "))
            y = int(input("Player 2, enter the y coordinate: "))
            jdv.play(x, y)
