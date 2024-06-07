def check_winner(board):
  """
  Checks if there is a winner in the given board.

  Args:
    board: A 3x3 list of strings representing the game board.

  Returns:
    The winner, or None if there is no winner yet.
  """

  # Check for horizontal wins.
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != " ":
      return row[0]

  # Check for vertical wins.
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
      return board[0][col]

  # Check for diagonal wins.
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
    return board[0][2]

  # No winner yet.
  return None


def play_jdv():
  """
  Plays a game of jdv.
  """

  # Create a new game board.
  board = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

  # Get the player names.
  player1 = input("Enter the name of player 1: ")
  player2 = input("Enter the name of player 2: ")

  # Set the current player to player 1.
  current_player = player1

  # Play the game until there is a winner or a draw.
  while True:
    # Get the player's move.
    row = int(input(f"{current_player}, enter the row (1-3): ")) - 1
    col = int(input(f"{current_player}, enter the column (1-3): ")) - 1

    # Check if the move is valid.
    if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the board.
    board[row][col] = current_player

    # Check if there is a winner.
    winner = check_winner(board)
    if winner is not None:
      print(f"{winner} wins!")
      break

    # Check if the game is a draw.
    if all(all(x != " " for x in row) for row in board):
      print("Draw!")
      break

    # Switch the current player.
    current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
  play_jdv()
