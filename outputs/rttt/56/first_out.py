import numpy as np

def jdv():
  """
  Plays a game of JDV.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create the game board.
  board = np.zeros((3, 3), dtype=int)

  # Get the names of the players.
  player1_name = input("Player 1, what is your name? ")
  player2_name = input("Player 2, what is your name? ")

  # Set the current player to player 1.
  current_player = 1

  # Play the game until there is a winner or a draw.
  while True:
    # Get the player's move.
    move = get_move(board, current_player)

    # Make the move.
    board[move[0], move[1]] = current_player

    # Check if the player has won.
    if check_win(board, current_player):
      return current_player

    # Check if the game is a draw.
    if is_draw(board):
      return None

    # Switch to the other player.
    current_player = 3 - current_player

def get_move(board, player):
  """
  Gets a move from the player.

  Args:
    board: The current state of the game board.
    player: The player who is making the move.

  Returns:
    The move that the player made.
  """

  # Get the player's input.
  move = input("Player {}, enter your move (row, column): ".format(player))

  # Convert the player's input to a tuple of integers.
  move = tuple(int(x) for x in move.split(","))

  # Check if the move is valid.
  if not is_valid_move(board, move):
    print("Invalid move. Please try again.")
    return get_move(board, player)

  # Return the player's move.
  return move

def is_valid_move(board, move):
  """
  Checks if a move is valid.

  Args:
    board: The current state of the game board.
    move: The move to check.

  Returns:
    True if the move is valid, False otherwise.
  """

  # Check if the move is within the bounds of the board.
  if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
    return False

  # Check if the space is already occupied.
  if board[move[0], move[1]] != 0:
    return False

  # The move is valid.
  return True

def check_win(board, player):
  """
  Checks if a player has won.

  Args:
    board: The current state of the game board.
    player: The player who is checking for a win.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row.
  for row in range(3):
    if board[row, 0] == player and board[row, 1] == player and board[row, 2] == player:
      return True

  # Check for a win in each column.
  for col in range(3):
    if board[0, col] == player and board[1, col] == player and board[2, col] == player:
      return True

  # Check for a win in each diagonal.
  if board[0, 0] == player and board[1, 1] == player and board[2, 2] == player:
    return True
  if board[0, 2] == player and board[1, 1] == player and board[2, 0] == player:
    return True

  # The player has not won.
  return False

def is_draw(board):
  """
  Checks if the game is a draw.

  Args:
    board: The current state of the game board.

  Returns:
    True if the game is a draw, False otherwise.
  """

  # Check if there are any empty spaces on the board.
  for row in range(3):
    for col in range(3):
      if board[row, col] == 0:
        return False

  # The game is a draw.
  return True

if __name__ == "__main__":
  # Play the game.
  winner = jdv()

  # Print the winner.
  if winner is None:
    print("The game is a draw.")
  else:
    print("Player {} wins!".format(winner))
