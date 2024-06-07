import numpy as np

def print_board(board):
  for i in range(3):
    print(' '.join(board[i]))

def check_win(board):
  for i in range(3):
    if np.all(board[i] == board[i][0]) and board[i][0] != '-':
      return board[i][0]
  for j in range(3):
    if np.all(board[:, j] == board[0, j]) and board[0, j] != '-':
      return board[0, j]
  if np.all(np.diag(board) == np.diag(board)[0]) and np.diag(board)[0] != '-':
    return np.diag(board)[0]
  if np.all(np.diag(np.flip(board)) == np.diag(np.flip(board))[0]) and np.diag(np.flip(board))[0] != '-':
    return np.diag(np.flip(board))[0]
  return '-'

def jdv():
  board = np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
  player = 'X'
  while True:
    print_board(board)
    print(f"Player {player}'s turn")
    row, col = map(int, input("Enter row and column: ").split())
    if board[row, col] == '-':
      board[row, col] = player
      if check_win(board) != '-':
        print_board(board)
        print(f"Player {player} wins!")
        break
      player = 'O' if player == 'X' else 'X'
    else:
      print("Invalid move")
  if check_win(board) == '-':
    print("Draw!")

if __name__ == "__main__":
  jdv()
