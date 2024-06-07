import numpy as np

def jdv():
  """
  Play a game of jdv.

  This game is played on a 3x3 grid. Two players take turns placing their pieces in a free space of the grid.
  The first player to make a line of 3 (horizontally, vertically or diagonally) adjacent pieces wins.
  If there are no more free spaces, the game is declared a draw.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Set the current player to player 1.
  current_player = 1

  # Play the game until someone wins or there are no more free spaces.
  while True:
    # Get the player's move.
    move = input("Player {}'s move (row, column): ".format(current_player))
    row, column = map(int, move.split(","))

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= column < 3 and board[row, column] == 0):
      print("Invalid move.")
      continue

    # Place the player's piece on the board.
    board[row, column] = current_player

    # Check if the player has won.
    if check_win(board, current_player):
      print("Player {} wins!".format(current_player))
      return current_player

    # Switch to the other player.
    current_player = 3 - current_player

    # Check if the game is a draw.
    if np.all(board != 0):
      print("Draw!")
      return None

def check_win(board, player):
  """
  Check if the given player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check if the player has won horizontally.
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check if the player has won vertically.
  for column in range(3):
    if np.all(board[:, column] == player):
      return True

  # Check if the player has won diagonally.
  if np.all(board.diagonal() == player):
    return True
  if np.all(np.flip(board, axis=0).diagonal() == player):
    return True

  # The player has not won.
  return False

if __name__ == "__main__":
  jdv()
