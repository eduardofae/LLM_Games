import numpy as np

def jdv():
  """
  A simple game of jdv.

  The game is played on a 3x3 grid. Two players take turns placing their pieces in a free space.
  The first player to make a line of three adjacent pieces wins. If there are no more free spaces, the game is declared a draw.
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3), dtype=int)

  # Define the player's symbols
  player1_symbol = 'X'
  player2_symbol = 'O'

  # Keep track of whose turn it is
  turn = 1

  # Keep track of the number of moves made
  moves = 0

  # Game loop
  while True:
    # Print the grid
    print(grid)

    # Get the player's move
    if turn == 1:
      row, col = input("Player 1, enter your move (row, column): ").split()
    else:
      row, col = input("Player 2, enter your move (row, column): ").split()

    # Check if the move is valid
    if not (0 <= int(row) < 3 and 0 <= int(col) < 3 and grid[int(row), int(col)] == 0):
      print("Invalid move.")
      continue

    # Place the player's piece in the grid
    if turn == 1:
      grid[int(row), int(col)] = player1_symbol
    else:
      grid[int(row), int(col)] = player2_symbol

    # Check if the player has won
    if check_win(grid, player1_symbol) or check_win(grid, player2_symbol):
      print(f"Player {turn} wins!")
      break

    # Check if the game is a draw
    moves += 1
    if moves == 9:
      print("Draw!")
      break

    # Change turns
    turn = 3 - turn

def check_win(grid, symbol):
  """
  Checks if a player has won the game.

  Args:
    grid: The game grid.
    symbol: The player's symbol.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check if the player has won horizontally
  for row in range(3):
    if grid[row, 0] == grid[row, 1] == grid[row, 2] == symbol:
      return True

  # Check if the player has won vertically
  for col in range(3):
    if grid[0, col] == grid[1, col] == grid[2, col] == symbol:
      return True

  # Check if the player has won diagonally
  if grid[0, 0] == grid[1, 1] == grid[2, 2] == symbol or grid[0, 2] == grid[1, 1] == grid[2, 0] == symbol:
    return True

  # The player has not won
  return False


if __name__ == "__main__":
  jdv()
