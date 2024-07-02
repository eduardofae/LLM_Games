import numpy as np

def jdv():
  """
  A simple 2-player game where players take turns placing their pieces in a 3x3 grid,
  until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces,
  in which case the person that made the line wins. If there are no more free spaces, the game is declared a draw.
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3))

  # Set the current player to 1 (the first player)
  current_player = 1

  # Keep track of the number of moves made
  num_moves = 0

  # Main game loop
  while True:
    # Get the player's move
    move = input(f"Player {current_player}, enter your move (row, column): ")
    row, column = map(int, move.split(","))

    # Check if the move is valid
    if grid[row, column] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece in the grid
    grid[row, column] = current_player

    # Increment the number of moves made
    num_moves += 1

    # Check if the player has won
    if check_for_win(grid, current_player):
      print(f"Player {current_player} wins!")
      break

    # Check if there are no more free spaces
    if num_moves == 9:
      print("Draw!")
      break

    # Switch to the other player
    current_player = 2 if current_player == 1 else 1

def check_for_win(grid, player):
  """
  Checks if the given player has won the game.

  Args:
    grid: The current state of the game board.
    player: The player to check for a win.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row
  for row in range(3):
    if grid[row, 0] == grid[row, 1] == grid[row, 2] == player:
      return True

  # Check for a win in each column
  for col in range(3):
    if grid[0, col] == grid[1, col] == grid[2, col] == player:
      return True

  # Check for a win in each diagonal
  if grid[0, 0] == grid[1, 1] == grid[2, 2] == player:
    return True

  if grid[0, 2] == grid[1, 1] == grid[2, 0] == player:
    return True

  # No win found
  return False


if __name__ == "__main__":
  jdv()
