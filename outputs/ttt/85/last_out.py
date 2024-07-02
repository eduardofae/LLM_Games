import numpy as np

# Create the game board
game_board = np.zeros((3, 3))

# Define the players
player1 = 'X'
player2 = 'O'

# Define the current player
current_player_symbol = player1

# Define the number of moves that have been made
num_moves = 0

# Game loop
while True:
  # Print the game board
  print(game_board)

  # Get the player's move
  if current_player_symbol == player1:
    row = int(input("Player 1, enter the row (0-2): "))
    col = int(input("Player 1, enter the column (0-2): "))
  else:
    row = int(input("Player 2, enter the row (0-2): "))
    col = int(input("Player 2, enter the column (0-2): "))

  # Check if the move is valid
  if game_board[row, col] == 0:
    # Place the player's piece on the board
    game_board[row, col] = current_player_symbol

    # Increment the number of moves
    num_moves += 1

    # Check if the player has won
    if check_win(game_board, current_player_symbol):
      print(f"{current_player_symbol} wins!")
      break
  else:
    print("Invalid move. Try again.")

  # Switch the current player
  if current_player_symbol == player1:
    current_player_symbol = player2
  else:
    current_player_symbol = player1

# Check if the board is full
if num_moves == 9:
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

# Define the function to reset the game
def reset_game():
  # Reset the game board
  game_board[:] = 0

  # Reset the current player
  current_player_symbol = player1

  # Reset the number of moves
  num_moves = 0

# Ask the user if they want to reset the game
while True:
  answer = input("Do you want to reset the game? (y/n) ")
  if answer == 'y':
    reset_game()
  elif answer == 'n':
    break
  else:
    print("Invalid input. Please enter 'y' or 'n'.")
