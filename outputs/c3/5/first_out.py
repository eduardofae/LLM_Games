import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10))

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the current player
current_player = player1_symbol

# Define the game status
game_status = 'ongoing'

# Main game loop
while game_status == 'ongoing':
  # Get the player's input
  column = int(input('Enter a column (0-9): '))

  # Check if the column is valid
  if column < 0 or column > 9:
    print('Invalid column. Please enter a number between 0 and 9.')
    continue

  # Check if the column is full
  if grid[9, column] != 0:
    print('Column is full. Please choose another column.')
    continue

  # Place the player's piece in the lowest free space of the column
  for row in range(9, -1, -1):
    if grid[row, column] == 0:
      grid[row, column] = current_player
      break

  # Check if the player has won
  if check_win(grid, current_player):
    game_status = 'win'
    print(f'{current_player} wins!')
  # Check if the game is a draw
  elif np.all(grid != 0):
    game_status = 'draw'
    print('Draw!')

  # Switch the current player
  current_player = player2_symbol if current_player == player1_symbol else player1_symbol

# Print the final grid
print(grid)

# Define a function to check if the player has won
def check_win(grid, player):
  # Check for horizontal wins
  for row in range(10):
    if all(grid[row, i] == player for i in range(3)):
      return True

  # Check for vertical wins
  for column in range(10):
    if all(grid[i, column] == player for i in range(3)):
      return True

  # Check for diagonal wins
  for row in range(8):
    for column in range(8):
      if all(grid[row + i, column + i] == player for i in range(3)):
        return True

  # Check for anti-diagonal wins
  for row in range(8):
    for column in range(2, 10):
      if all(grid[row + i, column - i] == player for i in range(3)):
        return True

  # No win found
  return False
