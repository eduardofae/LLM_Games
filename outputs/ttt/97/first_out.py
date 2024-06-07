import numpy as np

def jdv():
  """
  This function implements the game jdv in Python.
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3))

  # Get the names of the players
  player1 = input("Enter player 1's name: ")
  player2 = input("Enter player 2's name: ")

  # Set the current player to player 1
  current_player = player1

  # While there are no winners and there are free spaces, keep playing
  while not check_win(grid) and not np.all(grid != 0):
    # Get the player's move
    row, col = map(int, input(f"{current_player}'s turn: Enter row and column (0-2): ").split())

    # Place the player's piece in the grid
    grid[row, col] = 1 if current_player == player1 else -1

    # Check if the player won
    if check_win(grid):
      print(f"{current_player} wins!")
      break

    # Switch the current player
    current_player = player2 if current_player == player1 else player1

  # If there are no more free spaces, declare a draw
  if np.all(grid != 0):
    print("Draw!")

def check_win(grid):
  """
  This function checks if there is a winner in the grid.

  Args:
    grid: A 3x3 numpy array representing the game grid.

  Returns:
    True if there is a winner, False otherwise.
  """

  # Check if there is a winner in each row
  for row in grid:
    if np.all(row == row[0]) and row[0] != 0:
      return True

  # Check if there is a winner in each column
  for col in grid.T:
    if np.all(col == col[0]) and col[0] != 0:
      return True

  # Check if there is a winner in each diagonal
  if np.all(np.diag(grid) == np.diag(grid)[0]) and np.diag(grid)[0] != 0:
    return True

  if np.all(np.diag(np.flipud(grid)) == np.diag(np.flipud(grid))[0]) and np.diag(np.flipud(grid))[0] != 0:
    return True

  # If there is no winner, return False
  return False
