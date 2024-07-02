import numpy as np

def jdv():
  """
  JdV game.

  Two players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. 
  If there are no more free spaces, the game is declared a draw.
  """

  # Initialize the game board
  board = np.zeros((3, 3), dtype=int)

  # Initialize the player turn
  player = 1

  # Main game loop
  while True:
    # Get the player's move
    row, col = map(int, input("Player {}: Enter your move (row, column): ".format(player)).split())

    # Check if the move is valid
    if not (0 <= row < 3 and 0 <= col < 3 and board[row, col] == 0):
      print("Invalid move. Please try again.")
      continue

    # Update the game board
    board[row, col] = player

    # Check if the player has won
    if check_win(board, player):
      print("Player {} wins!".format(player))
      break

    # Check if the game is a draw
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch to the other player
    player = 3 - player

def check_win(board, player):
  """
  Check if the player has won.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for horizontal wins
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check for vertical wins
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check for diagonal wins
  if np.all(np.diag(board) == player) or np.all(np.diag(np.flip(board, axis=0)) == player):
    return True

  # No win
  return False


if __name__ == "__main__":
  jdv()
