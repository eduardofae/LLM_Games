import numpy as np

def jdv():
  """
  This function implements the jdv game.
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Get the players' names.
  player1 = input("Player 1, enter your name: ")
  player2 = input("Player 2, enter your name: ")

  # Set the current player to player 1.
  current_player = player1

  # Play the game until someone wins or there is a draw.
  while True:
    # Get the current player's move.
    move = input(f"{current_player}, enter your move (row, column): ")

    # Convert the move to a row and column.
    row, column = map(int, move.split(","))

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= column < 3 and board[row, column] == 0):
      print("Invalid move.")
      continue

    # Place the current player's piece on the board.
    board[row, column] = 1 if current_player == player1 else 2

    # Check if the current player has won.
    if check_win(board, current_player):
      print(f"{current_player} wins!")
      break

    # Check if there is a draw.
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch to the other player.
    current_player = player2 if current_player == player1 else player1


def check_win(board, player):
  """
  This function checks if the given player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check the rows.
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check the columns.
  for column in range(3):
    if np.all(board[:, column] == player):
      return True

  # Check the diagonals.
  if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
    return True

  return False


if __name__ == "__main__":
  jdv()
