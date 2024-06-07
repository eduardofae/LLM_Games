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

  # Get the player names or symbols.
  player1_name = input("Player 1, enter your name or symbol: ")
  player2_name = input("Player 2, enter your name or symbol: ")

  # Set the current player to 1.
  player = 1

  # While there are free spaces on the board, continue playing.
  while np.any(board == 0):
    # Get the move from the current player.
    move = get_move(board, player, player1_name, player2_name)

    # Place the player's piece on the board.
    board[move[0], move[1]] = player

    # Check if the player has won.
    if check_win(board, player, move):
      return player

    # Switch to the other player.
    player = 3 - player

  # If there are no more free spaces, the game is a draw.
  return None


def get_move(board, player, player1_name, player2_name):
  """
  This function gets the move from the current player.

  The function takes the game board, the current player, and the names or symbols of the two players as input, and returns the move as a tuple of the row and column indices.

  The move must be a free space on the board.

  If the player enters an invalid move, the function will ask for the move again.
  """

  while True:
    try:
      # Get the move from the player.
      if player == 1:
        move = input("{} enter your move (row, column): ".format(player1_name))
      else:
        move = input("{} enter your move (row, column): ".format(player2_name))

      # Convert the move to a tuple of integers.
      move = tuple(map(int, move.split(",")))

      # Check if the move is valid.
      if not (0 <= move[0] < 3 and 0 <= move[1] < 3 and board[move[0], move[1]] == 0):
        print("Invalid move. The space is not free.")
        continue

      # Return the move.
      return move

    except ValueError:
      print("Invalid move. Please enter a valid move in the format (row, column).")
      continue


def check_win(board, player, move):
  """
  This function checks if the given player has won the game.

  The function takes the game board, the current player, and the last move as input, and returns True if the player has won, and False otherwise.

  A player wins if they have made a line of 3 adjacent pieces (horizontally, vertically or diagonally).
  """

  # Check the row.
  if np.all(board[move[0], :] == player):
    return True

  # Check the column.
  if np.all(board[:, move[1]] == player):
    return True

  # Check the diagonals.
  if move[0] == move[1]:
    # Check the main diagonal.
    if np.all(board.diagonal() == player):
      return True
  else:
    # Check the secondary diagonal.
    if np.all(np.flip(board).diagonal() == player):
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
    print("{} wins!".format(winner))
