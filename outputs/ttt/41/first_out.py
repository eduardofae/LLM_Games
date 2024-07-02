import numpy as np

def jdv():
  """
  This function implements the jdv game.

  Returns:
    The winner of the game, or None if there is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Create the two players.
  players = [1, 2]

  # Keep track of the current player.
  current_player = 0

  # Play the game until there is a winner or a draw.
  while True:
    # Get the player's move.
    move = input("Player {}'s move: ".format(players[current_player]))

    # Check if the move is valid.
    if not (0 <= move[0] < 3 and 0 <= move[1] < 3):
      print("Invalid move.")
      continue

    # Check if the space is already occupied.
    if board[move[0], move[1]] != 0:
      print("Space already occupied.")
      continue

    # Place the player's piece on the board.
    board[move[0], move[1]] = players[current_player]

    # Check if the player has won.
    if check_win(board, players[current_player]):
      print("Player {} wins!".format(players[current_player]))
      return players[current_player]

    # Check if there is a draw.
    if np.all(board != 0):
      print("Draw!")
      return None

    # Switch to the other player.
    current_player = (current_player + 1) % 2


def check_win(board, player):
  """
  This function checks if the player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check the rows.
  for row in board:
    if np.all(row == player):
      return True

  # Check the columns.
  for column in board.T:
    if np.all(column == player):
      return True

  # Check the diagonals.
  if np.all(board.diagonal() == player):
    return True

  if np.all(np.flip(board).diagonal() == player):
    return True

  # No win.
  return False


if __name__ == "__main__":
  jdv()
