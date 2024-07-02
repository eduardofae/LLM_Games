import numpy as np

def jdv():
  # Create the game board
  board = np.zeros((3, 3))

  # Set the player turn to 1 (X)
  player = 1

  # Set the game state to ongoing
  game_state = "ongoing"

  # Main game loop
  while game_state == "ongoing":
    # Get the player's move
    move = input("Player {}'s turn: ".format(player))
    row, col = map(int, move.split())

    # Check if the move is valid
    if board[row, col] != 0:
      print("Invalid move. Please choose an empty space.")
      continue

    # Place the player's piece on the board
    board[row, col] = player

    # Check if the player has won
    if check_win(board, player):
      game_state = "won"
      print("Player {} wins!".format(player))
      break

    # Check if the game is a draw
    if np.all(board != 0):
      game_state = "draw"
      print("The game is a draw.")
      break

    # Switch the player turn
    player = 3 - player

# Function to check if a player has won
def check_win(board, player):
  # Check the rows
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check the columns
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check the diagonals
  if np.all(board.diagonal() == player):
    return True
  if np.all(np.flipud(board).diagonal() == player):
    return True

  # No winning combination found
  return False

# Play the game
jdv()
