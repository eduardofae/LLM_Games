import numpy as np

def print_board(board):
  """Prints the game board."""
  for row in board:
    for cell in row:
      print(cell, end=" ")
    print()


def check_winner(board):
  """Checks if there is a winner."""
  # Check for horizontal lines
  for row in board:
    if len(set(row)) == 1 and row[0] != 0:
      return row[0]

  # Check for vertical lines
  for col in range(10):
    column = [row[col] for row in board]
    if len(set(column)) == 1 and column[0] != 0:
      return column[0]

  # Check for diagonal lines
  diagonals = [
      [board[i][i] for i in range(10)],
      [board[i][9 - i] for i in range(10)],
  ]
  for diagonal in diagonals:
    if len(set(diagonal)) == 1 and diagonal[0] != 0:
      return diagonal[0]

  # Check for a draw
  if np.count_nonzero(board) == 100:
    return "Draw"

  # No winner yet
  return None


def get_move(player):
  """Gets a move from the player."""
  while True:
    try:
      column = int(input(f"Player {player}, choose a column (1-10): "))
      if 1 <= column <= 10:
        return column
      else:
        print("Invalid column. Please choose a column between 1 and 10.")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 10.")


def main():
  """Runs the game."""

  # Create the game board
  board = np.zeros((10, 10), dtype=int)

  # Set the current player
  player = 1

  # Play the game until there is a winner or a draw
  while True:
    # Print the game board
    print_board(board)

    # Get a move from the player
    column = get_move(player)

    # Place the player's piece on the board
    for i in range(9, -1, -1):
      if board[i][column - 1] == 0:
        board[i][column - 1] = player
        break

    # Check if there is a winner
    winner = check_winner(board)
    if winner is not None:
      if winner == "Draw":
        print("Draw!")
      else:
        print(f"Player {winner} wins!")
      break

    # Switch to the other player
    player = 3 - player


if __name__ == "__main__":
  main()
