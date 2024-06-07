import random

# Create the game board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Create a list of the players
players = ['X', 'O']

# Create a variable to keep track of the current player
current_player = random.choice(players)

# Create a variable to keep track of the number of moves
moves = 0

# Create a variable to keep track of the game status
game_status = 'ongoing'

# Game loop
while game_status == 'ongoing':
  # Print the game board
  for row in board:
    print(' '.join(row))

  # Get the player's move
  move = input(f"Player {current_player}, enter your move (row, column): ")

  # Split the move into the row and column
  row, column = move.split(',')

  # Convert the row and column to integers
  row = int(row)
  column = int(column)

  # Check if the move is valid
  if board[row][column] == ' ':
    # Place the player's piece on the board
    board[row][column] = current_player

    # Increment the number of moves
    moves += 1

    # Check if the player has won
    if check_win(board, current_player):
      game_status = 'win'
    # Check if the game is a draw
    elif moves == 9:
      game_status = 'draw'
    # Switch to the other player
    else:
      current_player = players[(players.index(current_player) + 1) % 2]
  else:
    print("Invalid move. Please try again.")

# Print the game status
if game_status == 'win':
  print(f"Player {current_player} wins!")
elif game_status == 'draw':
  print("Draw!")

# Define the function to check if a player has won
def check_win(board, player):
  # Check for a win in a row
  for row in board:
    if all(cell == player for cell in row):
      return True

  # Check for a win in a column
  for column in range(3):
    if all(board[row][column] == player for row in range(3)):
      return True

  # Check for a win in a diagonal
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[2][0] == player and board[1][1] == player and board[0][2] == player:
    return True

  # No win
  return False
