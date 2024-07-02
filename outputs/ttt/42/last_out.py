def jdv():
  """
  This function implements the jdv game.

  The game is played on a 3x3 grid. Two players take turns placing their pieces in a free space of the grid.
  The first player to make a line of 3 (horizontally, vertically or diagonally) adjacent pieces wins.
  If there are no more free spaces, the game is declared a draw.
  """

  # Create a 3x3 grid using a dictionary.
  grid = {}
  for row in range(3):
    for column in range(3):
      grid[(row, column)] = ' '

  # Get the names of the two players.
  player1 = input("Player 1, enter your name: ")
  player2 = input("Player 2, enter your name: ")

  # Set the current player to player1.
  current_player = player1

  # Play the game until one player wins or there are no more free spaces.
  while True:
    # Get the row and column of the player's move.
    while True:
      try:
        row = int(input(f"{current_player}, enter the row (0-2) of your move: "))
        column = int(input(f"{current_player}, enter the column (0-2) of your move: "))
        if row < 0 or row > 2 or column < 0 or column > 2:
          raise ValueError("Invalid row or column.")
        if grid[(row, column)] != ' ':
          raise ValueError("Space already occupied.")
        break
      except ValueError as e:
        print(e)

    # Place the player's piece in the grid.
    grid[(row, column)] = current_player

    # Print the current state of the grid.
    print_grid(grid)

    # Check if the player has won.
    if check_win(grid, current_player):
      print(f"{current_player} wins!")
      break

    # Check if there are no more free spaces.
    if all(space != ' ' for space in grid.values()):
      print("Draw!")
      break

    # Switch the current player.
    if current_player == player1:
      current_player = player2
    else:
      current_player = player1

def check_win(grid, player):
  """
  This function checks if the given player has won the game.

  The game is played on a 3x3 grid. A player wins if they have a line of 3 (horizontally, vertically or diagonally) adjacent pieces.

  Args:
    grid: The current state of the game grid.
    player: The player to check for a win.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a horizontal win.
  for row in range(3):
    if all(grid[(row, column)] == player for column in range(3)):
      return True

  # Check for a vertical win.
  for column in range(3):
    if all(grid[(row, column)] == player for row in range(3)):
      return True

  # Check for a diagonal win.
  if all(grid[(row, row)] == player for row in range(3)):
    return True
  if all(grid[(row, 2-row)] == player for row in range(3)):
    return True

  # No win found.
  return False

def print_grid(grid):
  """
  This function prints the current state of the game grid.
  """

  for row in range(3):
    for column in range(3):
      print(grid[(row, column)], end=" ")
    print()


if __name__ == "__main__":
  jdv()
