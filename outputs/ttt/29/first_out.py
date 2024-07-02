import numpy as np

def jdv():
  """
  This function implements the jdv game.

  Args:
    None

  Returns:
    None
  """

  # Create the game board
  board = np.zeros((3, 3))

  # Create a list of the players
  players = ['X', 'O']

  # Set the current player to the first player
  current_player = players[0]

  # Play the game until there is a winner or a draw
  while True:
    # Get the player's move
    move = input(f"Player {current_player}, choose a row and column (e.g. 1,2): ")

    # Split the move into the row and column
    row, col = map(int, move.split(','))

    # Check if the move is valid
    if board[row - 1, col - 1] != 0:
      print("Invalid move. Please choose a free space.")
      continue

    # Place the player's piece on the board
    board[row - 1, col - 1] = current_player

    # Check if the player has won
    if check_win(board, current_player):
      print(f"Player {current_player} wins!")
      break

    # Check if the game is a draw
    if np.all(board != 0):
      print("It's a draw!")
      break

    # Switch to the other player
    current_player = players[(players.index(current_player) + 1) % 2]

def check_win(board, player):
  """
  This function checks if the player has won the game.

  Args:
    board: The game board
    player: The player to check

  Returns:
    True if the player has won, False otherwise
  """

  # Check if the player has won horizontally
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check if the player has won vertically
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check if the player has won diagonally
  if np.all(board.diagonal() == player):
    return True
  if np.all(np.flip(board).diagonal() == player):
    return True

  # The player has not won
  return False

if __name__ == "__main__":
  jdv()
