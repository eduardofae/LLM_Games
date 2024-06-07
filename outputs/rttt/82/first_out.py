import numpy as np

def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if it is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Get the names of the players.
  player1_name = input("Player 1, enter your name: ")
  player2_name = input("Player 2, enter your name: ")

  # Set the current player to player 1.
  current_player = player1_name

  # Play the game until there is a winner or a draw.
  while True:
    # Get the player's move.
    row, col = map(int, input(f"{current_player}, enter your move (row, col): ").split())

    # Place the player's piece on the board.
    board[row, col] = 1 if current_player == player1_name else -1

    # Check if the player has won.
    if abs(board[row, :]).sum() == 3 or abs(board[:, col]).sum() == 3:
      winner = player1_name if current_player == player2_name else player2_name
      return winner

    # Check if the player has won diagonally.
    if abs(board.diagonal()).sum() == 3 or abs(np.flip(board, axis=0).diagonal()).sum() == 3:
      winner = player1_name if current_player == player2_name else player2_name
      return winner

    # Check if the game is a draw.
    if np.all(board != 0):
      return None

    # Switch the current player.
    current_player = player2_name if current_player == player1_name else player1_name

# Play the game.
winner = jdv()

# Print the winner.
if winner is None:
  print("The game is a draw.")
else:
  print(f"{winner} wins!")
