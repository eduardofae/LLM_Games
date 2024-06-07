import numpy as np

def jdv():
  """
  Plays a game of JDV (also known as Tic-Tac-Toe).

  The game is played on a 3x3 grid, and two players take turns placing their
  pieces in a free space. The first player to make a line of three adjacent
  pieces wins. If there are no more free spaces, the game is declared a draw.

  Args:
    None

  Returns:
    None
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Create a list of the players.
  players = [1, 2]

  # Keep track of the current player.
  current_player = 0

  # Keep track of the number of moves that have been made.
  num_moves = 0

  # Play the game until someone wins or there are no more moves left.
  while True:
    # Get the player's move.
    move = get_move(board, players[current_player])

    # Place the player's piece on the board.
    board[move[0], move[1]] = players[current_player]

    # Increment the number of moves.
    num_moves += 1

    # Check if the player has won.
    if check_win(board, players[current_player]):
      print(f"Player {players[current_player]} wins!")
      break

    # Check if there are no more moves left.
    if num_moves == 9:
      print("Draw!")
      break

    # Switch to the other player.
    current_player = (current_player + 1) % 2


def get_move(board, player):
  """
  Gets the player's move.

  Args:
    board: The current state of the game board.
    player: The player who is making the move.

  Returns:
    A tuple representing the player's move.
  """

  # Get the player's input.
  while True:
    move = input(f"Player {player}, enter your move (row, column): ")
    try:
      row, column = map(int, move.split(","))
    except ValueError:
      print("Invalid input. Please enter a valid move.")
      continue

    # Check if the move is valid.
    if not is_valid_move(board, row, column):
      print("Invalid move. Please enter a valid move.")
      continue

    # Return the player's move.
    return row, column


def is_valid_move(board, row, column):
  """
  Checks if a move is valid.

  Args:
    board: The current state of the game board.
    row: The row of the move.
    column: The column of the move.

  Returns:
    True if the move is valid, False otherwise.
  """

  # Check if the move is within the bounds of the board.
  if row < 0 or row > 2 or column < 0 or column > 2:
    return False

  # Check if the space is already occupied.
  if board[row, column] != 0:
    return False

  # The move is valid.
  return True


def check_win(board, player):
  """
  Checks if the player has won.

  Args:
    board: The current state of the game board.
    player: The player who is checking for a win.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check the rows.
  for row in range(3):
    if all(board[row, :] == player):
      return True

  # Check the columns.
  for column in range(3):
    if all(board[:, column] == player):
      return True

  # Check the diagonals.
  if all(board.diagonal() == player) or all(np.flip(board).diagonal() == player):
    return True

  # The player has not won.
  return False
