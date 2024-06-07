import numpy as np

def jdv():
  # Create a 3x3 grid
  board = np.zeros((3, 3))

  # Define the players
  players = ['X', 'O']

  # Start the game
  while True:
    # Get the current player
    player = players[0]

    # Get the player's move
    move = input(f"Player {player}, enter your move (row, column): ")
    row, column = [int(x) for x in move.split(',')]

    # Check if the move is valid
    if board[row, column] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board
    board[row, column] = player

    # Check if the player has won
    if check_win(board, player):
      print(f"Player {player} has won!")
      break

    # Check if the game is a draw
    if np.all(board != 0):
      print("The game is a draw.")
      break

    # Switch to the other player
    players = players[1:]

# Function to check if a player has won
def check_win(board, player):
  # Check for horizontal wins
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check for vertical wins
  for column in range(3):
    if np.all(board[:, column] == player):
      return True

  # Check for diagonal wins
  if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
    return True

  # No wins yet
  return False

# Start the game
jdv()
