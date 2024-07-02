import numpy as np

def create_board():
  """Creates a 3x3 board filled with empty spaces."""
  board = np.empty((3, 3), dtype=str)
  board[:] = ''
  return board

def print_board(board):
  """Prints the board to the console."""
  for row in board:
    for cell in row:
      print(cell, end=' ')
    print()

def get_player_input(player):
  """Gets the player's input for the next move."""
  while True:
    try:
      row, col = map(int, input(f"Player {player}, enter row and column (e.g. 1 2): ").split())
      if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid input. Row and column must be between 1 and 3.")
      elif board[row-1][col-1] != '':
        print("That space is already occupied.")
      else:
        return row-1, col-1
    except ValueError:
      print("Invalid input. Please enter two integers separated by a space.")

def check_winner(board):
  """Checks if there is a winner."""
  # Check rows
  for row in board:
    if len(set(row)) == 1 and row[0] != '':
      return row[0]

  # Check columns
  for col in range(3):
    if len(set(board[:, col])) == 1 and board[0][col] != '':
      return board[0][col]

  # Check diagonals
  if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != '':
    return board[0][0]
  if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != '':
    return board[0][2]

  # Check draw
  if np.all(board != ''):
    return 'draw'

  # No winner yet
  return None

# Main game loop
board = create_board()
player = 1

while True:
  print_board(board)
  row, col = get_player_input(player)
  board[row][col] = 'X' if player == 1 else 'O'
  winner = check_winner(board)
  if winner:
    if winner == 'draw':
      print("It's a draw!")
    else:
      print(f"Player {player} wins!")
    break
  player = 2 if player == 1 else 1
