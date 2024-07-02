import numpy as np

# Define the game board
board = np.zeros((3, 3))

# Define the players
players = ['X', 'O']

# Define the game status
game_over = False
winner = None

# Get the player's input
def get_player_input(player):
  """Get the player's input.

  Args:
    player: The current player.

  Returns:
    A tuple of the row and column of the player's move.
  """
  while True:
    try:
      row = int(input(f"Player {player}, enter the row (1-3): "))
      col = int(input(f"Player {player}, enter the column (1-3): "))
      if row not in range(1, 4) or col not in range(1, 4):
        raise ValueError
      if board[row-1][col-1] != 0:
        raise ValueError
      return row-1, col-1
    except ValueError:
      print("Invalid input. Please enter a valid row and column.")

# Check if the game is over
def check_game_over():
  """Check if the game is over.

  Updates the `game_over` and `winner` variables accordingly.
  """
  global game_over, winner

  # Check for a win
  for i in range(3):
    if np.all(board[i] == board[i][0]) and board[i][0] != 0:
      game_over = True
      winner = board[i][0]
    if np.all(board[:, i] == board[0][i]) and board[0][i] != 0:
      game_over = True
      winner = board[0][i]

  if np.all(board.diagonal() == board[0][0]) and board[0][0] != 0:
    game_over = True
    winner = board[0][0]
  if np.all(np.flip(board).diagonal() == board[0][2]) and board[0][2] != 0:
    game_over = True
    winner = board[0][2]

  # Check for a draw
  if np.all(board != 0) and winner is None:
    game_over = True

# Play the game
while not game_over:
  for player in players:
    # Get the player's input
    row, col = get_player_input(player)

    # Place the player's piece on the board
    board[row][col] = player

    # Check if the game is over
    check_game_over()

    # Print the board
    print(board)

    # Print the current player's turn
    print(f"Current player: {player}")

    # Check if the player has won
    if winner is not None:
      print(f"Player {winner} has won!")
      break

# Print the final board
print(board)

# Print the game status
if winner is None:
  print("The game is a draw.")
