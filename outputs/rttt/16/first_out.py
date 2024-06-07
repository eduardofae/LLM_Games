import numpy as np

def jdv():
  """
  Plays a game of JDV (Jogo da Velha).

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Get the names of the players.
  player1 = input("Player 1 name: ")
  player2 = input("Player 2 name: ")

  # Keep track of whose turn it is.
  turn = 1

  # Play the game until someone wins or there is a draw.
  while True:
    # Get the player's move.
    if turn == 1:
      move = input(f"{player1}'s move: ")
    else:
      move = input(f"{player2}'s move: ")

    # Convert the move to a row and column.
    row = int(move[0]) - 1
    col = int(move[1]) - 1

    # Check if the move is valid.
    if board[row, col] != 0:
      print("Invalid move.")
      continue

    # Place the player's piece on the board.
    board[row, col] = turn

    # Check if the player has won.
    if check_win(board, turn):
      if turn == 1:
        print(f"{player1} wins!")
        return player1
      else:
        print(f"{player2} wins!")
        return player2

    # Check if there is a draw.
    if np.all(board != 0):
      print("Draw!")
      return None

    # Switch turns.
    turn = 3 - turn

def check_win(board, turn):
  """
  Checks if the given player has won the game.

  Args:
    board: The game board.
    turn: The player's turn.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row.
  for row in range(3):
    if np.all(board[row, :] == turn):
      return True

  # Check for a win in each column.
  for col in range(3):
    if np.all(board[:, col] == turn):
      return True

  # Check for a win in each diagonal.
  if np.all(board.diagonal() == turn):
    return True
  if np.all(np.flip(board).diagonal() == turn):
    return True

  # No win yet.
  return False
