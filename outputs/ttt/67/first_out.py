import numpy as np

class Jdv:
  def __init__(self):
    self.board = np.zeros((3, 3))
    self.player = 1

  def play(self, row, col):
    if self.board[row, col] == 0:
      self.board[row, col] = self.player
      self.player *= -1

  def check_winner(self):
    for i in range(3):
      if np.all(self.board[i, :] == self.board[i, 0]) and self.board[i, 0] != 0:
        return self.board[i, 0]
      if np.all(self.board[:, i] == self.board[0, i]) and self.board[0, i] != 0:
        return self.board[0, i]

    if np.all(self.board.diagonal() == self.board[0, 0]) and self.board[0, 0] != 0:
      return self.board[0, 0]
    if np.all(np.flip(self.board).diagonal() == self.board[0, 2]) and self.board[0, 2] != 0:
      return self.board[0, 2]

    return 0

  def check_draw(self):
    return np.all(self.board != 0)

  def print_board(self):
    for row in self.board:
      print(' '.join(['X' if x == 1 else 'O' if x == -1 else ' ' for x in row]))

if __name__ == "__main__":
  game = Jdv()

  while True:
    game.print_board()

    row, col = map(int, input("Enter row and column: ").split())
    game.play(row, col)

    winner = game.check_winner()
    if winner != 0:
      game.print_board()
      print(f"Player {winner} wins!")
      break

    if game.check_draw():
      game.print_board()
      print("Draw!")
      break
