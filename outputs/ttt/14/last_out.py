import numpy as np

def jdv(size=3, board_type='square'):
  # Check if the board type is valid
  if board_type not in ['square', 'hexagonal']:
    raise ValueError("Invalid board type.")

  # Initialize the game board
  if board_type == 'square':
    board = np.zeros((size, size))
  elif board_type == 'hexagonal':
    board = np.zeros((size, 2*size - 1))

  # Initialize the player turn
  player = 1

  # Initialize the number of moves
  num_moves = 0

  # Game loop
  while True:
    # Print the game board
    print(board)

    # Get the player's move
    move = input("Player {}'s turn (row, col) (or 'q' to quit or 'r' to restart): ".format(player))

    # Check if the user wants to quit
    if move == 'q':
      break

    # Check if the user wants to restart
    if move == 'r':
      jdv(size, board_type)

    # Check if the move is valid
    try:
      if board_type == 'square':
        row, col = map(int, move.split())
        if board[row, col] != 0:
          print("Invalid move. Please try again.")
          continue
      elif board_type == 'hexagonal':
        row, col = map(int, move.split())
        if row >= size or col >= 2*size - 1 or (row + col) % 2 == 1:
          print("Invalid move. Please try again.")
          continue
    except ValueError:
      print("Invalid input. Please try again.")
      continue

    # Place the player's piece on the board
    board[row, col] = player

    # Increment the number of moves
    num_moves += 1

    # Check if the player has won
    if check_win(board, player, board_type):
      print("Player {} wins!".format(player))
      break

    # Check if the game is a draw
    if num_moves == size**2:
      print("Draw!")
      break

    # Switch to the other player
    player = 3 - player

def check_win(board, player, board_type):
  # Check for a horizontal win
  if board_type == 'square':
    for row in range(board.shape[0]):
      if np.all(board[row, :] == player):
        return True
  elif board_type == 'hexagonal':
    for row in range(board.shape[0]):
      for col in range(board.shape[1] - 1):
        if board[row, col] == player and board[row, col + 1] == player:
          return True

  # Check for a vertical win
  if board_type == 'square':
    for col in range(board.shape[1]):
      if np.all(board[:, col] == player):
        return True
  elif board_type == 'hexagonal':
    for col in range(board.shape[1]):
      for row in range(board.shape[0] - 1):
        if board[row, col] == player and board[row + 1, col] == player:
          return True

  # Check for a diagonal win
  if board_type == 'square':
    if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
      return True
  elif board_type == 'hexagonal':
    # Check for diagonals from the top-left to the bottom-right
    for row in range(board.shape[0] - 1):
      for col in range(board.shape[1] - 1):
        if board[row, col] == player and board[row + 1, col + 1] == player:
          return True

    # Check for diagonals from the bottom-left to the top-right
    for row in range(1, board.shape[0]):
      for col in range(board.shape[1] - 1):
        if board[row, col] == player and board[row - 1, col + 1] == player:
          return True

  # No win yet
  return False

if __name__ == "__main__":
  # Get the size of the game board from the user
  size = int(input("Enter the size of the game board (default is 3): "))

  # Get the type of game board from the user
  board_type = input("Enter the type of game board (square or hexagonal): ")

  # Start the game
  jdv(size, board_type)
