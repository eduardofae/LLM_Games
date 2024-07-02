import numpy as np

def print_board(board):
  for row in board:
    print(' '.join(row))

def check_win(board):
  # Check for horizontal wins
  for row in board:
    if len(set(row)) == 1 and row[0] != ' ':
      return row[0]

  # Check for vertical wins
  for col in range(len(board[0])):
    column = [row[col] for row in board]
    if len(set(column)) == 1 and column[0] != ' ':
      return column[0]

  # Check for diagonal wins
  diagonals = [[board[i][i] for i in range(len(board))],
               [board[i][len(board)-i-1] for i in range(len(board))]]
  for diagonal in diagonals:
    if len(set(diagonal)) == 1 and diagonal[0] != ' ':
      return diagonal[0]

  return None

def get_move(player, board):
  while True:
    try:
      move = int(input(f"Player {player}, choose a column (1-{len(board[0])}): "))
      if move < 1 or move > len(board[0]):
        raise ValueError
      col = move - 1
      if board[0][col] != ' ':
        raise ValueError
      return col
    except ValueError:
      print("Invalid input. Please enter a number between 1 and", len(board[0]))

def main():
  # Create a 10x10 board
  board = np.full((10, 10), ' ')

  # Initialize the game state
  player = 1
  winner = None

  # Main game loop
  while winner is None:
    # Get the move from the current player
    col = get_move(player, board)

    # Drop the piece into the board
    for row in range(len(board)-1, -1, -1):
      if board[row][col] == ' ':
        board[row][col] = 'X' if player == 1 else 'O'
        break

    # Check for a winner
    winner = check_win(board)

    # Switch to the other player
    player = 2 if player == 1 else 1

  # Print the final board and declare the winner
  print_board(board)
  if winner is None:
    print("Draw")
  else:
    print(f"Player {winner} wins!")

if __name__ == "__main__":
  main()
