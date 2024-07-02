import numpy as np

class Game:
    """
    The jdv game class handles the game state, moves, and logic.
    """

    def __init__(self):
        self.grid = np.zeros((3, 3))
        self.current_player = 'X'

    def handle_move(self):
        """
        Gets the player's move, checks if it's valid, and updates the grid.
        """
        while True:
            try:
                move = input(f"{self.current_player}'s turn. Enter a row and column (e.g. 1,2): ")
                if move == 'q':
                    exit()
                row, column = map(int, move.split(','))
                if self.grid[row, column] == 0:
                    self.grid[row, column] = self.current_player
                    return
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid row and column.")

    def check_win(self, player):
        """
        Checks if the player has won.
        """
        # Check for horizontal wins
        for row in range(3):
            if np.all(self.grid[row] == player):
                return True

        # Check for vertical wins
        for column in range(3):
            if np.all(self.grid[:, column] == player):
                return True

        # Check for diagonal wins
        if np.any(np.diagonal(self.grid) == player) or np.any(np.flip(np.diagonal(self.grid)) == player):
            return True

        # No win
        return False

    def check_draw(self):
        """
        Checks if the game is a draw.
        """
        return np.all(self.grid != 0)

    def start(self):
        """
        Starts the game loop.
        """
        while True:
            self.handle_move()

            if self.check_win(self.current_player):
                print(f"{self.current_player} wins!")
                break
            elif self.check_draw():
                print("Draw!")
                break

            self.current_player = 'X' if self.current_player == 'O' else 'O'

    def display_grid(self):
        """
        Displays the current state of the grid.
        """
        for row in self.grid:
            print(' '.join([str(cell) for cell in row]))

if __name__ == "__main__":
    game = Game()
    game.display_grid()
    game.start()
