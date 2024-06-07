import numpy as np

def jdv():
  """
  A simple game of JDV (3x3 grid tic-tac-toe).

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create a 3x3 grid of empty spaces.
  grid = np.empty((3, 3), dtype=str)

  # Player 1 is 'X' and player 2 is 'O'.
  players = ['X', 'O']

  # Keep track of whose turn it is.
  turn = 0

  # Play the game until someone wins or there are no more moves left.
  while True:
    # Get the player's move.
    move = input(f"Player {players[turn]}'s turn. Enter a row and column (e.g. 1,2): ")

    # Check if the move is valid.
    if not move or len(move) != 3 or not move[0].isdigit() or not move[2].isdigit():
      print("Invalid move. Please enter a row and column (e.g. 1,2).")
      continue

    # Convert the move to a row and column index.
    row, col = map(int, move.split(","))

    # Check if the space is empty.
    if grid[row-1][col-1] != '':
      print("That space is already taken. Please choose another space.")
      continue

    # Place the player's piece in the space.
    grid[row-1][col-1] = players[turn]

    # Check if the player has won.
    if check_win(grid, players[turn]):
      print(f"Player {players[turn]} wins!")
      return players[turn]

    # Check if there are no more moves left.
    if grid.all():
      print("Draw!")
      return None

    # Switch to the other player's turn.
    turn = (turn + 1) % 2

def check_win(grid, player):
  """
  Checks if the given player has won the game.

  Args:
    grid: The game grid.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row.
  for row in grid:
    if all(row == player):
      return True

  # Check for a win in each column.
  for col in grid.T:
    if all(col == player):
      return True

  # Check for a win in each diagonal.
  if all(grid.diagonal() == player) or all(np.flip(grid).diagonal() == player):
    return True

  # No win found.
  return False

if __name__ == "__main__":
  jdv()
