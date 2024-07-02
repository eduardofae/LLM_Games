import numpy as np

def check_winner(jdv_board):
  """
  Checks if there is a winner in the game.

  Args:
    jdv_board: A 3x3 numpy array representing the game board.

  Returns:
    The winner of the game, or None if there is no winner yet.
  """

  # Check if the input is a 3x3 numpy array.
  if not isinstance(jdv_board, np.ndarray) or jdv_board.shape != (3, 3):
    raise ValueError("The input must be a 3x3 numpy array.")

  # Check for horizontal wins.
  for row in jdv_board:
    if all(row == row[0]) and row[0] != 0:
      return row[0]

  # Check for vertical wins.
  for col in jdv_board.T:
    if all(col == col[0]) and col[0] != 0:
      return col[0]

  # Check for diagonal wins.
  if all(jdv_board.diagonal() == jdv_board.diagonal()[0]) and jdv_board.diagonal()[0] != 0:
    return jdv_board.diagonal()[0]
  if all(np.flip(jdv_board).diagonal() == np.flip(jdv_board).diagonal()[0]) and np.flip(jdv_board).diagonal()[0] != 0:
    return np.flip(jdv_board).diagonal()[0]

  # Check for a draw.
  if all(jdv_board.flatten() != 0):
    return 0

  # No winner yet.
  return None

def play_game():
  """
  Plays a game of jdv.
  """

  # Create the game board.
  jdv_board = np.zeros((3, 3), dtype=int)

  # Get the player names.
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")

  # Determine who goes first.
  player1_turn = True

  # Play the game.
  while True:
    # Get the player's move.
    if player1_turn:
      try:
        row = int(input(f"{player1_name}, choose a row (1-3): ")) - 1
        col = int(input(f"{player1_name}, choose a column (1-3): ")) - 1
      except ValueError:
        print("Invalid move. Please enter an integer between 1 and 3.")
        continue
    else:
      try:
        row = int(input(f"{player2_name}, choose a row (1-3): ")) - 1
        col = int(input(f"{player2_name}, choose a column (1-3): ")) - 1
      except ValueError:
        print("Invalid move. Please enter an integer between 1 and 3.")
        continue

    # Check for invalid moves.
    if row < 0 or row > 2 or col < 0 or col > 2:
      print("Invalid move. Please choose a row and column between 1 and 3.")
      continue
    if jdv_board[row, col] != 0:
      print("That space is already occupied. Please choose another space.")
      continue

    # Place the player's piece on the board.
    jdv_board[row, col] = 1 if player1_turn else 2

    # Check for a winner.
    winner = check_winner(jdv_board)
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

  # Ask if the players want to play again.
  play_again = input("Do you want to play again? (y/n): ")
  if play_again == "y":
    play_game()
  else:
    print("Thanks for playing!")

if __name__ == "__main__":
  play_game()
