import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the players
player1 = 1
player2 = -1

# Main game loop
while True:
  # Display the game board
  print(board)

  # Get the player's move
  move = input("Player {}'s turn: ".format(player1 if player1 == 1 else player2))

  # Check if the move is valid
  if move not in range(1, 11) or board[9, int(move) - 1] != 0:
    print("Invalid move. Please try again.")
    continue

  # Place the player's piece on the board
  board[9, int(move) - 1] = player1 if player1 == 1 else player2

  # Check if the player has won
  if check_win(board, player1) or check_win(board, player2):
    print("Player {} wins!".format(player1 if player1 == 1 else player2))
    break

  # Check if the game is a draw
  if np.all(board != 0):
    print("Draw!")
    break

  # Switch players
  player1, player2 = player2, player1

# Define the function to check if a player has won
def check_win(board, player):
  # Check for horizontal wins
  for i in range(10):
    if np.all(board[i, :] == player):
      return True

  # Check for vertical wins
  for j in range(10):
    if np.all(board[:, j] == player):
      return True

  # Check for diagonal wins
  for i in range(7):
    if np.all(np.diagonal(board[i:i+3, i:i+3]) == player):
      return True

  for i in range(7):
    if np.all(np.diagonal(board[i:i+3, 9-i:6-i]) == player):
      return True

  # No wins found
  return False
