import numpy as np

class Jdv:
  def __init__(self):
    self.grid = np.zeros((3, 3), dtype=int)
    self.player_turn = 1  # 1 or 2
    self.winner = None

  def play(self, row, col):
    if self.winner is not None:
      return  # Game is over

    if self.grid[row, col] != 0:
      return  # Space is already occupied

    self.grid[row, col] = self.player_turn
    self.check_winner()
    self.player_turn = 3 - self.player_turn

  def check_winner(self):
    # Check rows
    for row in range(3):
      if np.all(self.grid[row, :] == self.player_turn):
        self.winner = self.player_turn
        return

    # Check columns
    for col in range(3):
      if np.all(self.grid[:, col] == self.player_turn):
        self.winner = self.player_turn
        return

    # Check diagonals
    if np.all(self.grid.diagonal() == self.player_turn):
      self.winner = self.player_turn
      return
    if np.all(np.flip(self.grid).diagonal() == self.player_turn):
      self.winner = self.player_turn
      return

    # Check for draw
    if np.all(self.grid != 0):
      self.winner = 0  # Draw

  def get_grid(self):
    return self.grid

  def get_winner(self):
    return self.winner

if __name__ == "__main__":
  jdv = Jdv()
  while jdv.winner is None:
    print(jdv.get_grid())
    row, col = map(int, input("Enter row and column: ").split())
    jdv.play(row, col)

  if jdv.winner == 0:
    print("Draw")
  else:
    print("Player", jdv.winner, "wins")
