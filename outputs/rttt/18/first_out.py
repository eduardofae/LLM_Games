def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create a 3x3 grid.
  grid = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]

  # Get the players' names.
  player1 = input("Player 1, enter your name: ")
  player2 = input("Player 2, enter your name: ")

  # Determine which player goes first.
  turn = 1

  # Play the game until there is a winner or a draw.
  while True:
    # Get the current player's move.
    if turn == 1:
      move = input("%s, enter your move (row, column): " % player1)
    else:
      move = input("%s, enter your move (row, column): " % player2)

    # Convert the move to a row and column index.
    row, column = move.split(',')
    row = int(row) - 1
    column = int(column) - 1

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= column < 3):
      print("Invalid move. Please try again.")
      continue

    # Check if the space is already occupied.
    if grid[row][column] != ' ':
      print("Space already occupied. Please try again.")
      continue

    # Place the player's piece in the grid.
    if turn == 1:
      grid[row][column] = 'X'
    else:
      grid[row][column] = 'O'

    # Check if the player has won.
    if check_win(grid):
      if turn == 1:
        return player2
      else:
        return player1

    # Check if the game is a draw.
    if check_draw(grid):
      return None

    # Switch turns.
    turn = 3 - turn


def check_win(grid):
  """
  Checks if the given grid has a winner.

  Args:
    grid: A 3x3 grid.

  Returns:
    True if the grid has a winner, False otherwise.
  """

  # Check for horizontal wins.
  for row in grid:
    if row[0] != ' ' and row[0] == row[1] == row[2]:
      return True

  # Check for vertical wins.
  for column in range(3):
    if grid[0][column] != ' ' and grid[0][column] == grid[1][column] == grid[2][column]:
      return True

  # Check for diagonal wins.
  if grid[0][0] != ' ' and grid[0][0] == grid[1][1] == grid[2][2]:
    return True

  if grid[0][2] != ' ' and grid[0][2] == grid[1][1] == grid[2][0]:
    return True

  # No winner yet.
  return False


def check_draw(grid):
  """
  Checks if the given grid is a draw.

  Args:
    grid: A 3x3 grid.

  Returns:
    True if the grid is a draw, False otherwise.
  """

  # Check if there are any empty spaces.
  for row in grid:
    for space in row:
      if space == ' ':
        return False

  # No empty spaces, so the game is a draw.
  return True


if __name__ == "__main__":
  winner = jdv()

  if winner is None:
    print("The game is a draw.")
  else:
    print("%s wins!" % winner)
