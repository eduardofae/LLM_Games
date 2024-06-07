import numpy as np

def jdv():
  """
  This function implements the game jdv.

  The game is played on a 3x3 grid. Two players take turns placing their pieces in a free space of the grid. The first player to make a line of three adjacent pieces (horizontally, vertically, or diagonally) loses the game. If there are no more free spaces, the game is declared a draw.

  The function returns the winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Set the current player to 1.
  player = 1

  # Keep track of the number of free spaces.
  free_spaces = 9

  # Play the game until there are no more free spaces or a player wins.
  while free_spaces > 0:
    # Get the player's move.
    move = input("Player {}'s move: ".format(player))

    # Convert the move to a row and column.
    row, col = map(int, move.split(","))

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= col < 3 and board[row, col] == 0):
      print("Invalid move.")
      continue

    # Place the player's piece on the board.
    board[row, col] = player

    # Decrement the number of free spaces.
    free_spaces -= 1

    # Check if the player has won.
    if check_win(board, player):
      return player

    # Switch to the other player.
    player = 3 - player

  # If there are no more free spaces, the game is a draw.
  return None

def check_win(board, player):
  """
  This function checks if the given player has won the game.

  The function returns True if the player has won, and False otherwise.
  """

  # Check for a win in each row.
  for row in range(3):
    if board[row, 0] == player and board[row, 1] == player and board[row, 2] == player:
      return True

  # Check for a win in each column.
  for col in range(3):
    if board[0, col] == player and board[1, col] == player and board[2, col] == player:
      return True

  # Check for a win in each diagonal.
  if board[0, 0] == player and board[1, 1] == player and board[2, 2] == player:
    return True

  if board[0, 2] == player and board[1, 1] == player and board[2, 0] == player:
    return True

  # If there is no win, return False.
  return False

if __name__ == "__main__":
  # Play the game.
  winner = jdv()

  # Print the winner.
  if winner is None:
    print("Draw.")
  else:
    print("Player {} wins.".format(winner))
