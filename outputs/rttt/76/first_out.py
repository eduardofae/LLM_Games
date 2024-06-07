def jdv():
  """
  Plays a game of JDV.

  The game is played on a 3x3 grid. Two players take turns placing their pieces
  in a free space of the grid. The first player to make a line of 3 (horizontally,
  vertically, or diagonally) adjacent pieces wins. If there are no more free spaces,
  the game is declared a draw.

  Args:
    None

  Returns:
    None
  """

  # Create a 3x3 grid
  grid = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]

  # Get the names of the two players
  player1 = input("Enter the name of player 1: ")
  player2 = input("Enter the name of player 2: ")

  # Determine which player will go first
  first_player = input("Who will go first? (1 or 2) ")

  # Keep track of the current player
  current_player = first_player

  # Keep track of the number of moves that have been made
  num_moves = 0

  # Main game loop
  while True:
    # Get the next move from the current player
    row = int(input("Enter the row for your move: "))
    col = int(input("Enter the column for your move: "))

    # Check if the move is valid
    if row < 0 or row > 2 or col < 0 or col > 2 or grid[row][col] != ' ':
      print("Invalid move. Try again.")
      continue

    # Place the current player's piece in the grid
    grid[row][col] = current_player

    # Increment the number of moves
    num_moves += 1

    # Check if the current player has won
    if check_for_win(grid, current_player):
      print(f"{current_player} wins!")
      break

    # Check if the game is a draw
    if num_moves == 9:
      print("Draw!")
      break

    # Switch to the other player
    current_player = '1' if current_player == '2' else '2'


def check_for_win(grid, player):
  """
  Checks if the given player has won the game.

  Args:
    grid: The current state of the game board
    player: The player to check for a win

  Returns:
    True if the player has won, False otherwise
  """

  # Check for a win in each row
  for row in grid:
    if all(x == player for x in row):
      return True

  # Check for a win in each column
  for col in range(3):
    if all(grid[row][col] == player for row in range(3)):
      return True

  # Check for a win in each diagonal
  if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
    return True
  if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
    return True

  # No win found
  return False


if __name__ == "__main__":
  jdv()
