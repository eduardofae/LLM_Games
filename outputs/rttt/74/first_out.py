import numpy as np

def check_winner(board):
  """
  Checks if there is a winner in the game.

  Args:
    board: A 3x3 numpy array representing the game board.

  Returns:
    The winner, which can be 'X', 'O', or 'draw'.
  """

  # Check for horizontal wins.
  for row in range(3):
    if np.all(board[row, :] == 'X'):
      return 'X'
    elif np.all(board[row, :] == 'O'):
      return 'O'

  # Check for vertical wins.
  for col in range(3):
    if np.all(board[:, col] == 'X'):
      return 'X'
    elif np.all(board[:, col] == 'O'):
      return 'O'

  # Check for diagonal wins.
  if np.all(np.diag(board) == 'X'):
    return 'X'
  elif np.all(np.diag(board) == 'O'):
    return 'O'

  if np.all(board[:, ::-1] == 'X'):
    return 'X'
  elif np.all(board[:, ::-1] == 'O'):
    return 'O'

  # If there are no winners, check for a draw.
  if np.all(board != ''):
    return 'draw'

  return None


def play_game():
  """
  Plays a game of jdv.
  """

  # Initialize the game board.
  board = np.empty((3, 3), dtype=str)
  board[:] = ''

  # Get the names of the two players.
  player1_name = input("Enter the name of player 1: ")
  player2_name = input("Enter the name of player 2: ")

  # Determine who goes first.
  player1_turn = True

  # Play the game until there is a winner or a draw.
  while True:
    # Get the player's move.
    if player1_turn:
      player = player1_name
      symbol = 'X'
    else:
      player = player2_name
      symbol = 'O'

    row = int(input(f"{player}, enter the row (0-2): "))
    col = int(input(f"{player}, enter the column (0-2): "))

    # Check if the move is valid.
    if board[row, col] != '':
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the board.
    board[row, col] = symbol

    # Check if there is a winner or a draw.
    winner = check_winner(board)
    if winner is not None:
      if winner == 'draw':
        print("The game is a draw.")
      else:
        print(f"{winner} wins!")
      break

    # Switch turns.
    player1_turn = not player1_turn


if __name__ == "__main__":
  play_game()
