import numpy as np

def jdv():
  """
  Play a game of jdv.

  The game is played on a 3x3 grid. Two players take turns placing their
  pieces in a free space of the grid. The first player to make a line of three
  adjacent pieces wins. If there are no more free spaces, the game is declared
  a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Get the player names.
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Set the current player to player 1.
  current_player = player1

  # Game loop.
  while True:
    # Get the player's move.
    row, col = map(int, input(f"{current_player}, enter your move (row, col): ").split())

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= col < 3 and board[row, col] == 0):
      print("Invalid move.")
      continue

    # Place the player's piece on the board.
    board[row, col] = 1 if current_player == player1 else 2

    # Check if the player has won.
    if check_win(board):
      print(f"{current_player} wins!")
      break

    # Check if the game is a draw.
    if np.all(board != 0):
      print("Draw.")
      break

    # Switch the current player.
    current_player = player2 if current_player == player1 else player1


def check_win(board):
  """
  Check if a player has won the game.

  Args:
    board: The game board.

  Returns:
    True if a player has won, False otherwise.
  """

  # Check for a win in each row.
  for row in board:
    if np.all(row == row[0]) and row[0] != 0:
      return True

  # Check for a win in each column.
  for col in board.T:
    if np.all(col == col[0]) and col[0] != 0:
      return True

  # Check for a win in each diagonal.
  if np.all(np.diag(board) == np.diag(board)[0]) and np.diag(board)[0] != 0:
    return True
  if np.all(np.diag(np.flip(board)) == np.diag(np.flip(board))[0]) and np.diag(np.flip(board))[0] != 0:
    return True

  # No win yet.
  return False


if __name__ == "__main__":
  jdv()
