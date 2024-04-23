import numpy as np

def jdv():
  """
  This function implements the jdv game.

  The game is played on a 3x3 grid, and two players take turns placing their pieces in a free space.
  The first player to make a line of 3 (horizontally, vertically, or diagonally) adjacent pieces loses.
  If there are no more free spaces, the game is declared a draw.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Set the current player to 1.
  current_player = 1

  # While there are free spaces on the board...
  while np.any(board == 0):
    # Get the row and column of the player's move.
    row, col = input(f"Player {current_player}, enter your move (row, column): ").split()

    # Convert the row and column to integers.
    row = int(row)
    col = int(col)

    # Check if the move is valid.
    if board[row, col] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board.
    board[row, col] = current_player

    # Check if the player has won.
    if is_winner(board, current_player):
      print(f"Player {current_player} wins!")
      return current_player

    # Switch to the other player.
    current_player = 3 - current_player

  # If there are no more free spaces, the game is a draw.
  print("Draw!")
  return None


def is_winner(board, player):
  """
  This function checks if a player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check if the player has won horizontally.
  for row in range(3):
    if board[row, 0] == player and board[row, 1] == player and board[row, 2] == player:
      return True

  # Check if the player has won vertically.
  for col in range(3):
    if board[0, col] == player and board[1, col] == player and board[2, col] == player:
      return True

  # Check if the player has won diagonally.
  if board[0, 0] == player and board[1, 1] == player and board[2, 2] == player:
    return True
  if board[0, 2] == player and board[1, 1] == player and board[2, 0] == player:
    return True

  # The player has not won.
  return False


if __name__ == "__main__":
  jdv()