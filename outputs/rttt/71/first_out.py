import numpy as np

def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Set the current player.
  currentPlayer = 1

  # Play the game until someone wins or there are no more moves.
  while True:
    # Get the current player's move.
    move = getMove(currentPlayer)

    # Place the player's piece on the board.
    board[move[0], move[1]] = currentPlayer

    # Check if the player has won.
    if checkWin(board, currentPlayer):
      return currentPlayer

    # Check if there are no more moves.
    if np.all(board != 0):
      return None

    # Switch the current player.
    currentPlayer = 3 - currentPlayer

def getMove(currentPlayer):
  """
  Gets a move from the current player.

  Args:
    currentPlayer: The current player.

  Returns:
    A tuple representing the move.
  """

  while True:
    # Get the player's input.
    move = input("Player {}'s move: ".format(currentPlayer))

    # Check if the move is valid.
    if not isValidMove(move):
      print("Invalid move. Please try again.")
      continue

    # Return the move.
    return move

def isValidMove(move):
  """
  Checks if a move is valid.

  Args:
    move: The move to check.

  Returns:
    True if the move is valid, False otherwise.
  """

  # Check if the move is in the correct format.
  if not move.isdigit() or len(move) != 2:
    return False

  # Check if the move is within the bounds of the board.
  row, col = map(int, move)
  if row < 0 or row > 2 or col < 0 or col > 2:
    return False

  # Check if the space is already occupied.
  if board[row, col] != 0:
    return False

  # The move is valid.
  return True

def checkWin(board, currentPlayer):
  """
  Checks if the current player has won.

  Args:
    board: The game board.
    currentPlayer: The current player.

  Returns:
    True if the current player has won, False otherwise.
  """

  # Check for a win in each row.
  for row in range(3):
    if np.all(board[row, :] == currentPlayer):
      return True

  # Check for a win in each column.
  for col in range(3):
    if np.all(board[:, col] == currentPlayer):
      return True

  # Check for a win in each diagonal.
  if np.all(board.diagonal() == currentPlayer):
    return True
  if np.all(np.flip(board).diagonal() == currentPlayer):
    return True

  # The current player has not won.
  return False

if __name__ == "__main__":
  # Play the game.
  winner = jdv()

  # Print the winner.
  if winner is None:
    print("Draw")
  else:
    print("Player {} wins".format(winner))
