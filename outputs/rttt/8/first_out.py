
import numpy as np

def check_winner(board):
  """
  Checks if there is a winner in the game.

  Args:
    board: A 3x3 numpy array representing the game board.

  Returns:
    The winner of the game, or None if there is no winner yet.
  """

  # Check for horizontal wins.
  for row in board:
    if all(row == row[0]) and row[0] != 0:
      return row[0]

  # Check for vertical wins.
  for col in board.T:
    if all(col == col[0]) and col[0] != 0:
      return col[0]

  # Check for diagonal wins.
  if all(board.diagonal() == board.diagonal()[0]) and board.diagonal()[0] != 0:
    return board.diagonal()[0]
  if all(np.flip(board).diagonal() == np.flip(board).diagonal()[0]) and np.flip(board).diagonal()[0] != 0:
    return np.flip(board).diagonal()[0]

  # Check for a draw.
  if all(board.flatten() != 0):
    return 0

  # No winner yet.
  return None

def play_game():
  """
  Plays a game of jdv.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Get the player names.
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")

  # Determine who goes first.
  player1_turn = True

  # Play the game.
  while True:
    # Get the player's move.
    if player1_turn:
      row = int(input(f"{player1_name}, choose a row (1-3): ")) - 1
      col = int(input(f"{player1_name}, choose a column (1-3): ")) - 1
    else:
      row = int(input(f"{player2_name}, choose a row (1-3): ")) - 1
      col = int(input(f"{player2_name}, choose a column (1-3): ")) - 1

    # Place the player's piece on the board.
    board[row, col] = 1 if player1_turn else 2

    # Check for a winner.
    winner = check_winner(board)
    if winner is not None:
      if winner == 0:
        print("Draw!")
      else:
        if winner == 1:
          print(f"{player1_name} wins!")
        else:
          print(f"{player2_name} wins!")
      break

    # Switch turns.
    player1_turn = not player1_turn

if __name__ == "__main__":
  play_game()
