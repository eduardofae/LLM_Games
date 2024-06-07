import numpy as np

def jdv():
  """
  Plays a game of jdv.

  The game is played on a 3x3 grid. Two players take turns placing their pieces
  in a free space of the grid. The first player to make a line of 3 (horizontally,
  vertically, or diagonally) adjacent pieces wins. If there are no more free spaces,
  the game is declared a draw.

  Args:
    None

  Returns:
    The winner of the game, or "Draw" if the game is a draw.
  """

  # Create a 3x3 grid.
  grid = np.zeros((3, 3), dtype=int)

  # Get the player who goes first.
  first_player = choose_first_player()

  # Set the current player to the first player.
  current_player = first_player

  # While there are no winners and there are still free spaces, continue playing.
  while not is_winner(grid) and not is_draw(grid):
    # Get the player's move.
    move = get_move(grid, current_player)

    # Place the player's piece on the grid.
    grid[move[0], move[1]] = current_player

    # Switch to the other player.
    current_player = 3 - current_player

  # Check if there is a winner.
  if is_winner(grid):
    return current_player

  # If there is no winner, the game is a draw.
  return "Draw"


def choose_first_player():
  """
  Gets the player who goes first.

  Args:
    None

  Returns:
    The player who goes first.
  """

  while True:
    try:
      first_player = int(input("Who goes first (1 or 2)? "))
      if first_player not in [1, 2]:
        print("Invalid input. Please enter 1 or 2.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter 1 or 2.")

  return first_player


def is_winner(grid):
  """
  Checks if there is a winner in the given grid.

  Args:
    grid: A 3x3 numpy array representing the game grid.

  Returns:
    True if there is a winner, False otherwise.
  """

  # Check for horizontal wins.
  for i in range(3):
    if grid[i, 0] != 0 and grid[i, 0] == grid[i, 1] and grid[i, 1] == grid[i, 2]:
      return True

  # Check for vertical wins.
  for j in range(3):
    if grid[0, j] != 0 and grid[0, j] == grid[1, j] and grid[1, j] == grid[2, j]:
      return True

  # Check for diagonal wins.
  if grid[0, 0] != 0 and grid[0, 0] == grid[1, 1] and grid[1, 1] == grid[2, 2]:
    return True
  if grid[0, 2] != 0 and grid[0, 2] == grid[1, 1] and grid[1, 1] == grid[2, 0]:
    return True

  # No winner yet.
  return False


def is_draw(grid):
  """
  Checks if the given grid is a draw.

  Args:
    grid: A 3x3 numpy array representing the game grid.

  Returns:
    True if the grid is a draw, False otherwise.
  """

  # If there are no more free spaces, the game is a draw.
  if np.count_nonzero(grid) == 9:
    return True

  # Otherwise, the game is not a draw.
  return False


def get_move(grid, player):
  """
  Gets the player's move.

  Args:
    grid: A 3x3 numpy array representing the game grid.
    player: The player who is making the move.

  Returns:
    A tuple representing the player's move.
  """

  while True:
    try:
      move = tuple(int(x) for x in input("Player {}'s move (row, column): ".format(player)).split(","))
      if not is_valid_move(grid, move):
        print("Invalid move. Please try again.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter two integers separated by a comma.")

  return move


def is_valid_move(grid, move):
  """
  Checks if the player's move is valid.

  Args:
    grid: A 3x3 numpy array representing the game grid.
    move: A tuple representing the player's move.

  Returns:
    True if the move is valid, False otherwise.
  """

  # Check if the move is within the bounds of the grid.
  if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
    return False

  # Check if the space is already occupied.
  if grid[move[0], move[1]] != 0:
    return False

  # The move is valid.
  return True


if __name__ == "__main__":
  winner = jdv()
  if winner == "Draw":
    print("The game is a draw.")
  else:
    print("Player {} wins!".format(winner))
