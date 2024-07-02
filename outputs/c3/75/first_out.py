import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10))

# Create a list of players
players = ["Player 1", "Player 2"]

# Create a loop to let the players take turns
while True:
  # Get the current player
  player = players[0]

  # Get the player's move
  move = int(input(f"{player}, choose a column (0-9): "))

  # Check if the move is valid
  if move < 0 or move > 9 or grid[9, move] != 0:
    print("Invalid move")
    continue

  # Place the player's piece on the grid
  for i in range(9, -1, -1):
    if grid[i, move] == 0:
      grid[i, move] = 1 if player == "Player 1" else 2
      break

  # Check if the player has won
  if check_win(grid, player):
    print(f"{player} wins!")
    break

  # Check if the game is a draw
  if np.all(grid != 0):
    print("Draw!")
    break

  # Switch to the next player
  players = players[1:]

# Define a function to check if a player has won
def check_win(grid, player):
  # Check for horizontal wins
  for i in range(10):
    if np.all(grid[i, :] == player):
      return True

  # Check for vertical wins
  for j in range(10):
    if np.all(grid[:, j] == player):
      return True

  # Check for diagonal wins
  for i in range(10):
    for j in range(10):
      if grid[i, j] == player and (
          (i + 2 < 10 and grid[i + 1, j + 1] == player and grid[i + 2, j + 2] == player) or
          (i - 2 >= 0 and grid[i - 1, j + 1] == player and grid[i - 2, j + 2] == player) or
          (j + 2 < 10 and grid[i, j + 1] == player and grid[i, j + 2] == player) or
          (j - 2 >= 0 and grid[i, j - 1] == player and grid[i, j - 2] == player)
      ):
        return True

  return False
