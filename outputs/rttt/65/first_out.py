import numpy as np

def jdv():
  """
  Plays a game of jdv.

  The game is played on a 3x3 grid, and two players take turns placing their pieces in free spaces.
  The first player to make a line of three adjacent pieces wins.
  If there are no more free spaces, the game is declared a draw.

  Args:
    None

  Returns:
    None
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3), dtype=int)

  # Set the current player to 1
  current_player = 1

  # Loop until the game is over
  while True:
    # Print the grid
    print(grid)

    # Get the player's move
    move = input(f"Player {current_player}, enter your move (row, column): ")

    # Convert the move to a row and column
    row, column = map(int, move.split(","))

    # Check if the move is valid
    if grid[row, column] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the grid
    grid[row, column] = current_player

    # Check if the player has won
    if check_win(grid, current_player):
      print(f"Player {current_player} wins!")
      break

    # Check if the game is a draw
    if np.all(grid != 0):
      print("Draw!")
      break

    # Switch to the other player
    current_player = 3 - current_player

def check_win(grid, player):
  """
  Checks if a player has won.

  Args:
    grid: A 3x3 grid.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row
  for row in range(3):
    if np.all(grid[row, :] == player):
      return True

  # Check for a win in each column
  for column in range(3):
    if np.all(grid[:, column] == player):
      return True

  # Check for a win in each diagonal
  if np.all(grid.diagonal() == player):
    return True
  if np.all(np.flip(grid).diagonal() == player):
    return True

  # No win found
  return False

if __name__ == "__main__":
  jdv()
