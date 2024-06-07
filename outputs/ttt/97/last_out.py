import numpy as np

class JdvGame:
  """
  This class implements the game jdv in Python.

  Players take turns placing their pieces on a 3x3 grid. The first player to get three of their pieces in a row, column, or diagonal wins.
  """

  def __init__(self):
    """
    Initializes a new game of jdv.
    """

    # Create a 3x3 grid
    self.grid = np.zeros((3, 3))

    # Initialize the current player
    self.current_player = 'X'

    # Initialize the game status
    self.game_over = False
    self.winner = None

  def play(self):
    """
    Starts the game loop.
    """

    while not self.game_over:
      # Get the player's move
      row, col = map(int, input(f"{self.current_player}'s turn: Enter row and column (0-2): ").split())

      # Check if the move is valid
      if not self._is_valid_move(row, col):
        print("Invalid move!")
        continue

      # Place the player's piece in the grid
      self.grid[row, col] = self.current_player

      # Check if the player has won
      if self._check_win():
        self.game_over = True
        self.winner = self.current_player

      # Switch the current player
      self.current_player = 'X' if self.current_player == 'O' else 'O'

    # Print the game over message
    if self.winner is not None:
      print(f"{self.winner} wins!")
    else:
      print("Draw!")

  def _is_valid_move(self, row, col):
    """
    Checks if a move is valid.

    Args:
      row: The row of the move.
      col: The column of the move.

    Returns:
      True if the move is valid, False otherwise.
    """

    # Check if the grid is the correct size
    if not self.grid.shape == (3, 3):
      raise ValueError("Grid must be a 3x3 numpy array.")

    return 0 <= row <= 2 and 0 <= col <= 2 and self.grid[row, col] == 0

  def _check_win(self):
    """
    Checks if a player has won.

    Returns:
      True if a player has won, False otherwise.
    """

    # Check rows
    for row in self.grid:
      if np.all(row == row[0]) and row[0] != 0:
        return True

    # Check columns
    for col in self.grid.T:
      if np.all(col == col[0]) and col[0] != 0:
        return True

    # Check diagonals
    if np.all(np.diag(self.grid) == np.diag(self.grid)[0]) and np.diag(self.grid)[0] != 0:
      return True

    if np.all(np.diag(np.flipud(self.grid)) == np.diag(np.flipud(self.grid))[0]) and np.diag(np.flipud(self.grid))[0] != 0:
      return True

    # If there is no winner, return False
    return False


if __name__ == "__main__":
  game = JdvGame()
  game.play()
