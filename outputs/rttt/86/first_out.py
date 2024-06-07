import numpy as np

def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create a 3x3 grid.
  grid = np.zeros((3, 3), dtype=int)

  # Get the players' names.
  player1_name = input("Player 1, enter your name: ")
  player2_name = input("Player 2, enter your name: ")

  # Keep track of whose turn it is.
  turn = 1

  # Play the game until someone wins or there are no more moves left.
  while True:
    # Get the player's move.
    if turn == 1:
      move = input(f"{player1_name}, enter your move (row, column): ")
    else:
      move = input(f"{player2_name}, enter your move (row, column): ")

    # Convert the move to a row and column.
    row, column = map(int, move.split(","))

    # Check if the move is valid.
    if grid[row, column] != 0:
      print("That space is already taken.")
      continue

    # Place the player's piece on the grid.
    grid[row, column] = turn

    # Check if the player has won.
    if check_win(grid, turn):
      if turn == 1:
        print(f"{player1_name} wins!")
      else:
        print(f"{player2_name} wins!")
      return turn

    # Check if there are no more moves left.
    if np.all(grid != 0):
      print("Draw!")
      return None

    # Switch turns.
    turn = 3 - turn


def check_win(grid, turn):
  """
  Checks if the given player has won the game.

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
  if np.all(grid.diagonal() == turn):
    return True
  if np.all(np.flip(grid).diagonal() == turn):
    return True

  # No win yet.
  return False


if __name__ == "__main__":
  jdv()
