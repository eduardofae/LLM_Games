import numpy as np

def jdv():
  """
  This function implements the jdv game.
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Get the names of the players.
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Set the current player to player 1.
  current_player = 1

  # Play the game until there is a winner or a draw.
  while True:
    # Get the move from the current player.
    move = input(f"{current_player}, where do you want to place your piece? ")

    # Convert the move to a row and column index.
    row, col = map(int, move.split(","))

    # Check if the move is valid.
    if board[row, col] != 0:
      print("Invalid move.")
      continue

    # Place the piece on the board.
    board[row, col] = current_player

    # Check if the current player has won.
    if check_win(board, current_player):
      print(f"{current_player} wins!")
      break

    # Check if there is a draw.
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch the current player.
    current_player = 3 - current_player

def check_win(board, player):
  """
  This function checks if the given player has won the game.
  """

  # Check for a win in each row.
  for row in board:
    if np.all(row == player):
      return True

  # Check for a win in each column.
  for col in board.T:
    if np.all(col == player):
      return True

  # Check for a win in each diagonal.
  if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
    return True

  # No win found.
  return False

if __name__ == "__main__":
  jdv()
