import numpy as np

def print_board(board):
  """
  Prints the game board.

  Args:
    board: The game board.
  """

  for row in board:
    print(" ".join(["X" if x == 1 else "O" if x == 2 else "_" for x in row]))

def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Get the player names.
  player1_name = input("Enter the name of player 1: ")
  player2_name = input("Enter the name of player 2: ")

  # Choose who goes first.
  first_player = input("Who goes first? {} or {}: ".format(player1_name, player2_name))
  if first_player == player1_name:
    current_player = 1
  else:
    current_player = 2

  # Game loop.
  while True:
    # Print the game board.
    print_board(board)

    # Get the player's move.
    try:
      row = int(input("Player {}: Enter the row of your move (1-3): ".format(current_player)))
      col = int(input("Player {}: Enter the column of your move (1-3): ".format(current_player)))
    except ValueError:
      print("Invalid input. Please enter an integer between 1 and 3.")
      continue

    # Check if the move is valid.
    if board[row - 1, col - 1] != 0:
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the board.
    board[row - 1, col - 1] = current_player

    # Check if the player has won.
    if check_win(board, current_player):
      print("Player {} wins!".format(current_player))
      return current_player

    # Check if the game is a draw.
    if np.all(board != 0):
      print("Draw!")
      return None

    # Switch to the other player.
    current_player = 2 if current_player == 1 else 1


def check_win(board, player):
  """
  Checks if the player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for horizontal wins.
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check for vertical wins.
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check for diagonal wins.
  if np.all(np.diagonal(board) == player):
    return True
  if np.all(np.flip(np.diagonal(board)) == player):
    return True

  # No win found.
  return False


if __name__ == "__main__":
  jdv()
