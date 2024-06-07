import numpy as np

def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3), dtype=int)

  # Get the names of the two players
  player1 = input("Player 1, enter your name: ")
  player2 = input("Player 2, enter your name: ")

  # Start the game
  turn = 1
  while True:
    # Get the player's move
    if turn == 1:
      player = player1
    else:
      player = player2

    move = input(f"{player}, enter your move (row, column): ")
    row, column = map(int, move.split(","))

    # Check if the move is valid
    if grid[row, column] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the grid
    grid[row, column] = turn

    # Check if the player has won
    if check_win(grid, turn):
      print(f"{player} wins!")
      return turn

    # Check if the game is a draw
    if np.all(grid != 0):
      print("Draw!")
      return None

    # Switch turns
    turn = 3 - turn

def check_win(grid, turn):
  """
  Checks if the given player has won the game.

  Args:
    grid: The game grid.
    turn: The player's turn (1 or 2).

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row
  for row in range(3):
    if np.all(grid[row, :] == turn):
      return True

  # Check for a win in each column
  for column in range(3):
    if np.all(grid[:, column] == turn):
      return True

  # Check for a win in each diagonal
  if np.all(grid.diagonal() == turn):
    return True
  if np.all(np.flip(grid).diagonal() == turn):
    return True

  # No win yet
  return False


if __name__ == "__main__":
  jdv()
