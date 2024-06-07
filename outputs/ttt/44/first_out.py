import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3))

# Define the players
players = ['X', 'O']

# Start the game
current_player = 0

while True:
  # Get the player's move
  row, col = map(int, input("Player {}'s turn: ".format(players[current_player])).split())

  # Check if the move is valid
  if grid[row, col] != 0:
    print("Invalid move. Try again.")
    continue

  # Place the player's piece on the grid
  grid[row, col] = players[current_player]

  # Check if the player has won
  for i in range(3):
    if (grid[i, 0] == grid[i, 1] == grid[i, 2] != 0 or
        grid[0, i] == grid[1, i] == grid[2, i] != 0 or
        grid[0, 0] == grid[1, 1] == grid[2, 2] != 0 or
        grid[0, 2] == grid[1, 1] == grid[2, 0] != 0):
      print("Player {} wins!".format(players[current_player]))
      break

  # Check if the game is a draw
  if np.all(grid != 0):
    print("Draw!")
    break

  # Switch to the other player
  current_player = (current_player + 1) % 2
