import numpy as np

def jdv():
  """
  Play a game of jdv.

  The game is played on a 3x3 grid. Two players take turns placing their pieces in a free space of the grid.
  The first player to make a line of 3 (horizontally, vertically, or diagonally) adjacent pieces wins the game.
  If there are no more free spaces, the game is declared a draw.

  Args:
    None

  Returns:
    None
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3), dtype=int)

  # Set the player number
  player = 1

  # Play the game
  while True:
    # Get the player's move
    move = input("Player {}'s move: ".format(player))

    # Convert the move to a row and column
    row, col = [int(x) for x in move.split(",")]

    # Check if the move is valid
    if grid[row, col] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the grid
    grid[row, col] = player

    # Check if the player has won
    if check_win(grid, player):
      print("Player {} wins!".format(player))
      break

    # Check if the game is a draw
    if np.all(grid != 0):
      print("Draw!")
      break

    # Switch the player
    player = 3 - player

def check_win(grid, player):
  """
  Check if the player has won the game.

  Args:
    grid: The game grid.
    player: The player number.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row
  for row in range(3):
    if np.all(grid[row, :] == player):
      return True

  # Check for a win in each column
  for col in range(3):
    if np.all(grid[:, col] == player):
      return True

  # Check for a win in each diagonal
  if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
    return True

  # No win
  return False

if __name__ == "__main__":
  jdv()
