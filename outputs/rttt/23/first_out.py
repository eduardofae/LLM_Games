import numpy as np

class Jdv:
    def __init__(self):
        self.grid = np.zeros((3, 3), dtype=int)
        self.turn = 1  # 1 for player 1, 2 for player 2

    def play(self, row, col):
        if self.grid[row, col] == 0:
            self.grid[row, col] = self.turn
            self.check_win()
            self.turn = 3 - self.turn

    def check_win(self):
        # Check rows
        for i in range(3):
            if np.all(self.grid[i, :] == self.turn):
                self.declare_winner(self.turn)
                return

        # Check columns
        for j in range(3):
            if np.all(self.grid[:, j] == self.turn):
                self.declare_winner(self.turn)
                return

        # Check diagonals
        if np.all(self.grid.diagonal() == self.turn):
            self.declare_winner(self.turn)
            return
        if np.all(np.flipud(self.grid).diagonal() == self.turn):
            self.declare_winner(self.turn)
            return

        # Check for draw
        if np.all(self.grid != 0):
            self.declare_draw()

    def declare_winner(self, winner):
        print(f"Player {winner} wins!")

    def declare_draw(self):
        print("Draw!")

    def print_grid(self):
        print(self.grid)

if __name__ == "__main__":
    game = Jdv()

    while True:
        game.print_grid()

        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        game.play(row, col)

        if game.turn == 1:
            print("Player 1's turn")
        else:
            print("Player 2's turn")
