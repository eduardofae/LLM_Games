import numpy as np

def check_winner(board):
  # Check for horizontal wins
  for row in range(3):
    if np.all(board[row] == board[row][0]) and board[row][0] != 0:
      return board[row][0]

  # Check for vertical wins
  for col in range(3):
    if np.all(board[:, col] == board[0, col]) and board[0, col] != 0:
      return board[0, col]

  # Check for diagonal wins
  if np.all(board.diagonal() == board[0, 0]) and board[0, 0] != 0:
    return board[0, 0]
  if np.all(np.flip(board).diagonal() == board[0, 2]) and board[0, 2] != 0:
    return board[0, 2]

  # Check for tie
  if np.all(board != 0):
    return -1

  # No winner yet
  return 0

def play_jdv():
  # Initialize the game board
  board = np.zeros((3, 3), dtype=int)

  # Set the current player to 1
  player = 1

  # Game loop
  while True:
    # Get the player's move
    row, col = map(int, input("Player {}'s turn (row, column): ".format(player)).split())

    # Check if the move is valid
    if board[row, col] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board
    board[row, col] = player

    # Check for a winner or tie
    winner = check_winner(board)
    if winner != 0:
      if winner == -1:
        print("Tie!")
      else:
        print("Player {} wins!".format(winner))
      break

    # Switch to the other player
    player = 3 - player

# Play the game
play_jdv()
