import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Create a list of players
players = [1, 2]

# Create a variable to keep track of the current player
current_player = 0

# Create a variable to keep track of the game status
game_status = "ongoing"

# Game loop
while game_status == "ongoing":
  # Get the column where the player wants to place their piece
  column = int(input("Player {}: Enter the column where you want to place your piece (1-10): ".format(players[current_player])))

  # Check if the column is valid
  if column < 1 or column > 10:
    print("Invalid column. Please enter a column between 1 and 10.")
    continue

  # Check if the column is full
  if board[:, column - 1].all():
    print("Column {} is full. Please choose another column.".format(column))
    continue

  # Place the player's piece in the lowest free space of the column
  row = np.where(board[:, column - 1] == 0)[0][-1]
  board[row, column - 1] = players[current_player]

  # Check if the player has won
  if check_win(board, players[current_player]):
    game_status = "won"
    print("Player {} wins!".format(players[current_player]))
  # Check if the game is a draw
  elif board.all():
    game_status = "draw"
    print("The game is a draw.")

  # Switch to the other player
  current_player = (current_player + 1) % 2

# Define the function to check if a player has won
def check_win(board, player):
  # Check for horizontal wins
  for row in range(10):
    if np.all(board[row, :] == player):
      return True

  # Check for vertical wins
  for col in range(10):
    if np.all(board[:, col] == player):
      return True

  # Check for diagonal wins
  for i in range(10):
    # Check for diagonal wins from top left to bottom right
    if np.all(board[i:, i:] == player):
      return True

    # Check for diagonal wins from bottom left to top right
    if np.all(board[:i+1, i:] == player):
      return True

  # No win found
  return False
