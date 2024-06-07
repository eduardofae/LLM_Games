import numpy as np

# Create the game board
game_board = np.zeros((10, 10))

# Create the players
players = [1, 2]

# Create a variable to keep track of the current player
current_player = 0

# Create a variable to keep track of the game status
game_status = "ongoing"

# Create a variable to keep track of the score
player_scores = {1: 0, 2: 0}

# Function to print the game board
def print_board(board):
  for row in board:
    for cell in row:
      if cell == 0:
        print(".", end=" ")
      else:
        print(cell, end=" ")
    print()

# Function to get the next move from a player
def get_move(player):
  while True:
    try:
      column = int(input(f"Player {player}, choose a column (0-9): "))
      if column < 0 or column > 9:
        print("Invalid column. Please choose a column between 0 and 9.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a number between 0 and 9.")
  return column

# Function to check if a player has won
def check_win(board, player):
  # Check for horizontal wins
  for i in range(10):
    for j in range(7):
      if board[i, j] == player and board[i, j+1] == player and board[i, j+2] == player and board[i, j+3] == player:
        return True

  # Check for vertical wins
  for i in range(7):
    for j in range(10):
      if board[i, j] == player and board[i+1, j] == player and board[i+2, j] == player and board[i+3, j] == player:
        return True

  # Check for diagonal wins
  for i in range(7):
    for j in range(7):
      if board[i, j] == player and board[i+1, j+1] == player and board[i+2, j+2] == player and board[i+3, j+3] == player:
        return True

      if board[i, j+3] == player and board[i+1, j+2] == player and board[i+2, j+1] == player and board[i+3, j] == player:
        return True

  # No win found
  return False

# Game loop
while game_status == "ongoing":
  # Print the game board
  print_board(game_board)

  # Get the next move from the current player
  column = get_move(players[current_player])

  # Check if the column is full
  if game_board[9, column] != 0:
    print("This column is full. Please choose another column.")
    continue

  # Place the player's piece in the column
  for i in range(9, -1, -1):
    if game_board[i, column] == 0:
      game_board[i, column] = players[current_player]
      break

  # Check if the player has won
  if check_win(game_board, players[current_player]):
    game_status = "won"
    print(f"Player {players[current_player]} wins!")
    player_scores[players[current_player]] += 1
    break

  # Check if the game is a draw
  if np.all(game_board != 0):
    game_status = "draw"
    print("The game is a draw!")
    break

  # Switch to the other player
  current_player = (current_player + 1) % 2

# Print the final game board
print_board(game_board)

# Print the player scores
print("Player scores:")
for player, score in player_scores.items():
  print(f"Player {player}: {score}")

# Ask the players if they want to play again
while True:
  answer = input("Do you want to play again? (y/n) ")
  if answer == "y":
    # Reset the game board and player scores
    game_board = np.zeros((10, 10))
    player_scores = {1: 0, 2: 0}
    game_status = "ongoing"
    current_player = 0
    break
  elif answer == "n":
    break
  else:
    print("Invalid input. Please enter 'y' or 'n'.")
