import numpy as np

def jdv():
  """
  This function implements the jdv game.

  The game is played on a 3x3 grid. Two players take turns placing their pieces
  in a free space of the grid. The first player to make a line of 3 (horizontally,
  vertically or diagonally) adjacent pieces wins. If there are no more free spaces,
  the game is declared a draw.

  Args:
    None

  Returns:
    None
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Define the players.
  players = ["X", "O"]

  # Set the current player to player 1.
  current_player = 0

  # Play the game until one player wins or there are no more free spaces.
  while True:
    # Get the player's move.
    move = input("Player {}'s turn. Enter a row and column (e.g. 1,2): ".format(players[current_player]))

    # Convert the move to a row and column index.
    row, column = map(int, move.split(","))

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= column < 3 and board[row, column] == 0):
      print("Invalid move.")
      continue

    # Place the player's piece on the board.
    board[row, column] = players[current_player]

    # Check if the player has won.
    if check_win(board, players[current_player]):
      print("Player {} wins!".format(players[current_player]))
      break

    # Check if there are no more free spaces.
    if np.all(board != 0):
      print("Draw.")
      break

    # Switch to the other player.
    current_player = (current_player + 1) % 2

def check_win(board, player):
  """
  This function checks if the given player has won the game.

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
  if np.all(board.diagonal() == player) or np.all(np.fliplr(board).diagonal() == player):
    return True

  # The player has not won.
  return False

# Play the game.
jdv()
