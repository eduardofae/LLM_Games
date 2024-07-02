import numpy as np

# Create the game board
board = np.zeros((10, 10), dtype=int)

# Create a list of the players
players = ['X', 'O']

# Set the current player to the first player
current_player = 0

# Set the game state to not finished
game_state = 'not finished'

# Main game loop
while game_state == 'not finished':
  # Get the player's move
  move = input("Player {}'s turn. Enter a column (1-10): ".format(players[current_player]))

  # Check if the move is valid
  if move not in range(1, 11) or board[9, move - 1] != 0:
    print("Invalid move. Please enter a valid column.")
    continue

  # Place the player's piece on the board
  for i in range(9, -1, -1):
    if board[i, move - 1] == 0:
      board[i, move - 1] = players[current_player]
      break

  # Check if the player has won
  if check_win(board, players[current_player]):
    game_state = 'win'
    print("Player {} wins!".format(players[current_player]))

  # Check if the game is a draw
  elif np.all(board != 0):
    game_state = 'draw'
    print("The game is a draw.")

  # Switch to the other player
  current_player = (current_player + 1) % 2

# Print the final game board
print(board)

