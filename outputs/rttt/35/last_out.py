import numpy as np

class Jdv:
    def __init__(self):
        self.grid = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.symbols = ["X", "O"]

    def play(self):
        while True:
            self.display_grid()

            # Get the player's move
            move = input(f"Player {self.current_player}, enter your move (row, column): ")
            try:
                row, column = map(int, move.split(","))
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")
                continue

            # Check if the move is valid
            if not self.is_valid_move(row, column):
                print("Invalid move. Please try again.")
                continue

            # Place the player's piece on the grid
            self.grid[row, column] = self.current_player

            # Check if the player has won
            if self.check_win():
                self.display_grid()
                print(f"Player {self.current_player} wins!")
                return

            # Check if the game is a draw
            if np.all(self.grid != 0):
                self.display_grid()
                print("Draw!")
                return

            # Switch to the other player
            self.current_player = 3 - self.current_player

    def is_valid_move(self, row, column):
        return self.grid[row, column] == 0

    def check_win(self):
        # Check for a win in each row
        for row in range(3):
            if np.all(self.grid[row, :] == self.current_player):
                return True

        # Check for a win in each column
        for column in range(3):
            if np.all(self.grid[:, column] == self.current_player):
                return True

        # Check for a win in each diagonal
        if np.all(np.diag(self.grid) == self.current_player) or np.all(np.diag(np.flip(self.grid)) == self.current_player):
            return True

        # No win found
        return False

    def display_grid(self):
        print("--------")
        for row in range(3):
            for column in range(3):
                print(f"| {self.symbols[self.grid[row, column] - 1]} ", end="")
            print("|")
        print("--------")

if __name__ == "__main__":
    game = Jdv()
    game.play()
