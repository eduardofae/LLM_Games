import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1

    def play(self, x, y):
        if self.board[x, y] == 0:
            self.board[x, y] = self.player
            self.player *= -1

    def check_winner(self):
        for i in range(3):
            if np.all(self.board[i, :] == self.board[i, 0]) and self.board[i, 0] != 0:
                return self.board[i, 0]
            if np.all(self.board[:, i] == self.board[0, i]) and self.board[0, i] != 0:
                return self.board[0, i]

        if np.all(self.board.diagonal() == self.board[0, 0]) and self.board[0, 0] != 0:
            return self.board[0, 0]

        if np.all(np.flip(self.board).diagonal() == self.board[0, 2]) and self.board[0, 2] != 0:
            return self.board[0, 2]

        if np.all(self.board != 0):
            return 0

        return None

    def __str__(self):
        return "\n".join([" ".join([str(x) for x in row]) for row in self.board])

if __name__ == "__main__":
    game = Jdv()
    while True:
        print(game)
        x, y = map(int, input("Enter the coordinates (x, y): ").split())
        game.play(x, y)
        winner = game.check_winner()
        if winner is not None:
            if winner == 0:
                print("Draw!")
            else:
                print("Player", winner, "wins!")
            break
