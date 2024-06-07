import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Define the players
player1 = 'X'
player2 = 'O'

# Define the current player
current_player = player1

# Game loop
while True:
  # Print the game board
  print(board)

  # Get the player's move
  row = int(input("Enter the row (0-2): "))
  col = int(input("Enter the column (0-2): "))

  # Check if the move is valid
  if board[row, col] == 0:
    # Place the player's piece on the board
    board[row, col] = current_player

    # Check if the player has won
    if check_win(board, current_player):
      print(f"{current_player} wins!")
      break
  else:
    print("Invalid move. Try again.")

  # Switch the current player
  if current_player == player1:
    current_player = player2
  else:
    current_player = player1

# Check if the board is full
if np.all(board != 0):
  print("Draw!")

# Define the function to check if a player has won
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
  if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
    return True

  # Otherwise, return False
  return False
