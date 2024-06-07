import numpy as np

def check_winner(board):
  """Check if there is a winner in the board.

  Args:
    board: A 10x10 numpy array representing the game board.

  Returns:
    The player number of the winner, or 0 if there is no winner.
  """

  # Check for horizontal lines.
  for row in range(10):
    for col in range(7):
      if board[row, col] != 0 and board[row, col] == board[row, col+1] and board[row, col] == board[row, col+2]:
        return board[row, col]

  # Check for vertical lines.
  for col in range(10):
    for row in range(7):
      if board[row, col] != 0 and board[row, col] == board[row+1, col] and board[row, col] == board[row+2, col]:
        return board[row, col]

  # Check for diagonal lines.
  for row in range(7):
    for col in range(7):
      if board[row, col] != 0 and board[row, col] == board[row+1, col+1] and board[row, col] == board[row+2, col+2]:
        return board[row, col]

      if board[row, col] != 0 and board[row, col] == board[row+1, col-1] and board[row, col] == board[row+2, col-2]:
        return board[row, col]

  # No winner yet.
  return 0


def print_board(board):
  """Print the game board.

  Args:
    board: A 10x10 numpy array representing the game board.
  """

  for row in range(10):
    for col in range(10):
      if board[row, col] == 0:
        print(".", end=" ")
      elif board[row, col] == 1:
        print("X", end=" ")
      elif board[row, col] == 2:
        print("O", end=" ")
    print()


def main():
  # Create a new game board.
  board = np.zeros((10, 10), dtype=int)

  # Set the current player to 1.
  current_player = 1

  # Start the game loop.
  while True:
    # Print the game board.
    print_board(board)

    # Get the player's move.
    column = int(input("Player {}'s turn. Enter a column number (0-9): ".format(current_player)))

    # Drop the player's piece into the column.
    for row in range(9, -1, -1):
      if board[row, column] == 0:
        board[row, column] = current_player
        break

    # Check for a winner.
    winner = check_winner(board)

    # If there is a winner, print the winner and exit the game.
    if winner != 0:
      print("Player {} wins!".format(winner))
      break

    # If the board is full, declare a draw and exit the game.
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch to the other player.
    current_player = 3 - current_player


if __name__ == "__main__":
  main()
