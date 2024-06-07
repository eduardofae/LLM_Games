import numpy as np

def check_winner(grid):
  # Check rows
  for row in grid:
    if np.all(row == row[0]) and row[0] != 0:
      return row[0]

  # Check columns
  for col in grid.T:
    if np.all(col == col[0]) and col[0] != 0:
      return col[0]

  # Check diagonals
  if np.all(grid.diagonal() == grid.diagonal()[0]) and grid.diagonal()[0] != 0:
    return grid.diagonal()[0]

  if np.all(np.flip(grid).diagonal() == np.flip(grid).diagonal()[0]) and np.flip(grid).diagonal()[0] != 0:
    return np.flip(grid).diagonal()[0]

  return 0


def print_grid(grid):
  print("---------")
  for row in grid:
    print("|", end="")
    for cell in row:
      if cell == 0:
        print(" ", end="|")
      elif cell == 1:
        print("X", end="|")
      elif cell == 2:
        print("O", end="|")
    print()
  print("---------")


def main():
  # Initialize the game grid
  grid = np.zeros((3, 3), dtype=int)

  # Keep track of the current player
  player = 1

  # Game loop
  while True:
    # Print the current grid
    print_grid(grid)

    # Get the player's move
    move = input(f"Player {player}, enter your move (row, column): ")
    row, col = map(int, move.split(','))

    # Check if the move is valid
    if grid[row, col] != 0:
      print("Invalid move. Cell already occupied.")
      continue

    # Place the player's piece on the grid
    grid[row, col] = player

    # Check if the player has won
    winner = check_winner(grid)
    if winner != 0:
      print(f"Player {winner} wins!")
      break

    # Check if the game is a draw
    if np.all(grid != 0):
      print("Draw!")
      break

    # Switch to the other player
    player = 3 - player


if __name__ == "__main__":
  main()
