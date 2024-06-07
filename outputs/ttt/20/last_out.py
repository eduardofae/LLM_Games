class Game:
  def __init__(self):
    self.game_board = set()
    self.current_player = "X"

  def print_grid(self):
    """Prints the current state of the game board."""
    for row in range(3):
      for col in range(3):
        if (row, col) in self.game_board:
          print(self.game_board[(row, col)], end=" ")
        else:
          print(" ", end=" ")
      print()

  def check_win(self):
    """Checks if the current player has won the game."""
    # Check rows
    for row in range(3):
      if all((row, col) in self.game_board and self.game_board[(row, col)] == self.current_player for col in range(3)):
        return True

    # Check columns
    for col in range(3):
      if all((row, col) in self.game_board and self.game_board[(row, col)] == self.current_player for row in range(3)):
        return True

    # Check diagonals
    if (0, 0) in self.game_board and (1, 1) in self.game_board and (2, 2) in self.game_board and self.game_board[(0, 0)] == self.game_board[(1, 1)] == self.game_board[(2, 2)] == self.current_player:
      return True
    if (0, 2) in self.game_board and (1, 1) in self.game_board and (2, 0) in self.game_board and self.game_board[(0, 2)] == self.game_board[(1, 1)] == self.game_board[(2, 0)] == self.current_player:
      return True

    # No win yet
    return False

  def get_valid_moves(self):
    """Returns a list of valid moves for the current state of the game board."""
    return [(row, col) for row in range(3) for col in range(3) if (row, col) not in self.game_board]

  def play_game(self):
    """Plays the game of jdv."""

    # Game loop
    while True:
      # Print the current state of the game board
      self.print_grid()

      # Get the valid moves for the current player
      valid_moves = self.get_valid_moves()

      # If there are no valid moves, the game is a draw
      if not valid_moves:
        print("Draw!")
        break

      # Get the player's move
      while True:
        try:
          player_move = input(f"{self.current_player}'s turn: ")
          player_row, player_col = map(int, player_move.split())
          if (player_row, player_col) not in valid_moves:
            raise ValueError("Invalid move!")
          break
        except ValueError:
          print("Invalid move! Please enter a valid move.")
        except:
          print("An error occurred. Please try again.")

      # Place the player's piece on the game board
      self.game_board.add((player_row, player_col))

      # Check if the player has won
      if self.check_win():
        print(f"{self.current_player} wins!")
        break

      # Switch to the other player
      self.current_player = "O" if self.current_player == "X" else "X"


if __name__ == "__main__":
  game = Game()
  game.play_game()
