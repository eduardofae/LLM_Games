import numpy as np

def jdv():
  """
  A simple game of JDV.

  The game is played on a 3x3 grid. Two players take turns placing their pieces
  in a free space of the grid. The first player to make a line of 3 (horizontally,
  vertically, or diagonally) adjacent pieces wins. If there are no more free spaces,
  the game is declared a draw.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Get the names of the two players.
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")

  # Set the current player to player 1.
  current_player = 1

  # Game loop.
  while True:
    # Get the current player's move.
    move = input(f"{player1_name if current_player == 1 else player2_name}'s move: ")

    # Check if the move is valid.
    if not move.isdigit() or int(move) < 1 or int(move) > 9:
      print("Invalid move.")
      continue

    # Convert the move to a row and column index.
    row = (int(move) - 1) // 3
    col = (int(move) - 1) % 3

    # Check if the space is free.
    if board[row, col] != 0:
      print("That space is already taken.")
      continue

    # Place the current player's piece in the space.
    board[row, col] = current_player

    # Check if the current player has won.
    if check_win(board, current_player):
      print(f"{player1_name if current_player == 1 else player2_name} wins!")
      return current_player

    # Check if the board is full.
    if np.all(board != 0):
      print("Draw!")
      return None

    # Switch the current player.
    current_player = 2 if current_player == 1 else 1


def check_win(board, player):
  """
  Checks if the given player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win horizontally.
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check for a win vertically.
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check for a win diagonally.
  if np.all(board.diagonal() == player):
    return True

  if np.all(np.flip(board).diagonal() == player):
    return True

  # No win found.
  return False


if __name__ == "__main__":
  jdv()
