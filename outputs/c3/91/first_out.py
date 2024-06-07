
import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Create a list of players
players = ['X', 'O']

# Create a variable to keep track of the current player
current_player = 0

# Create a variable to keep track of the game state
game_state = 'in progress'

# Create a loop to run the game
while game_state == 'in progress':
  # Get the column where the player wants to place their piece
  column = int(input(f'Player {players[current_player]}, choose a column (0-9): '))

  # Check if the column is valid
  if column < 0 or column > 9:
    print('Invalid column')
    continue

  # Check if the column is full
  if grid[9, column] != 0:
    print('Column is full')
    continue

  # Place the player's piece in the column
  for i in range(9, -1, -1):
    if grid[i, column] == 0:
      grid[i, column] = players[current_player]
      break

  # Check if the player has won
  if check_win(grid, players[current_player]):
    game_state = 'won'
    print(f'Player {players[current_player]} wins!')
  
  # Check if the game is a draw
  elif np.all(grid != 0):
    game_state = 'draw'
    print('Draw!')

  # Switch to the next player
  current_player = (current_player + 1) % 2

# Print the final grid
print(grid)

def check_win(grid, player):
  # Check for horizontal wins
  for i in range(10):
    if all(grid[i, j] == player for j in range(3)):
      return True

  # Check for vertical wins
  for j in range(10):
    if all(grid[i, j] == player for i in range(3)):
      return True

  # Check for diagonal wins
  for i in range(8):
    if all(grid[i+k, j+k] == player for k in range(3)):
      return True

  for i in range(2, 10):
    if all(grid[i-k, j+k] == player for k in range(3)):
      return True

  return False
