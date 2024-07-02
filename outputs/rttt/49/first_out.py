def jdv():
  """
  A simple game of JDV.

  The game is played on a 3x3 grid. Two players take turns placing their pieces
  in a free space of the grid. The first player to get three of their pieces in
  a row, either horizontally, vertically, or diagonally, wins the game. If there
  are no more free spaces, the game is declared a draw.
  """

  # Create a 3x3 grid.
  grid = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]

  # Get the names of the two players.
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Set the current player to player 1.
  current_player = player1

  # Play the game until there is a winner or a draw.
  while True:
    # Get the player's move.
    row, col = map(int, input("{}, what is your move? (row, column) ".format(current_player)).split())

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= col < 3 and grid[row][col] == ' '):
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the grid.
    grid[row][col] = 'X' if current_player == player1 else 'O'

    # Check if the player has won.
    if check_win(grid):
      print("{} wins!".format(current_player))
      break

    # Check if there are no more free spaces.
    if all(all(cell != ' ' for cell in row) for row in grid):
      print("Draw!")
      break

    # Switch the current player.
    current_player = player2 if current_player == player1 else player1


def check_win(grid):
  """
  Check if there is a winner in the given grid.

  Args:
    grid: A 3x3 grid.

  Returns:
    True if there is a winner, False otherwise.
  """

  # Check for horizontal wins.
  for row in grid:
    if all(cell == row[0] for cell in row) and row[0] != ' ':
      return True

  # Check for vertical wins.
  for col in range(3):
    if all(grid[row][col] == grid[0][col] for row in range(3)) and grid[0][col] != ' ':
      return True

  # Check for diagonal wins.
  if all(grid[row][row] == grid[0][0] for row in range(3)) and grid[0][0] != ' ':
    return True

  if all(grid[row][2 - row] == grid[0][2] for row in range(3)) and grid[0][2] != ' ':
    return True

  # No winner yet.
  return False


if __name__ == "__main__":
  jdv()
