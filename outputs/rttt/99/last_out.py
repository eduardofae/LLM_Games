import numpy as np

def jdv():
  """
  Plays the jdv game.

  Parameters
  ----------
  None

  Returns
  -------
  None

  Raises
  ------
  None
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Get the player names.
  player1_name = input("Player 1, what is your name? ")
  player2_name = input("Player 2, what is your name? ")

  # Set the current player to player 1.
  current_player = 1

  # Set the game over flag to False.
  game_over = False

  # Play the game until the game is over.
  while not game_over:

    # Get the move from the current player.
    while True:
      try:
        move = input(f"{player1_name if current_player == 1 else player2_name}, where do you want to place your piece? ")

        # Convert the move to a row and column index.
        row, col = map(int, move.split(","))

        # Check if the move is valid.
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row, col] != 0:
          print("Invalid move. Please enter an empty space.")
          continue
      except ValueError:
        print("Invalid move. Please enter a valid row and column index (e.g., 0,0).")
        continue

      # Place the piece on the board.
      board[row, col] = current_player
      break

    # Draw the game board.
    print("-" * 13)
    for row in board:
      print("| " + " | ".join(["O" if cell == 1 else "X" if cell == 2 else " " for cell in row]) + " |")
    print("-" * 13)

    # Check if the current player has won.
    if check_win(board, current_player):
      print(f"{player1_name if current_player == 1 else player2_name} wins!")
      game_over = True
      break

    # Check if there is a draw.
    if np.all(board != 0):
      print("Draw!")
      game_over = True
      break

    # Switch the current player.
    current_player = 3 - current_player

def check_win(board, player):
  """
  Checks if the given player has won the jdv game.

  Parameters
  ----------
  board : numpy.ndarray
    The game board as a 3x3 NumPy array.
  player : int
    The player to check for a win (1 or 2).

  Returns
  -------
  bool
    True if the player has won, False otherwise.

  Raises
  ------
  None
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
  while True:
    jdv()
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
      break
