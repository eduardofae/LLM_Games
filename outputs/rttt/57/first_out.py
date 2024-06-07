import numpy as np

def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if it's a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Keep track of the current player.
  player = 1

  # Keep track of the number of moves that have been made.
  moves = 0

  # Game loop.
  while True:
    # Get the player's move.
    move = input("Player {}'s move: ".format(player))

    # Parse the move.
    row, col = map(int, move.split())

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= col < 3 and board[row, col] == 0):
      print("Invalid move.")
      continue

    # Place the player's piece on the board.
    board[row, col] = player

    # Increment the number of moves.
    moves += 1

    # Check if the player has won.
    if check_win(board, player):
      return player

    # Check if the game is a draw.
    if moves == 9:
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

if __name__ == "__main__":
  # Play the game.
  winner = jdv()

  # Print the winner.
  if winner is None:
    print("Draw.")
  else:
    print("Player {} wins!".format(winner))
