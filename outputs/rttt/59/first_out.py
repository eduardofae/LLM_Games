import numpy as np

def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create a 3x3 grid.
  grid = np.zeros((3, 3), dtype=int)

  # Get the names of the two players.
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Keep track of whose turn it is.
  turn = 1

  # Loop until the game is over.
  while True:

    # Get the player's move.
    if turn == 1:
      move = input(f"{player1}, enter your move (row, column): ")
    else:
      move = input(f"{player2}, enter your move (row, column): ")

    # Convert the move to a row and column.
    row, column = map(int, move.split(","))

    # Check if the move is valid.
    if grid[row, column] != 0:
      print("That move is invalid. Please try again.")
      continue

    # Place the player's piece on the grid.
    grid[row, column] = turn

    # Check if the player has won.
    if check_win(grid, turn):
      if turn == 1:
        print(f"{player1} wins!")
      else:
        print(f"{player2} wins!")
      return turn

    # Check if the game is a draw.
    if np.all(grid != 0):
      print("The game is a draw.")
      return None

    # Switch turns.
    turn = 3 - turn


def check_win(grid, turn):
  """
  Checks if the player with the given turn has won the game.

  Args:
    grid: The game grid.
    turn: The player's turn.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row.
  for row in range(3):
    if np.all(grid[row, :] == turn):
      return True

  # Check for a win in each column.
  for column in range(3):
    if np.all(grid[:, column] == turn):
      return True

  # Check for a win in each diagonal.
  if np.all(grid.diagonal() == turn) or np.all(np.flip(grid).diagonal() == turn):
    return True

  # No win found.
  return False


if __name__ == "__main__":
  jdv()
