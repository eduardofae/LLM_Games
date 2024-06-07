import numpy as np

def jdv():
  board = np.zeros((3, 3))
  player = 1
  while True:
    print(board)
    move = input("Player {}'s turn: ".format(player))
    i, j = map(int, move.split())
    if board[i, j] != 0:
      print("Invalid move")
      continue
    board[i, j] = player
    if check_win(board, player):
      print("Player {} wins!".format(player))
      break
    if np.all(board != 0):
      print("Draw!")
      break
    player = 3 - player

def check_win(board, player):
  for i in range(3):
    if np.all(board[i, :] == player) or np.all(board[:, i] == player):
      return True
  if np.all(np.diag(board) == player) or np.all(np.diag(np.flipud(board)) == player):
    return True
  return False

if __name__ == "__main__":
  jdv()
