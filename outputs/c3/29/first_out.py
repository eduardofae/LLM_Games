import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the players
players = [1, 2]

# Define the game state
game_over = False
winner = None

# Main game loop
while not game_over:
  # Get the current player
  player = players[0]

  # Get the player's move
  move = input("Player {}'s move: ".format(player))

  # Check if the move is valid
  if move not in range(10):
    print("Invalid move.")
    continue

  # Check if the column is full
  if board[:, move].any():
    print("Column is full.")
    continue

  # Place the player's piece on the board
  board[board[:, move] == 0, move] = player

  # Check if the player has won
  if check_win(board, player):
    winner = player
    game_over = True
    break

  # Check if the game is a draw
  if board.all():
    game_over = True
    break

  # Switch to the other player
  players = players[1:]

# Print the game board
print(board)

# Print the winner
if winner:
  print("Player {} wins!".format(winner))
else:
  print("Draw.")


def check_win(board, player):
  """
  Checks if the player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a horizontal win
  for row in range(10):
    if np.all(board[row, :] == player):
      return True

  # Check for a vertical win
  for col in range(10):
    if np.all(board[:, col] == player):
      return True

  # Check for a diagonal win
  for i in range(10):
    # Check the main diagonal
    if np.all(board[i, :10-i] == player):
      return True

    # Check the secondary diagonal
    if np.all(board[i, i:] == player):
      return True

  return False
