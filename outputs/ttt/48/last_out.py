def jdv():
  """
  Plays a game of jdv.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]

  # Get the names of the players.
  player1_name = input("Player 1, enter your name: ")
  player2_name = input("Player 2, enter your name: ")

  # Determine which player goes first.
  player1_turn = True

  # Play the game until there is a winner or a draw.
  while True:
    # Get the player's move.
    if player1_turn:
      move = input(f"{player1_name}, enter your move (row, column): ").split()
    else:
      move = input(f"{player2_name}, enter your move (row, column): ").split()

    # Check if the move is valid.
    if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit() or int(move[0]) < 0 or int(move[0]) > 2 or int(move[1]) < 0 or int(move[1]) > 2 or board[int(move[0])][int(move[1])] != ' ':
      print("Invalid move.")
      continue

    # Place the player's piece on the board.
    if player1_turn:
      board[int(move[0])][int(move[1])] = 'X'
    else:
      board[int(move[0])][int(move[1])] = 'O'

    # Check if the player has won.
    if check_winner(board):
      if player1_turn:
        return player1_name
      else:
        return player2_name

    # Check if the game is a draw.
    if all(all(x != ' ' for x in row) for row in board):
      return None

    # Switch turns.
    player1_turn = not player1_turn

def check_winner(board):
  """
  Checks if there is a winner in the given board.

  Args:
    board: A list of lists representing the game board.

  Returns:
    True if there is a winner, False otherwise.
  """

  # Check for a winner in each row.
  for row in board:
    if all(x == row[0] for x in row) and row[0] != ' ':
      return True

  # Check for a winner in each column.
  for col in range(3):
    if all(board[row][col] == board[0][col] for row in range(3)) and board[0][col] != ' ':
      return True

  # Check for a winner in each diagonal.
  if all(board[row][row] == board[0][0] for row in range(3)) and board[0][0] != ' ':
    return True

  if all(board[row][2-row] == board[0][2] for row in range(3)) and board[0][2] != ' ':
    return True

  # No winner yet.
  return False

if __name__ == "__main__":
  winner = jdv()
  if winner is None:
    print("The game is a draw.")
  else:
    print(f"{winner} wins!")
