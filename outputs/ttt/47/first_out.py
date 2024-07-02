import numpy as np

def jdv():
  """
  Plays a game of JDV.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create a 3x3 grid.
  grid = np.zeros((3, 3), dtype=int)

  # Set the current player to 1.
  player = 1

  # Loop until the game is over.
  while True:
    # Get the player's move.
    row, col = map(int, input("Player {}'s move (row, col): ".format(player)).split())

    # Check if the move is valid.
    if grid[row, col] != 0:
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the grid.
    grid[row, col] = player

    # Check if the player has won.
    if check_win(grid, player):
      print("Player {} wins!".format(player))
      return player

    # Check if the game is a draw.
    if np.all(grid != 0):
      print("Draw!")
      return None

    # Switch to the other player.
    player = 3 - player

def check_win(grid, player):
  """
  Checks if the player has won the game.

  Args:
    grid: The game grid.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a horizontal win.
  for row in range(3):
    if np.all(grid[row, :] == player):
      return True

  # Check for a vertical win.
  for col in range(3):
    if np.all(grid[:, col] == player):
      return True

  # Check for a diagonal win.
  if np.all(np.diagonal(grid) == player):
    return True

  if np.all(np.flipud(grid).diagonal() == player):
    return True

  # No win found.
  return False

if __name__ == "__main__":
  jdv()
