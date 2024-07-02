import numpy as np

class Jdv:
  def __init__(self):
    self.board = np.zeros((3, 3))
    self.player_turn = 1
    self.player_names = ["Player 1", "Player 2"]
    self.player_symbols = ["X", "O"]
    self.player_scores = [0, 0]
    self.game_stats = {"num_moves": 0, "avg_game_length": 0, "win_counts": [0, 0], "most_common_winning_combinations": []}

  def print_board(self):
    for row in self.board:
      for cell in row:
        if cell == 0:
          print(" ", end=" ")
        elif cell == 1:
          print(self.player_symbols[0], end=" ")
        else:
          print(self.player_symbols[1], end=" ")
      print()

  def is_valid_move(self, row, col):
    if row < 0 or row >= 3 or col < 0 or col >= 3:
      return False
    if self.board[row][col] != 0:
      return False
    return True

  def make_move(self, row, col):
    if not self.is_valid_move(row, col):
      raise ValueError("Invalid move.")
    self.board[row][col] = self.player_turn
    self.game_stats["num_moves"] += 1

  def check_win(self):
    # Check rows
    for row in self.board:
      if np.all(row == self.player_turn):
        return True
    # Check columns
    for col in range(3):
      if np.all(self.board[:, col] == self.player_turn):
        return True
    # Check diagonals
    if np.all(np.diagonal(self.board) == self.player_turn) or np.all(np.flipud(self.board).diagonal() == self.player_turn):
      return True
    return False

  def play(self):
    # Print introduction and instructions
    print("Welcome to the Jdv game!")
    print("Rules:")
    print("- Players take turns placing their symbols on the 3x3 board.")
    print("- The first player to get three of their symbols in a row, column, or diagonal wins.")
    print("- If all the squares are filled and no player has won, the game ends in a draw.")
    print()

    # Get player names and symbols
    for i in range(2):
      player_name = input(f"Enter player {i+1}'s name: ")
      player_symbol = input(f"Enter player {i+1}'s symbol (X or O): ")
      self.player_names[i] = player_name
      self.player_symbols[i] = player_symbol

    # Start the game loop
    while True:
      # Print the game board
      self.print_board()

      # Get the move from the current player
      player_name = self.player_names[self.player_turn - 1]
      player_symbol = self.player_symbols[self.player_turn - 1]
      row = int(input(f"{player_name}'s turn. Row: "))
      col = int(input("Col: "))

      try:
        self.make_move(row, col)
      except ValueError:
        print("Invalid move. Please try again.")
        continue

      # Check if the current player has won
      if self.check_win():
        print(f"{player_name} ({player_symbol}) wins!")
        self.player_scores[self.player_turn - 1] += 1
        self.game_stats["win_counts"][self.player_turn - 1] += 1
        break

      # Switch the player turn
      self.player_turn = 3 - self.player_turn

      # Check if the game is a draw
      if np.all(self.board != 0):
        print("Draw!")
        break

      # Calculate the average game length
      self.game_stats["avg_game_length"] = self.game_stats["num_moves"] / 2

      # Print the final scores and game statistics
      print("Final scores:")
      for i in range(2):
        print(f"{self.player_names[i]}: {self.player_scores[i]}")
      print("Game statistics:")
      for stat, value in self.game_stats.items():
        print(f"{stat}: {value}")

      # Ask players if they want to play again
      play_again = input("Do you want to play again? (y/n): ")
      if play_again == "y":
        self.reset_game()
      else:
        break

  def reset_game(self):
    self.board = np.zeros((3, 3))
    self.player_turn = 1
    self.game_stats["num_moves"] = 0

if __name__ == "__main__":
  jdv = Jdv()
  jdv.play()
