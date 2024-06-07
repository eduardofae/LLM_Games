import random

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

  # Get the players' names and the characters they want to use.
  player1 = input("Player 1, what is your name? ")
  player1_character = input("Player 1, what character do you want to use? ")
  player2 = input("Player 2, what is your name? ")
  player2_character = input("Player 2, what character do you want to use? ")

  # Set the current player to player 1.
  current_player = player1

  # Keep track of the number of moves that have been made.
  num_moves = 0

  # Keep track of the number of wins for each player.
  player1_wins = 0
  player2_wins = 0

  # Play the game until someone wins or there is a draw.
  while True:
    # Print the game board.
    print_board(board)

    # Get the player's move.
    if current_player == player1:
      move = input("{}'s turn. Enter your move (row, column): ".format(current_player))
    else:
      move = get_computer_move(board)

    # Split the move into the row and column.
    try:
      row, column = map(int, move.split(','))
    except ValueError:
      print("Invalid move. Try again.")
      continue

    # Check if the move is valid.
    if not is_valid_move(board, row, column):
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the board.
    board[row][column] = current_player

    # Increment the number of moves.
    num_moves += 1

    # Check if the player has won.
    if has_won(board, current_player):
      print("{} has won!".format(current_player))
      if current_player == player1:
        player1_wins += 1
      else:
        player2_wins += 1
      return current_player

    # Check if the game is a draw.
    if is_draw(board):
      print("The game is a draw.")
      return None

    # Switch to the other player.
    if current_player == player1:
      current_player = player2
    else:
      current_player = player1


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


def is_draw(board):
  """
  Checks if the game is a draw.

  Args:
    board: The game board.

  Returns:
    True if the game is a draw, otherwise False.
  """

  # Check if all the spaces on the board are occupied.
  if all(all(space != ' ' for space in row) for row in board):
    return True

  return False


def print_board(board):
  """
  Prints the game board to the console.

  Args:
    board: The game board.
  """

  for row in board:
    print(' '.join(row))


def get_computer_move(board):
  """
  Gets a move for the computer player.

  Args:
    board: The game board.

  Returns:
    A move in the form of a string (row, column).
  """

  # Get all the possible moves.
  possible_moves = []
  for row in range(3):
    for column in range(3):
      if board[row][column] == ' ':
        possible_moves.append((row, column))

  # Choose a random move.
  move = random.choice(possible_moves)

  # Return the move as a string.
  return '{},{