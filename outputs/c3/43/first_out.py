import numpy as np

GRID_SIZE = 10

def create_grid():
  """Creates a new empty grid."""
  return np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

def print_grid(grid):
  """Prints the grid to the console."""
  for row in grid:
    for cell in row:
      print(cell, end=" ")
    print()

def place_piece(grid, player, col):
  """Places a piece in the lowest free space of the given column."""
  for row in range(GRID_SIZE-1, -1, -1):
    if grid[row][col] == 0:
      grid[row][col] = player
      return

def check_win(grid):
  """Checks if there is a line of 3 adjacent pieces."""
  # Check horizontal lines
  for row in range(GRID_SIZE):
    for col in range(GRID_SIZE-2):
      if grid[row][col] != 0 and grid[row][col] == grid[row][col+1] == grid[row][col+2]:
        return grid[row][col]

  # Check vertical lines
  for col in range(GRID_SIZE):
    for row in range(GRID_SIZE-2):
      if grid[row][col] != 0 and grid[row][col] == grid[row+1][col] == grid[row+2][col]:
        return grid[row][col]

  # Check diagonal lines
  for row in range(GRID_SIZE-2):
    for col in range(GRID_SIZE-2):
      if grid[row][col] != 0 and grid[row][col] == grid[row+1][col+1] == grid[row+2][col+2]:
        return grid[row][col]
  
  return 0

def is_draw(grid):
  """Checks if the game is a draw."""
  return np.all(grid != 0)

def main():
  """Plays the game."""
  grid = create_grid()
  players = [1, 2]
  current_player = 0

  while True:
    print_grid(grid)

    col = int(input("Player {}: Choose a column (0-9): ".format(players[current_player])))

    place_piece(grid, players[current_player], col)

    winner = check_win(grid)
    if winner != 0:
      print("Player {} wins!".format(winner))
      break

    if is_draw(grid):
      print("Draw!")
      break

    current_player = (current_player + 1) % 2

if __name__ == "__main__":
  main()
