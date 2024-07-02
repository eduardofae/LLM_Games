
import numpy as np

def check_winner(grid):
  # Check rows
  for i in range(3):
    if np.all(grid[i] == grid[i][0]) and grid[i][0] != 0:
      return grid[i][0]
  # Check columns
  for j in range(3):
    if np.all(grid[:, j] == grid[0, j]) and grid[0, j] != 0:
      return grid[0, j]
  # Check diagonals
  if np.all(np.diag(grid) == grid[0, 0]) and grid[0, 0] != 0:
    return grid[0, 0]
  if np.all(np.diag(grid[::-1]) == grid[0, 2]) and grid[0, 2] != 0:
    return grid[0, 2]
  # Check draw
  if np.all(grid != 0):
    return -1
  # No winner or draw
  return 0

def print_grid(grid):
  for i in range(3):
    for j in range(3):
      print(grid[i, j], end=" ")
    print()

def play_jdv():
  grid = np.zeros((3, 3), dtype=int)
  player = 1
  while True:
    print_grid(grid)
    print("Player", player, "turn")
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))
    if row < 0 or row > 2 or col < 0 or col > 2 or grid[row, col] != 0:
      print("Invalid move")
      continue
    grid[row, col] = player
    winner = check_winner(grid)
    if winner != 0:
      if winner == -1:
        print("Draw")
      else:
        print("Player", player, "wins")
      break
    player = 3 - player

if __name__ == "__main__":
  play_jdv()
