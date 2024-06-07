import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Create the players
players = [1, 2]

# Create a variable to keep track of the current player
current_player = 0

# Create a variable to keep track of the game status
game_status = "ongoing"

# Game loop
while game_status == "ongoing":
  # Get the column where the player wants to place their piece
  column = int(input(f"Player {players[current_player]}, choose a column (0-9): "))

  # Check if the column is valid
  if column < 0 or column > 9:
    print("Invalid column. Please choose a column between 0 and 9.")
    continue

  # Check if the column is full
  if board[9, column] != 0:
    print("This column is full. Please choose another column.")
    continue

  # Place the player's piece in the column
  for i in range(9, -1, -1):
    if board[i, column] == 0:
      board[i, column] = players[current_player]
      break

  # Check if the player has won
  if check_win(board, players[current_player]):
    game_status = "won"
    print(f"Player {players[current_player]} wins!")
    break

  # Check if the game is a draw
  if np.all(board != 0):
    game_status = "draw"
    print("The game is a draw!")
    break

  # Switch to the other player
  current_player = (current_player + 1) % 2

# Print the final game board
print(board)

# Function to check if a player has won
def check_win(board, player):
  # Check for horizontal wins
  for i in range(10):
    for j in range(7):
      if board[i, j] == player and board[i, j+1] == player and board[i, j+2] == player:
        return True

  # Check for vertical wins
  for i in range(7):
    for j in range(10):
      if board[i, j] == player and board[i+1, j] == player and board[i+2, j] == player:
        return True

  # Check for diagonal wins
  for i in range(7):
    for j in range(7):
      if board[i, j] == player and board[i+1, j+1] == player and board[i+2, j+2] == player:
        return True

      if board[i, j+2] == player and board[i+1, j+1] == player and board[i+2, j] == player:
        return True

  # No win found
  return False
