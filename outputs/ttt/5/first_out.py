import numpy as np

def jdv():
  """
  This function plays a game of jdv, a 2-player game where players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line wins. If there are no more free spaces, the game is declared a draw.
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3))

  # Set the player turn to 1
  player = 1

  # While there are no winners and free spaces
  while not check_winner(grid) and not check_draw(grid):
    # Get the player's move
    move = get_move(grid, player)

    # Place the player's piece in the grid
    grid[move[0], move[1]] = player

    # Switch the player turn
    player = 3 - player

  # Check if there is a winner
  if check_winner(grid):
    print(f"Player {player} wins!")
  else:
    print("Draw!")

def get_move(grid, player):
  """
  This function gets the player's move.

  Args:
    grid: The current state of the grid.
    player: The player whose turn it is.

  Returns:
    A tuple representing the row and column of the player's move.
  """

  # Get the player's input
  while True:
    move = input(f"Player {player}, enter your move (row, column): ")

    # Check if the move is valid
    if not move.isdigit() or int(move) < 1 or int(move) > 3:
      print("Invalid move. Please enter a number between 1 and 3.")
    else:
      move = (int(move) - 1, int(input("Enter your column: ")) - 1)
      if grid[move[0], move[1]] != 0:
        print("Invalid move. Please choose an empty space.")
      else:
        return move

def check_winner(grid):
  """
  This function checks if there is a winner.

  Args:
    grid: The current state of the grid.

  Returns:
    True if there is a winner, False otherwise.
  """

  # Check for horizontal wins
  for row in grid:
    if np.all(row == row[0]) and row[0] != 0:
      return True

  # Check for vertical wins
  for col in grid.T:
    if np.all(col == col[0]) and col[0] != 0:
      return True

  # Check for diagonal wins
  if np.all(grid.diagonal() == grid.diagonal()[0]) and grid.diagonal()[0] != 0:
    return True
  if np.all(np.flip(grid).diagonal() == np.flip(grid).diagonal()[0]) and np.flip(grid).diagonal()[0] != 0:
    return True

  # No winner yet
  return False

def check_draw(grid):
  """
  This function checks if the game is a draw.

  Args:
    grid: The current state of the grid.

  Returns:
    True if the game is a draw, False otherwise.
  """

  # If there are no more free spaces, the game is a draw
  return np.all(grid != 0)

if __name__ == "__main__":
  jdv()
