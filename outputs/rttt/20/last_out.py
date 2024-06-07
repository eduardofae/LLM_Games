import numpy as np
import re

# Create a game class
class JdvGame:
    """
    A class representing the Jdv game.

    Attributes:
        grid_size (int): The size of the game grid.
        grid (numpy.ndarray): A numpy array representing the game grid.
        players (list): A list of players.
        current_player (str): The current player.
        game_state (str): The current game state, can be "ongoing", "win", or "draw".
    """

    def __init__(self, grid_size=3):
        """
        Initialize a new game.

        Args:
            grid_size (int, optional): The size of the game grid. Defaults to 3.
        """
        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size))
        self.players = ['X', 'O']
        self.current_player = self.players[0]
        self.game_state = "ongoing"

    def play(self):
        """
        Play the game.
        """
        while self.game_state == "ongoing":
            # Get the player's move
            move = input(f"Player {self.current_player}, enter your move (row, column): ")

            # Validate the player's move
            if not re.match(r"^\d+,\d+$", move):
                print("Invalid move. Please enter a valid row and column.")
                continue

            row, column = map(int, move.split(','))

            if not (0 <= row < self.grid_size and 0 <= column < self.grid_size):
                print("Invalid move. Row and column must be within the grid boundaries.")
                continue

            if self.grid[row, column] != 0:
                print("Invalid move. Space is already occupied.")
                continue

            # Place the player's piece on the grid
            self.grid[row, column] = self.current_player

            # Check if the player has won
            if self.check_win(self.current_player):
                self.game_state = "win"
                print(f"Player {self.current_player} has won!")
                break

            # Check if the game is a draw
            if np.all(self.grid != 0):
                self.game_state = "draw"
                print("It's a draw!")
                break

            # Switch to the other player
            self.current_player = self.players[1 - self.players.index(self.current_player)]

    def play_move(self, row, column):
        """
        Play a move at the specified row and column.

        Args:
            row (int): The row of the move.
            column (int): The column of the move.

        Raises:
            IndexError: If the specified row or column is out of bounds.
            ValueError: If the specified space is already occupied.
        """
        if not (0 <= row < self.grid_size and 0 <= column < self.grid_size):
            raise IndexError("Invalid move. Row and column must be within the grid boundaries.")

        if self.grid[row, column] != 0:
            raise ValueError("Invalid move. Space is already occupied.")

        # Place the player's piece on the grid
        self.grid[row, column] = self.current_player

    def check_win(self, player):
        """
        Check if the specified player has won the game.

        Args:
            player (str): The player to check for a win.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        # Check the rows
        for row in range(self.grid_size):
            if np.all(self.grid[row, :] == player):
                return True

        # Check the columns
        for column in range(self.grid_size):
            if np.all(self.grid[:, column] == player):
                return True

        # Check the diagonals
        if np.all(self.grid.diagonal() == player):
            return True
        if np.all(np.flip(self.grid).diagonal() == player):
            return True

        # No winner yet
        return False

# Create a game instance and play the game
game = JdvGame()
game.play()
