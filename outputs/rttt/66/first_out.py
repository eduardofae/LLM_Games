def jdv():
  """
  Plays a game of JdV.

  Returns:
    The winner of the game.
  """

  # Create the game board.
  board = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]

  # Get the names of the players.
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Set the current player to player 1.
  current_player = player1

  # Keep track of the number of moves that have been made.
  moves = 0

  # Play the game until someone wins or there is a draw.
  while True:
    # Get the player's move.
    move = input("{}'s turn. Enter your move (row, column): ".format(current_player))

    # Split the move into the row and column.
    row, column = move.split(',')

    # Convert the row and column to integers.
    row = int(row)
    column = int(column)

    # Check if the move is valid.
    if not is_valid_move(board, row, column):
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the board.
    board[row][column] = current_player

    # Check if the player has won.
    if has_won(board, current_player):
      print("{} has won!".format(current_player))
      return current_player

    # Check if the game is a draw.
    if moves == 9:
      print("The game is a draw.")
      return None

    # Switch to the other player.
    if current_player == player1:
      current_player = player2
    else:
      current_player = player1

    # Increment the number of moves.
    moves += 1


def is_valid_move(board, row, column):
  """
  Checks if a move is valid.

  Args:
    board: The game board.
    row: The row of the move.
    column: The column of the move.

  Returns:
    True if the move is valid, otherwise False.
  """

  # Check if the row and column are within the bounds of the board.
  if not (0 <= row <= 2 and 0 <= column <= 2):
    return False

  # Check if the space is already occupied.
  if board[row][column] != ' ':
    return False

  return True


def has_won(board, player):
  """
  Checks if a player has won.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, otherwise False.
  """

  # Check for a win in any row.
  for row in board:
    if all(row[i] == player for i in range(3)):
      return True

  # Check for a win in any column.
  for column in range(3):
    if all(board[i][column] == player for i in range(3)):
      return True

  # Check for a win in either diagonal.
  if all(board[i][i] == player for i in range(3)):
    return True
  if all(board[i][2 - i] == player for i in range(3)):
    return True

  return False
