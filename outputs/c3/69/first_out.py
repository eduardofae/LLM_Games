
import numpy as np

def create_board():
  """Creates a 10x10 numpy array to represent the game board."""
  board = np.zeros((10, 10))
  return board

def place_piece(board, player, col):
  """Places a piece for the given player in the lowest free space of the given column."""
  for i in range(9, -1, -1):
    if board[i][col] == 0:
      board[i][col] = player
      return

def check_win(board, player):
  """Checks if the given player has won the game."""
  # Check for horizontal wins
  for i in range(10):
    if np.all(board[i] == player):
      return True

  # Check for vertical wins
  for j in range(10):
    if np.all(board[:, j] == player):
      return True

  # Check for diagonal wins
  for i in range(7):
    for j in range(7):
      if np.all(board[i:i+3, j:j+3] == player):
        return True

  # Check for diagonal wins in the other direction
  for i in range(7):
    for j in range(2, 10):
      if np.all(board[i:i+3, j:j-3:-1] == player):
        return True

  return False

def play_game():
  """Plays the game of pong."""
  board = create_board()
  player1 = 1
  player2 = 2
  current_player = player1
  while True:
    # Get the column where the player wants to place their piece
    try:
      col = int(input("Player {}'s turn. Enter a column number (0-9): ".format(current_player)))
    except ValueError:
      print("Invalid input. Please enter a number between 0 and 9.")
      continue

    # Check if the column is valid
    if col < 0 or col > 9:
      print("Invalid column. Please enter a number between 0 and 9.")
      continue

    # Place the piece
    place_piece(board, current_player, col)

    # Check if the player has won
    if check_win(board, current_player):
      print("Player {} wins!".format(current_player))
      break

    # Check if the game is a draw
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch to the other player
    current_player = player1 if current_player == player2 else player2

# Play the game
play_game()
