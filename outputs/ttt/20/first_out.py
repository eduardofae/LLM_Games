import numpy as np

def print_grid(grid):
  """Prints the current state of the grid."""
  for row in grid:
    print(" ".join(row))

def check_win(grid, player):
  """Checks if the given player has won the game."""
  # Check rows
  for row in grid:
    if all(row == player):
      return True

  # Check columns
  for col in range(3):
    if all(grid[row][col] == player for row in range(3)):
      return True

  # Check diagonals
  if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
    return True
  if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
    return True

  # No win yet
  return False

def get_valid_moves(grid):
  """Returns a list of valid moves for the current state of the grid."""
  valid_moves = []
  for row in range(3):
    for col in range(3):
      if grid[row][col] == " ":
        valid_moves.append((row, col))
  return valid_moves

def play_game():
  """Plays the game of jdv."""

  # Create the game grid
  grid = np.array([[" " for _ in range(3)] for _ in range(3)])

  # Initialize the current player
  current_player = "X"

  # Game loop
  while True:
    # Print the current state of the grid
    print_grid(grid)

    # Get the valid moves for the current player
    valid_moves = get_valid_moves(grid)

    # If there are no valid moves, the game is a draw
    if not valid_moves:
      print("Draw!")
      break

    # Get the player's move
    move = input(f"{current_player}'s turn: ")
    row, col = map(int, move.split())

    # Check if the move is valid
    if (row, col) not in valid_moves:
      print("Invalid move!")
      continue

    # Place the player's piece on the grid
    grid[row][col] = current_player

    # Check if the player has won
    if check_win(grid, current_player):
      print(f"{current_player} wins!")
      break

    # Switch to the other player
    current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
  play_game()
