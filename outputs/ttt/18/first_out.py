import numpy as np

def check_win(board):
  """
  Checks if there is a winner in the given board.

  Args:
    board: A 3x3 numpy array representing the game board.

  Returns:
    The winner, or None if there is no winner.
  """

  # Check for horizontal wins
  for row in board:
    if np.all(row == row[0]) and row[0] != 0:
      return row[0]

  # Check for vertical wins
  for col in board.T:
    if np.all(col == col[0]) and col[0] != 0:
      return col[0]

  # Check for diagonal wins
  if np.all(np.diag(board) == np.diag(board)[0]) and np.diag(board)[0] != 0:
    return np.diag(board)[0]

  if np.all(np.diag(np.flip(board)) == np.diag(np.flip(board))[0]) and np.diag(np.flip(board))[0] != 0:
    return np.diag(np.flip(board))[0]

  # No winner yet
  return None


def jdv():
  """
  Plays a game of jdv.
  """

  # Create a 3x3 game board
  board = np.zeros((3, 3), dtype=int)

  # Keep track of whose turn it is
  player = 1

  # Play the game until there is a winner or a draw
  while True:
    # Get the player's move
    move = input(f"Player {player}, enter your move (row, column): ")

    # Check if the move is valid
    row, col = map(int, move.split(","))
    if row < 0 or row > 2 or col < 0 or col > 2:
      print("Invalid move. Please enter a row and column between 0 and 2.")
      continue

    if board[row, col] != 0:
      print("That space is already taken. Please choose another space.")
      continue

    # Place the player's piece on the board
    board[row, col] = player

    # Check if there is a winner
    winner = check_win(board)
    if winner is not None:
      print(f"Player {winner} wins!")
      break

    # Switch to the other player
    player = 3 - player

    # Check if the board is full
    if np.all(board != 0):
      print("Draw!")
      break


if __name__ == "__main__":
  jdv()
