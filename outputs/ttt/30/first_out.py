
def jdv():
  """
  Play a game of jdv.

  Args:
    None

  Returns:
    None
  """

  # Create a 3x3 grid
  grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

  # Get the names of the two players
  player1_name = input("Player 1, enter your name: ")
  player2_name = input("Player 2, enter your name: ")

  # Decide who goes first
  first_player = input("Who goes first? (1 or 2) ")
  if first_player == "1":
    current_player = player1_name
  else:
    current_player = player2_name

  # Play the game
  while True:
    # Get the current player's move
    row = int(input("Enter a row (1-3): ")) - 1
    column = int(input("Enter a column (1-3): ")) - 1

    # Check if the move is valid
    if grid[row][column] != ' ':
      print("Invalid move. That space is already taken.")
      continue

    # Place the current player's piece in the grid
    grid[row][column] = 'X' if current_player == player1_name else 'O'

    # Check if the current player has won
    if check_for_win(grid):
      print(f"{current_player} wins!")
      break

    # Check if the game is a draw
    if check_for_draw(grid):
      print("It's a draw!")
      break

    # Switch to the other player
    if current_player == player1_name:
      current_player = player2_name
    else:
      current_player = player1_name

def check_for_win(grid):
  """
  Check if the given grid has a winning line.

  Args:
    grid: A 3x3 grid

  Returns:
    True if there is a winning line, False otherwise
  """

  # Check for horizontal wins
  for row in grid:
    if row[0] == row[1] == row[2] and row[0] != ' ':
      return True

  # Check for vertical wins
  for column in range(3):
    if grid[0][column] == grid[1][column] == grid[2][column] and grid[0][column] != ' ':
      return True

  # Check for diagonal wins
  if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
    return True
  if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
    return True

  # No winning line found
  return False

def check_for_draw(grid):
  """
  Check if the given grid is a draw.

  Args:
    grid: A 3x3 grid

  Returns:
    True if the game is a draw, False otherwise
  """

  # Check if there are any empty spaces left
  for row in grid:
    for space in row:
      if space == ' ':
        return False

  # No empty spaces left, so it's a draw
  return True

# Play the game
jdv()
