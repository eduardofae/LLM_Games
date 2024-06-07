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
  player_turn = 1

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

  def is_game_over(board):
    """
    Check if the game is over.

    Args:
      board: The game board.

    Returns:
      True if the game is over, False otherwise.
    """

    # Check if there are any more free spaces.
    if np.all(board != 0):
      return True

    # Check if either player has won.
    if check_win(board, 1) or check_win(board, 2):
      return True

    # The game is not over.
    return False

  def reset_board():
    """
    Reset the game board to its initial state.
    """

    board[:] = 0

  # Play the game until someone wins or there are no more free spaces.
  while not is_game_over(board):
    # Get the player's move.
    while True:
      try:
        move = input("Player {}'s move (row, column): ".format(player_turn))
        row, column = map(int, move.split(","))

        # Check if the move is valid.
        if not (0 <= row < 3 and 0 <= column < 3 and board[row, column] == 0):
          print("Invalid move.")
          continue
        break
      except:
        print("Invalid input. Please enter a valid row and column.")

    # Place the player's piece on the board.
    board[row, column] = player_turn

    # Check if the player has won.
    if check_win(board, player_turn):
      print("Player {} wins!".format(player_turn))
      return player_turn

    # Switch to the other player.
    player_turn = 3 - player_turn

  # The game is a draw.
  print("Draw!")
  return None

if __name__ == "__main__":
  while True:
    jdv()

    # Ask the players if they want to play again.
    play_again = input("Play again? (y/n): ")
    if play_again == "n":
      break

    # Reset the game board.
    reset_board()
