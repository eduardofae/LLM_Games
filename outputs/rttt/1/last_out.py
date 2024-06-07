
import numpy as np

class JdvGame:
  def __init__(self, size=3, num_players=2):
    self.grid = np.zeros((size, size), dtype=int)
    self.players = [i for i in range(1, num_players + 1)]
    self.current_player = 0

  def play(self):
    while True:
      self.print_grid()
      print("Player", self.players[self.current_player], "turn")
      try:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if row < 0 or row >= self.grid.shape[0] or col < 0 or col >= self.grid.shape[1] or self.grid[row, col] != 0:
          raise ValueError("Invalid move")
        self.grid[row, col] = self.players[self.current_player]
      except ValueError as e:
        print(e)
        continue
      winner = self.check_winner()
      if winner != 0:
        if winner == -1:
          print("Draw")
        else:
          print("Player", winner, "wins")
        break
      self.current_player = (self.current_player + 1) % len(self.players)

  def check_winner(self):
    # Check rows
    for i in range(self.grid.shape[0]):
      if np.all(self.grid[i] == self.grid[i][0]) and self.grid[i][0] != 0:
        return self.grid[i][0]
    # Check columns
    for j in range(self.grid.shape[1]):
      if np.all(self.grid[:, j] == self.grid[0, j]) and self.grid[0, j] != 0:
        return self.grid[0, j]
    # Check diagonals
    if np.all(np.diag(self.grid) == self.grid[0, 0]) and self.grid[0, 0] != 0:
      return self.grid[0, 0]
    if np.all(np.diag(self.grid[::-1]) == self.grid[0, self.grid.shape[1] - 1]) and self.grid[0, self.grid.shape[1] - 1] != 0:
      return self.grid[0, self.grid.shape[1] - 1]
    # Check draw
    if np.all(self.grid != 0):
      return -1
    # No winner or draw
    return 0

  def print_grid(self):
    for i in range(self.grid.shape[0]):
      for j in range(self.grid.shape[1]):
        print(self.grid[i, j], end=" ")
      print()

if __name__ == "__main__":
  size = int(input("Enter the size of the game board: "))
  num_players = int(input("Enter the number of players: "))
  game = JdvGame(size, num_players)
  game.play()
