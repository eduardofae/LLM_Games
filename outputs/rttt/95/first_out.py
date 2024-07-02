import numpy as np

def jdv():
  """
  This function implements the jdv game.

  The game is played on a 3x3 grid. Two players take turns placing their pieces in a free space of the grid.
  The first player to make a line of 3 adjacent pieces (horizontally, vertically or diagonally) loses.
  If there are no more free spaces, the game is declared a draw.

  The function returns the winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Set the current player to 1.
  player = 1

  # While there are free spaces on the board, continue playing.
  while np.any(board == 0):
    # Get the move from the current player.
    move = get_move(board, player)

    # Place the player's piece on the board.
    board[move[0], move[1]] = player

    # Check if the player has won.
    if check_win(board, player):
      return player

    # Switch to the other player.
    player = 3 - player

  # If there are no more free spaces, the game is a draw.
  return None


def get_move(board, player):
  """
  This function gets the move from the current player.

  The function takes the game board and the current player as input, and returns the move as a tuple of the row and column indices.

  The move must be a free space on the board.

  If the player enters an invalid move, the function will ask for the move again.
  """

  while True:
    # Get the move from the player.
    move = input("Player {} enter your move (row, column): ".format(player))

    # Convert the move to a tuple of integers.
    try:
      move = tuple(map(int, move.split(",")))
    except:
      print("Invalid move. Please enter a valid move in the format (row, column).")
      continue

    # Check if the move is valid.
    if not (0 <= move[0] < 3 and 0 <= move[1] < 3 and board[move[0], move[1]] == 0):
      print("Invalid move. The space is not free.")
      continue

    # Return the move.
    return move


def check_win(board, player):
  """
  This function checks if the given player has won the game.

  The function takes the game board and the current player as input, and returns True if the player has won, and False otherwise.

  A player wins if they have made a line of 3 adjacent pieces (horizontally, vertically or diagonally).
  """

  # Check the rows.
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check the columns.
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check the diagonals.
  if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
    return True

  # The player has not won.
  return False


if __name__ == "__main__":
  # Play the game.
  winner = jdv()

  # Print the winner.
  if winner is None:
    print("The game is a draw.")
  else:
    print("Player {} wins!".format(winner))
