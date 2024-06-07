# Create a 3x3 grid
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Define the players
player1 = 'X'
player2 = 'O'

# Define the current player
current_player = player1

# Define the game status
game_status = 'ongoing'

# Get the player's move
def get_player_move():
  while True:
    try:
      row, column = map(int, input('Enter the row and column of your move (e.g. 1 2): ').split())
      if row < 1 or row > 3 or column < 1 or column > 3 or grid[row - 1][column - 1] != ' ':
        print('Invalid move. Please try again.')
      else:
        return row - 1, column - 1
    except ValueError:
      print('Invalid input. Please enter two numbers separated by a space.')

# Check if there is a winner
def check_winner():
  # Check rows
  for row in range(3):
    if grid[row][0] == grid[row][1] == grid[row][2] != ' ':
      return grid[row][0]

  # Check columns
  for column in range(3):
    if grid[0][column] == grid[1][column] == grid[2][column] != ' ':
      return grid[0][column]

  # Check diagonals
  if grid[0][0] == grid[1][1] == grid[2][2] != ' ':
    return grid[0][0]
  if grid[0][2] == grid[1][1] == grid[2][0] != ' ':
    return grid[0][2]

  return None

# Update the game status
def update_game_status():
  winner = check_winner()
  if winner:
    game_status = f'{winner} wins!'
  elif all(all(cell != ' ' for cell in row) for row in grid):
    game_status = 'Draw'

# Print the game board
def print_board():
  for row in grid:
    print(' | '.join(row))
  print('-' * 5)

# Main game loop
while game_status == 'ongoing':
  # Get the player's move
  row, column = get_player_move()

  # Place the player's piece on the board
  grid[row][column] = current_player

  # Print the game board
  print_board()

  # Check if there is a winner
  update_game_status()

  # Switch the current player
  current_player = player2 if current_player == player1 else player1

# Print the game status
print(game_status)
