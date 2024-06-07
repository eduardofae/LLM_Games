import numpy as np

def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if it's a draw.
  """

  # Get the player who goes first.
  player = input("Which player goes first? (1 or 2): ")

  # Check if the player's choice is valid.
  if player not in [1, 2]:
    print("Invalid choice. Please choose 1 or 2.")
    return jdv()

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Game loop.
  while True:
    # Print the game board.
    print_board(board)

    # Get the current player's move.
    print("Player {}'s move: ".format(player))
    move = input()

    # Parse the move.
    try:
      row, col = map(int, move.split())
    except ValueError:
      print("Invalid move. Please enter two numbers separated by a space.")
      continue

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= col < 3 and board[row, col] == 0):
      print("Invalid move. Please choose an empty space.")
      continue

    # Place the player's piece on the board.
    board[row, col] = player

    # Check if the player has won.
    if check_win(board, player):
      return player

    # Check if the game is a draw.
    if np.all(board != 0):
      return None

    # Switch to the other player.
    player = 3 - player


def check_win(board, player):
  """
  Checks if the given player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row.
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check for a win in each column.
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check for a win in each diagonal.
  if np.all(board.diagonal() == player):
    return True
  if np.all(np.flip(board.diagonal(), axis=0) == player):
    return True

  # No win found.
  return False


def print_board(board):
  """
  Prints the game board.
  """

  for row in range(3):
    for col in range(3):
      if board[row, col] == 0:
        print(" ", end=" ")
      elif board[row, col] == 1:
        print("X", end=" ")
      elif board[row, col] == 2:
        print("O", end=" ")
    print()


if __name__ == "__main__":
  # Play the game.
  winner = jdv()

  # Print the winner.
  if winner is None:
    print("Draw.")
  else:
    print("Player {} wins!".format(winner))
