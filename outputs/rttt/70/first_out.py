import numpy as np

def jdv():
  """
  A simple 3x3 grid game where two players take turns placing their pieces in a free space until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw.
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3))

  # Set the player's symbols
  player1_symbol = 'X'
  player2_symbol = 'O'

  # Set the current player
  current_player = player1_symbol

  # Game loop
  while True:
    # Get the player's move
    move = input(f"{current_player}'s turn. Enter a row and column (e.g. 1,2): ")
    row, column = map(int, move.split(','))

    # Check if the move is valid
    if grid[row, column] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the grid
    grid[row, column] = current_player

    # Check if the player has won
    if check_win(grid, current_player):
      print(f"{current_player} wins!")
      break

    # Check if the game is a draw
    if np.all(grid != 0):
      print("Draw!")
      break

    # Switch the current player
    current_player = player2_symbol if current_player == player1_symbol else player1_symbol

def check_win(grid, player):
  """
  Checks if the player has won.

  Args:
    grid: The game grid.
    player: The player's symbol.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for horizontal wins
  for row in range(3):
    if np.all(grid[row] == player):
      return True

  # Check for vertical wins
  for column in range(3):
    if np.all(grid[:, column] == player):
      return True

  # Check for diagonal wins
  if np.all(np.diagonal(grid) == player):
    return True

  if np.all(np.flip(np.diagonal(grid)) == player):
    return True

  # No win
  return False

if __name__ == "__main__":
  jdv()
