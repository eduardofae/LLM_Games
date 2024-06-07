import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Create a list of player symbols
player_symbols = ["X", "O"]

# Define the game state
game_state = "ongoing"

# Define the current player
current_player = 0

# Define the winning condition
winning_condition = 3

# Game loop
while game_state == "ongoing":
  # Get the player's move
  move = input("Player " + player_symbols[current_player] + ", enter your move (column number): ")

  # Validate the move
  if not move.isdigit() or int(move) < 1 or int(move) > 10 or board[9, int(move) - 1] != 0:
    print("Invalid move. Please enter a valid column number.")
    continue

  # Place the player's piece on the board
  for i in range(9, -1, -1):
    if board[i, int(move) - 1] == 0:
      board[i, int(move) - 1] = current_player + 1
      break

  # Check for a win
  for i in range(10):
    for j in range(10):
      if board[i, j] != 0 and board[i, j] == board[i, (j + 1) % 10] and board[i, j] == board[i, (j + 2) % 10]:
        game_state = "win"
        winner = current_player
      elif board[i, j] != 0 and board[i, j] == board[(i + 1) % 10, j] and board[i, j] == board[(i + 2) % 10, j]:
        game_state = "win"
        winner = current_player
      elif board[i, j] != 0 and board[i, j] == board[(i + 1) % 10, (j + 1) % 10] and board[i, j] == board[(i + 2) % 10, (j + 2) % 10]:
        game_state = "win"
        winner = current_player
      elif board[i, j] != 0 and board[i, j] == board[(i + 1) % 10, (j - 1) % 10] and board[i, j] == board[(i + 2) % 10, (j - 2) % 10]:
        game_state = "win"
        winner = current_player

  # Check for a draw
  if np.all(board != 0):
    game_state = "draw"

  # Switch the current player
  current_player = (current_player + 1) % 2

# Print the game board
print(board)

# Print the game state
if game_state == "win":
  print("Player " + player_symbols[winner] + " wins!")
elif game_state == "draw":
  print("Draw!")
