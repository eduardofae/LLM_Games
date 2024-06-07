
import numpy as np

# Create the grid
grid = np.zeros((10, 10))

# Define the players
player1 = 1
player2 = -1

# Define the game state
game_over = False
draw = False

# Start the game
while not game_over:
  # Get the player's move
  if grid[9, 0] == 0:
      column = int(input("Player 1, enter a column (0-9): "))
  else:
      column = int(input("Player 2, enter a column (0-9): "))

  # Check if the move is valid
  if grid[9, column] != 0:
    print("Invalid move, try again.")
    continue

  # Update the grid
  grid[9, column] = player1 if player1 == 1 else player2

  # Check if the player has won
  if check_win(grid, player1) or check_win(grid, player2):
    game_over = True
    print("Player {} wins!".format(1 if player1 == 1 else 2))
  # Check if there is a draw
  elif np.all(grid != 0):
    game_over = True
    draw = True
    print("Draw!")

  # Switch the player
  player1, player2 = player2, player1

# Define the function to check for a win
def check_win(grid, player):
  # Check for horizontal wins
  for row in range(10):
    if np.all(grid[row, :] == player):
      return True

  # Check for vertical wins
  for col in range(10):
    if np.all(grid[:, col] == player):
      return True

  # Check for diagonal wins
  for i in range(10):
    if np.all(grid[i, :i] == player) or np.all(grid[i, 9-i:] == player):
      return True

  return False

