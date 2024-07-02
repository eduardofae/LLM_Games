def jdv():
  """
  A simple game of tic-tac-toe.

  The game is played on a 3x3 grid. Players take turns placing their pieces in a free space.
  The first player to make a line of three of their pieces wins. If there are no more free spaces, the game is declared a draw.
  """

  # Create a game board.
  board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

  # Create a list of player symbols.
  players = ["X", "O"]

  # Keep track of the current player.
  current_player = 0

  # Keep track of the number of moves made.
  moves = 0

  # Game loop.
  while True:
    # Get the player's move.
    row, col = input("Enter your move (row, column): ").split()
    row = int(row) - 1
    col = int(col) - 1

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "):
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board.
    board[row][col] = players[current_player]

    # Check if the player has won.
    if check_win(board, players[current_player]):
      print(f"{players[current_player]} wins!")
      break

    # Check if the game is a draw.
    if moves == 9:
      print("Draw!")
      break

    # Switch to the other player.
    current_player = 1 - current_player

    # Increment the number of moves.
    moves += 1


def check_win(board, player):
  """
  Checks if the player has won.

  Args:
    board: The game board.
    player: The player's symbol.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check if the player has won horizontally.
  for row in board:
    if all(x == player for x in row):
      return True

  # Check if the player has won vertically.
  for col in range(3):
    if all(x == player for x in [board[0][col], board[1][col], board[2][col]]):
      return True

  # Check if the player has won diagonally.
  if all(x == player for x in [board[0][0], board[1][1], board[2][2]]):
    return True
  if all(x == player for x in [board[0][2], board[1][1], board[2][0]]):
    return True

  # The player has not won.
  return False


if __name__ == "__main__":
  jdv()
