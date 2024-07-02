import numpy as np

def print_grid(grid):
  for row in grid:
    print(' '.join([str(cell) for cell in row]))

def check_winner(grid):
  # Check rows
  for row in grid:
    if all(cell == row[0] for cell in row) and row[0] != 0:
      return row[0]

  # Check columns
  for col in range(len(grid[0])):
    if all(grid[row][col] == grid[0][col] for row in range(len(grid))) and grid[0][col] != 0:
      return grid[0][col]

  # Check diagonals
  if all(grid[row][row] == grid[0][0] for row in range(len(grid))) and grid[0][0] != 0:
    return grid[0][0]
  if all(grid[row][len(grid)-row-1] == grid[0][len(grid)-1] for row in range(len(grid))) and grid[0][len(grid)-1] != 0:
    return grid[0][len(grid)-1]

  # Check for draw
  if all(cell != 0 for row in grid for cell in row):
    return -1

  # No winner yet
  return 0

def play_jdv():
  # Create a 3x3 grid
  grid = np.zeros((3,3), dtype=int)

  # Player 1 starts
  player = 1

  # Play until there is a winner or a draw
  while True:
    # Print the grid
    print_grid(grid)

    # Get the player's move
    while True:
      move = input(f"Player {player}, enter your move (row, column): ")
      try:
        row, col = map(int, move.split(','))
      except ValueError:
        print("Invalid move. Please enter a comma-separated pair of integers.")
        continue
      if not (0 <= row < 3 and 0 <= col < 3):
        print("Invalid move. Please enter a pair of integers between 0 and 2.")
        continue
      if grid[row, col] != 0:
        print("Invalid move. That space is already taken.")
        continue
      break

    # Place the player's piece in the grid
    grid[row, col] = player

    # Check for a winner or a draw
    winner = check_winner(grid)
    if winner != 0:
      print_grid(grid)
      if winner == -1:
        print("Draw!")
      else:
        print(f"Player {winner} wins!")
      break

    # Switch players
    player = 3 - player

# Play the game
if __name__ == "__main__":
  play_jdv()
