def jdv():
  """
  Plays a game of jdv, a 3x3 grid game where players take turns placing their pieces until one of them makes a line of 3 adjacent pieces.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create a 3x3 grid
  grid = [[" ", " ", " "] for _ in range(3)]

  # Get the names of the two players
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Determine who goes first
  currentPlayer = player1

  # Play the game until one player wins or there is a draw
  while True:
    # Get the current player's move
    row, col = map(int, input(f"{currentPlayer}, enter your move (row, column): ").split())

    # Check if the move is valid
    if grid[row][col] != " ":
      print("That space is already taken.")
      continue

    # Place the current player's piece in the grid
    grid[row][col] = currentPlayer

    # Check if the current player has won
    if check_win(grid, currentPlayer):
      print(f"{currentPlayer} wins!")
      return currentPlayer

    # Check if there is a draw
    if check_draw(grid):
      print("The game is a draw.")
      return None

    # Switch to the other player
    currentPlayer = player2 if currentPlayer == player1 else player1


def check_win(grid, player):
  """
  Checks if the given player has won the game.

  Args:
    grid: The game grid.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for horizontal wins
  for row in grid:
    if all(row[i] == player for i in range(3)):
      return True

  # Check for vertical wins
  for col in range(3):
    if all(grid[i][col] == player for i in range(3)):
      return True

  # Check for diagonal wins
  if grid[0][0] == grid[1][1] == grid[2][2] == player:
    return True

  if grid[0][2] == grid[1][1] == grid[2][0] == player:
    return True

  # No wins found
  return False


def check_draw(grid):
  """
  Checks if the game is a draw.

  Args:
    grid: The game grid.

  Returns:
    True if the game is a draw, False otherwise.
  """

  # Check if there are any empty spaces left
  for row in grid:
    for col in row:
      if col == " ":
        return False

  # No empty spaces left, so the game is a draw
  return True


if __name__ == "__main__":
  jdv()
