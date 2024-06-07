import numpy as np

def jdv():
  """
  JDV game.

  This is a 2-player game where players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Get the player names.
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")

  # Set the current player to player 1.
  current_player = 1

  # Main game loop.
  while True:
    # Get the player's move.
    row = int(input(f"{player1_name}'s turn. Enter row (1-3): ")) - 1
    col = int(input(f"{player1_name}'s turn. Enter column (1-3): ")) - 1

    # Check if the move is valid.
    if board[row, col] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board.
    board[row, col] = current_player

    # Check if the player has won.
    if check_win(board, current_player):
      print(f"{player1_name} wins!")
      break

    # Check if there are no more free spaces.
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch the current player.
    current_player = 3 - current_player

def check_win(board, player):
  """
  Checks if the given player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for horizontal wins.
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check for vertical wins.
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check for diagonal wins.
  if np.all(board.diagonal() == player):
    return True
  if np.all(np.flip(board).diagonal() == player):
    return True

  # No win found.
  return False

if __name__ == "__main__":
  jdv()
