import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Create a list of players
players = ['X', 'O']

# Create a variable to keep track of the current player
current_player = 0

# Create a variable to keep track of the game status
game_over = False

# Create a function to check if a player has won
def check_win(board, player):
  # Check if the player has won horizontally
  for i in range(3):
    if np.all(board[i] == player):
      return True

  # Check if the player has won vertically
  for j in range(3):
    if np.all(board[:, j] == player):
      return True

  # Check if the player has won diagonally
  if np.all(board.diagonal() == player):
    return True
  if np.all(np.flip(board).diagonal() == player):
    return True

  # If the player has not won, return False
  return False

# Create a function to play the game
def play_game():
  # While the game is not over
  while not game_over:
    # Get the current player's move
    move = input("Player {}'s move: ".format(players[current_player]))

    # Convert the move to a row and column
    row, col = map(int, move.split(','))

    # If the move is valid
    if row >= 0 and row < 3 and col >= 0 and col < 3 and board[row, col] == 0:
      # Place the player's piece on the board
      board[row, col] = players[current_player]

      # Check if the player has won
      if check_win(board, players[current_player]):
        # If the player has won, print the winning message
        print("Player {} wins!".format(players[current_player]))

        # Set the game over variable to True
        game_over = True
    else:
      # If the move is not valid, print an error message
      print("Invalid move. Please try again.")

    # Switch to the other player
    current_player = (current_player + 1) % 2

  # If the game is a draw
  if not game_over:
    # Print the draw message
    print("Draw!")

# Play the game
play_game()
