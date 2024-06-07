def jdv():
  """
  This function implements the jdv game.

  The game is played on a 3x3 grid, and two players take turns placing their pieces in the grid.
  The first player to get three of their pieces in a row, either horizontally, vertically, or diagonally, wins the game.
  If all the squares in the grid are filled and neither player has won, the game is declared a draw.
  """

  # Create a 3x3 grid
  grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

  # Get the names of the two players
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Set the current player to player 1
  current_player = player1

  # Keep track of the number of moves that have been made
  moves = 0

  # Game loop
  while True:
    # Print the grid
    print("   0 1 2")
    for i in range(3):
      print(i, "|".join(grid[i]))

    # Get the player's move
    move = input(f"{current_player}, where would you like to place your piece? (row, column) ")
    row, column = map(int, move.split(","))

    # Check if the move is valid
    if row < 0 or row > 2 or column < 0 or column > 2 or grid[row][column] != ' ':
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece in the grid
    grid[row][column] = current_player

    # Check if the player has won
    if check_win(grid, current_player):
      print(f"{current_player} wins!")
      break

    # Increment the number of moves
    moves += 1

    # Check if the game is a draw
    if moves == 9:
      print("Draw!")
      break

    # Switch the current player
    if current_player == player1:
      current_player = player2
    else:
      current_player = player1


def check_win(grid, player):
  """
  This function checks if the given player has won the game.

  Args:
    grid: The game grid.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for horizontal wins
  for row in range(3):
    if grid[row][0] == player and grid[row][1] == player and grid[row][2] == player:
      return True

  # Check for vertical wins
  for column in range(3):
    if grid[0][column] == player and grid[1][column] == player and grid[2][column] == player:
      return True

  # Check for diagonal wins
  if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
    return True

  if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
    return True

  # No wins found
  return False


if __name__ == "__main__":
  jdv()
