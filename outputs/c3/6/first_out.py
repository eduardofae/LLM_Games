import numpy as np

class Pong:
  def __init__(self):
    self.board = np.zeros((10, 10), dtype=int)
    self.player_turn = 1

  def play(self):
    while True:
      # Get the player's move
      move = int(input("Player {}'s turn: ".format(self.player_turn)))

      # Check if the move is valid
      if move < 1 or move > 10 or self.board[9, move-1] != 0:
        print("Invalid move. Try again.")
        continue

      # Place the player's piece on the board
      for i in range(9, -1, -1):
        if self.board[i, move-1] == 0:
          self.board[i, move-1] = self.player_turn
          break

      # Check if the player has won
      if self.check_win(self.player_turn):
        print("Player {} wins!".format(self.player_turn))
        break

      # Check if the game is a draw
      if np.all(self.board != 0):
        print("Draw!")
        break

      # Switch to the other player's turn
      self.player_turn = 3 - self.player_turn

  def check_win(self, player):
    # Check for a horizontal win
    for i in range(10):
      if np.all(self.board[i, :] == player):
        return True

    # Check for a vertical win
    for i in range(10):
      if np.all(self.board[:, i] == player):
        return True

    # Check for a diagonal win
    for i in range(10):
      if np.all(self.board.diagonal()[i::10] == player):
        return True
      if np.all(np.flip(self.board).diagonal()[i::10] == player):
        return True

    return False

if __name__ == "__main__":
  game = Pong()
  game.play()
