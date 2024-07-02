import numpy as np

# Constants
BOARD_SIZE = 3
PLAYER1_SYMBOL = 'X'
PLAYER2_SYMBOL = 'O'

def create_board():
  """Creates a 3x3 board."""
  board = np.zeros((BOARD_SIZE, BOARD_SIZE))
  return board

def print_board(board):
  """Prints the board."""
  print("   0 1 2")
  for i in range(BOARD_SIZE):
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
  for row in range(BOARD_SIZE):
    if np.all(board[row, :] == board[row, 0]) and board[row, 0] != 0:
      return True

  # Check columns
  for col in range(BOARD_SIZE):
    if np.all(board[:, col] == board[0, col]) and board[0, col] != 0:
      return True

  # Check diagonals
  if np.all(board.diagonal() == board[0, 0]) and board[0, 0] != 0:
    return True

  if np.all(np.flip(board).diagonal() == board[0, BOARD_SIZE-1]) and board[0, BOARD_SIZE-1] != 0:
    return True

  return False

def check_draw(board):
  """Checks if the game is a draw."""
  return np.all(board != 0)

def play_game():
  """Plays the game."""
  board = create_board()
  print_board(board)

  player = 1
  while True:
    if player == 1:
      symbol = PLAYER1_SYMBOL
    else:
      symbol = PLAYER2_SYMBOL

    print(f"Player {player}'s turn ({symbol}).")
    
    while True:
      try:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
      except ValueError:
        print("Invalid input. Please enter integers.")
      else:
        if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
          print("Invalid coordinates. Please enter values between 0 and 2.")
        elif board[row, col] != 0:
          print("Invalid move. Space already occupied.")
        else:
          break

    place_piece(board, player, row, col)
    print_board(board)

    if check_win(board):
      print(f"Player {player} wins!")
      break

    if check_draw(board):
      print("Draw!")
      break

    player = 3 - player

if __name__ == "__main__":
  play_game()
