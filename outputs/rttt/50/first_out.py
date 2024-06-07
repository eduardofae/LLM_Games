# Create a 3x3 grid
grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

# Create a list of the players
players = ['X', 'O']

# Set the current player to the first player in the list
current_player = players[0]

# Create a function to check if a player has won
def check_win(grid):
  # Check for a win horizontally
  for row in grid:
    if row[0] == row[1] == row[2] and row[0] != ' ':
      return True

  # Check for a win vertically
  for col in range(3):
    if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
      return True

  # Check for a win diagonally
  if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
    return True
  if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
    return True

  # Return False if there is no win
  return False

# Create a function to check if the game is a draw
def check_draw(grid):
  # Check if all the spaces are filled
  for row in grid:
    for space in row:
      if space == ' ':
        return False

  # Return True if the game is a draw
  return True

# Create a function to get the player's input
def get_input(grid):
  # Get the player's row and column input
  row = int(input("Enter a row (1-3): ")) - 1
  column = int(input("Enter a column (1-3): ")) - 1

  # Check if the space is empty
  if grid[row][column] != ' ':
    print("That space is already taken.")
    return get_input(grid)  # Recursively call the function to get the player's input again

  # Return the player's input
  return row, column

# Create a function to play the game
def play_game():
  # Loop until the game is over
  while True:
    # Get the player's input
    row, column = get_input(grid)

    # Place the player's piece in the grid
    grid[row][column] = current_player

    # Check if the player has won
    if check_win(grid):
      print(f"{current_player} wins!")
      break

    # Check if the game is a draw
    if check_draw(grid):
      print("The game is a draw.")
      break

    # Switch to the other player
    current_player = players[(players.index(current_player) + 1) % 2]

# Play the game
play_game()
