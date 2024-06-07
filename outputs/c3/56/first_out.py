import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the player symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Keep track of whose turn it is
player1_turn = True

# Keep track of the number of moves made
num_moves = 0

# Main game loop
while num_moves < 100:
  # Get the player's move
  if player1_turn:
    column = int(input("Player 1, choose a column (0-9): "))
  else:
    column = int(input("Player 2, choose a column (0-9): "))

  # Check if the column is valid
  if column < 0 or column > 9:
    print("Invalid column. Please choose a column between 0 and 9.")
    continue

  # Check if the column is full
  if board[9, column] != 0:
    print("Column is full. Please choose another column.")
    continue

  # Place the player's piece in the column
  for i in range(9, -1, -1):
    if board[i, column] == 0:
      board[i, column] = player1_symbol if player1_turn else player2_symbol
      num_moves += 1
      break

  # Check if the player has won
  if check_win(board, player1_symbol if player1_turn else player2_symbol):
    print(f"Player {1 if player1_turn else 2} wins!")
    break

  # Switch turns
  player1_turn = not player1_turn

# Check if the game is a draw
if num_moves == 100:
  print("Draw!")

# Define the function to check for a win
def check_win(board, symbol):
  # Check for a horizontal win
  for row in range(10):
    if all(board[row, i] == symbol for i in range(10)):
      return True

  # Check for a vertical win
  for col in range(10):
    if all(board[i, col] == symbol for i in range(10)):
      return True

  # Check for a diagonal win
  for row in range(10):
    for col in range(10):
      if row + 2 < 10 and col + 2 < 10 and board[row, col] == symbol and board[row + 1, col + 1] == symbol and board[row + 2, col + 2] == symbol:
        return True
      if row - 2 >= 0 and col + 2 < 10 and board[row, col] == symbol and board[row - 1, col + 1] == symbol and board[row - 2, col + 2] == symbol:
        return True
      if row + 2 < 10 and col - 2 >= 0 and board[row, col] == symbol and board[row + 1, col - 1] == symbol and board[row + 2, col - 2] == symbol:
        return True
      if row - 2 >= 0 and col - 2 >= 0 and board[row, col] == symbol and board[row - 1, col - 1] == symbol and board[row - 2, col - 2] == symbol:
        return True

  # No win found
  return False
