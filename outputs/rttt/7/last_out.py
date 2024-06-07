import numpy as np

class Jdv:
    def __init__(self, grid_size=3):
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.players = ['X', 'O']
        self.current_player = self.players[0]
        self.grid_size = grid_size

    def play(self):
        while True:
            # Get the player's move
            try:
                row, col = map(int, input("Enter your move (row, col): ").split())
            except ValueError:
                print("Invalid input. Please enter two integers separated by a comma.")
                continue

            # Check if the move is valid
            if not self.is_valid_move(row, col):
                print("Invalid move. Please try again.")
                continue

            # Place the player's piece on the grid
            self.grid[row, col] = self.current_player

            # Check if the player has won
            if self.check_win(self.current_player):
                print(f"{self.current_player} wins!")
                break

            # Check if the game is a draw
            if np.all(self.grid != 0):
                print("Draw!")
                break

            # Switch to the other player
            self.current_player = self.players[1 - self.players.index(self.current_player)]

    def is_valid_move(self, row, col):
        return (0 <= row < self.grid_size and 0 <= col < self.grid_size and self.grid[row, col] == 0)

    def check_win(self, player):
        # Check if the player has won horizontally
        for i in range(self.grid_size):
            if np.all(self.grid[i, :] == player):
                return True

        # Check if the player has won vertically
        for j in range(self.grid_size):
            if np.all(self.grid[:, j] == player):
                return True

        # Check if the player has won diagonally
        if np.all(self.grid.diagonal() == player):
            return True
        if np.all(np.flip(self.grid).diagonal() == player):
            return True

        # Otherwise, the player has not won
        return False


if __name__ == "__main__":
    # Customize the grid size here (default is 3)
    grid_size = int(input("Enter the grid size (minimum 3): "))
    if grid_size < 3:
        print("Invalid grid size. Please enter a value greater than or equal to 3.")
    else:
        jdv = Jdv(grid_size)
        jdv.play()
