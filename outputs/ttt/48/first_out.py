import numpy as np

def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Get the names of the players.
  player1_name = input("Player 1, enter your name: ")
  player2_name = input("Player 2, enter your name: ")

  # Determine which player goes first.
  player1_turn = True

  # Play the game until there is a winner or a draw.
  while True:
    # Get the player's move.
    if player1_turn:
      row, col = map(int, input("Player 1, enter your move (row, column): ").split())
    else:
      row, col = map(int, input("Player 2, enter your move (row, column): ").split())

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= col < 3 and board[row, col] == 0):
      print("Invalid move.")
      continue

    # Place the player's piece on the board.
    if player1_turn:
      board[row, col] = 1
    else:
      board[row, col] = -1

    # Check if the player has won.
    if abs(board[row, col]) == 3:
      if player1_turn:
        return player1_name
      else:
        return player2_name

    # Check if the game is a draw.
    if np.all(board != 0):
      return None

    # Switch turns.
    player1_turn = not player1_turn

if __name__ == "__main__":
  winner = jdv()
  if winner is None:
    print("The game is a draw.")
  else:
    print(f"{winner} wins!")
