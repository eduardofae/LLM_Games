import numpy as np

def create_board():
  """Creates a 3x3 board."""
  board = np.zeros((3, 3))
  return board

def print_board(board):
  """Prints the board."""
  print("   0 1 2")
  for i in range(3):
    print(i, board[i, :])

def place_piece(board, player, row, col):
  """Places a piece on the board."""
  if board[row, col] == 0:
    board[row, col] = player
  else:
    print("Invalid move. Space already occupied.")

def check_win(board):
  """Checks if there is a winner."""
  # Check rows
  for row in range(3):
    if np.all(board[row, :] == board[row, 0]) and board[row, 0] != 0:
      return True

  # Check columns
  for col in range(3):
    if np.all(board[:, col] == board[0, col]) and board[0, col] != 0:
      return True

  # Check diagonals
  if np.all(board.diagonal() == board[0, 0]) and board[0, 0] != 0:
    return True

  if np.all(np.flip(board).diagonal() == board[0, 2]) and board[0, 2] != 0:
    return True

  return False

def play_game():
  """Plays the game."""
  board = create_board()
  print_board(board)

  player = 1
  while True:
    print(f"Player {player}'s turn.")
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))

    place_piece(board, player, row, col)
    print_board(board)

    if check_win(board):
      print(f"Player {player} wins!")
      break

    if np.all(board != 0):
      print("Draw!")
      break

    player = 3 - player

if __name__ == "__main__":
  play_game()
