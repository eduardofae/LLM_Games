import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the current player
current_player = player1_symbol

# Define the game status
game_status = 'ongoing'

# Define the winning combinations
winning_combinations = [
  [(0, 0), (0, 1), (0, 2)],
  [(1, 0), (1, 1), (1, 2)],
  [(2, 0), (2, 1), (2, 2)],
  [(0, 0), (1, 0), (2, 0)],
  [(0, 1), (1, 1), (2, 1)],
  [(0, 2), (1, 2), (2, 2)],
  [(0, 0), (1, 1), (2, 2)],
  [(0, 2), (1, 1), (2, 0)],
]

# Main game loop
while game_status == 'ongoing':

  # Get the player's input
  row = int(input("Enter the row (0-2): "))
  column = int(input("Enter the column (0-2): "))

  # Check if the input is valid
  if row < 0 or row > 2 or column < 0 or column > 2 or board[row, column] != 0:
    print("Invalid input. Please try again.")
    continue

  # Place the player's piece on the board
  board[row, column] = current_player

  # Check if the player has won
  for combination in winning_combinations:
    if all(board[row, column] == current_player for row, column in combination):
      game_status = 'over'
      winner = current_player
      break

  # Check if the game is a draw
  if np.all(board != 0) and game_status == 'ongoing':
    game_status = 'draw'

  # Switch the current player
  if current_player == player1_symbol:
    current_player = player2_symbol
  else:
    current_player = player1_symbol

# Print the game board
print(board)

# Print the game status
if game_status == 'over':
  print(f"The winner is {winner}")
elif game_status == 'draw':
  print("The game is a draw.")
