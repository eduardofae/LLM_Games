import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Create a list of players
players = [1, 2]

# Keep track of the current player
current_player = 0

# Game loop
while True:
  # Get the player's move
  move = int(input("Player {}'s move: ".format(players[current_player])))

  # Check if the move is valid
  if move < 1 or move > 10 or grid[move-1, :].any():
    print("Invalid move")
    continue

  # Place the player's piece on the grid
  grid[move-1, np.argmin(grid[move-1, :])] = players[current_player]

  # Check if the player has won
  if np.any(np.all(grid == players[current_player], axis=0)) or np.any(np.all(grid == players[current_player], axis=1)) or np.any(np.diagonal(grid) == players[current_player]) or np.any(np.flipud(np.diagonal(grid)) == players[current_player]):
    print("Player {} wins!".format(players[current_player]))
    break

  # Check if the game is a draw
  if np.all(grid != 0):
    print("Draw")
    break

  # Switch to the other player
  current_player = (current_player + 1) % 2

# Print the final grid
print(grid)
