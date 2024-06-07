import numpy as np

def jdv():
  """
  This function implements the jdv game.

  The game is played on a 3x3 grid. Two players take turns placing their pieces in a free space of the grid.
  The first player to make a line of 3 (horizontally, vertically or diagonally) adjacent pieces wins.
  If there are no more free spaces, the game is declared a draw.

  The function returns the winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Create a list of the possible winning lines.
  winning_lines = [
      [(0, 0), (0, 1), (0, 2)],
      [(1, 0), (1, 1), (1, 2)],
      [(2, 0), (2, 1), (2, 2)],
      [(0, 0), (1, 0), (2, 0)],
      [(0, 1), (1, 1), (2, 1)],
      [(0, 2), (1, 2), (2, 2)],
      [(0, 0), (1, 1), (2, 2)],
      [(0, 2), (1, 1), (2, 0)],
  ]

  # Get the player's names.
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")

  # Set the current player to player 1.
  current_player = 1

  # Loop until the game is over.
  while True:
    # Get the current player's move.
    move = input(f"{player1_name}'s turn (row, column): ")

    # Check if the move is valid.
    if not move or len(move.split(",")) != 2:
      print("Invalid move. Please enter a row and column number separated by a comma.")
      continue

    row, column = map(int, move.split(","))
    if row < 0 or row > 2 or column < 0 or column > 2 or board[row, column] != 0:
      print("Invalid move. Please enter a free space.")
      continue

    # Place the current player's piece on the board.
    board[row, column] = current_player

    # Check if the current player has won.
    for winning_line in winning_lines:
      if all(board[x, y] == current_player for x, y in winning_line):
        return player1_name if current_player == 1 else player2_name

    # Check if the game is a draw.
    if all(board.flatten() != 0):
      return None

    # Switch to the other player.
    current_player = 3 - current_player

if __name__ == "__main__":
  winner = jdv()
  if winner is None:
    print("The game is a draw.")
  else:
    print(f"{winner} wins!")
