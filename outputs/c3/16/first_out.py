import numpy as np

def print_grid(grid):
  """Prints the grid to the console."""
  for row in grid:
    for cell in row:
      print(cell, end=" ")
    print()

def check_winner(grid):
  """Checks if there is a winner.

  Returns the winner's symbol if there is a winner, or None otherwise."""
  # Check for horizontal wins
  for row in grid:
    if len(set(row)) == 1 and row[0] != ' ':
      return row[0]

  # Check for vertical wins
  for col in range(len(grid[0])):
    column = [row[col] for row in grid]
    if len(set(column)) == 1 and column[0] != ' ':
      return column[0]

  # Check for diagonal wins
  diagonals = [[grid[i][i] for i in range(len(grid))],
               [grid[i][len(grid)-i-1] for i in range(len(grid))]]

  for diagonal in diagonals:
    if len(set(diagonal)) == 1 and diagonal[0] != ' ':
      return diagonal[0]

  # No winner yet
  return None

def get_valid_moves(grid):
  """Gets the valid moves for the current player.

  Returns a list of tuples representing the valid moves."""
  valid_moves = []
  for col in range(len(grid[0])):
    if grid[0][col] == ' ':
      valid_moves.append((0, col))

  return valid_moves

def play_game():
  """Plays a game of pong."""
  grid = [[' ' for _ in range(10)] for _ in range(10)]
  players = ['X', 'O']
  currentPlayer = 0

  while True:
    print_grid(grid)

    # Get the valid moves for the current player
    valid_moves = get_valid_moves(grid)

    # If there are no valid moves, the game is a draw
    if not valid_moves:
      print("Draw!")
      break

    # Get the player's move
    move = input(f"Player {players[currentPlayer]}, enter your move (row, col): ")
    row, col = map(int, move.split(","))

    # Check if the move is valid
    if (row, col) not in valid_moves:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the grid
    grid[row][col] = players[currentPlayer]

    # Check if the player has won
    winner = check_winner(grid)
    if winner:
      print(f"Player {winner} wins!")
      break

    # Switch to the other player
    currentPlayer = (currentPlayer + 1) % 2

if __name__ == "__main__":
  play_game()
