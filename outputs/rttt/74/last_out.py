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
  current_player = player1_name
  next_player = player2_name

  # Play the game until there is a winner or a draw.
  while True:
    # Get the current player's move.
    try:
      row = int(input(f"{current_player}, enter the row (0-2): "))
      col = int(input(f"{current_player}, enter the column (0-2): "))
    except ValueError:
      print("Invalid input. Please enter a valid row and column.")
      continue

    # Check if the move is valid.
    if not (0 <= row <= 2 and 0 <= col <= 2):
      print("Invalid move. Please enter a valid row and column.")
      continue
    if board[row, col] != '':
      print("Invalid move. Try again.")
      continue

    # Place the current player's piece on the board.
    board[row, col] = 'X' if current_player == player1_name else 'O'

    # Check if there is a winner or a draw.
    winner = check_winner(board)
    if winner is not None:
      if winner == 'draw':
        print("The game is a draw.")
      else:
        print(f"{winner} wins!")
      break

    # Switch turns.
    current_player, next_player = next_player, current_player

  # Ask the user if they want to play again or quit.
  play_again = input("Do you want to play again? (y/n/q): ")
  if play_again == 'y':
    play_game()
  elif play_again == 'q':
    exit()


if __name__ == "__main__":
  play_game()
