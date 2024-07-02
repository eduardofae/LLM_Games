import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Create a list of the players
players = ['Player 1', 'Player 2']

# Create a variable to keep track of the current player
current_player = 0

# Create a variable to keep track of the game state
game_state = 'ongoing'

# Create a function to check if there is a winner
def check_winner(board):
  # Check for horizontal wins
  for i in range(10):
    for j in range(7):
      if np.all(board[i, j:j+3] == 1) or np.all(board[i, j:j+3] == 2):
        return True

  # Check for vertical wins
  for i in range(7):
    for j in range(10):
      if np.all(board[i:i+3, j] == 1) or np.all(board[i:i+3, j] == 2):
        return True

  # Check for diagonal wins
  for i in range(7):
    for j in range(7):
      if np.all(board[i:i+3, j:j+3] == 1) or np.all(board[i:i+3, j:j+3] == 2):
        return True

  return False

# Create a function to get the lowest free space in a column
def get_lowest_free_space(board, column):
  for i in range(9, -1, -1):
    if board[i, column] == 0:
      return i

  return None

# Create a function to place a piece on the board
def place_piece(board, player, column):
  lowest_free_space = get_lowest_free_space(board, column)
  if lowest_free_space is not None:
    board[lowest_free_space, column] = player

# Create a function to play the game
def play_game():
  # While the game is ongoing
  while game_state == 'ongoing':
    # Get the current player's move
    column = int(input(f'{players[current_player]}, choose a column (0-9): '))

    # Place the piece on the board
    place_piece(board, current_player + 1, column)

    # Check if there is a winner
    if check_winner(board):
      game_state = 'finished'
      print(f'{players[current_player]} wins!')
    else:
      # Check if the board is full
      if np.all(board != 0):
        game_state = 'finished'
        print('Draw!')

      # Switch to the next player
      current_player = (current_player + 1) % 2

# Play the game
play_game()
