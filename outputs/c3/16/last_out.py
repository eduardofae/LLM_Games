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

# Simplified code to get the valid moves
def get_valid_moves(grid):
  return [(row, col) for col in range(len(grid[0])) for row in range(len(grid)) if grid[row][col] == ' ']

def play_game():
  """Plays a game of pong."""
  grid = [[' ' for _ in range(10)] for _ in range(10)]
  players = ['X', 'O']
  currentPlayer = 0
  scores = [0, 0]

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
      scores[currentPlayer] += 1
      break

    # Switch to the other player
    currentPlayer = (currentPlayer + 1) % 2

  # Print the final scores
  print("Final scores:")
  for i in range(len(players)):
    print(f"Player {players[i]}: {scores[i]}")

  # Ask if the players want to play again
  play_again = input("Do you want to play again? (y/n) ")
  if play_again == 'y':
    play_game()

if __name__ == "__main__":
  play_game()
