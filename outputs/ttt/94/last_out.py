import copy
import colorama
from colorama import Fore, Back, Style

class Jdv:
  def __init__(self, board_size=3):
    """
    This class implements the jdv game, where two players take turns placing their pieces in a free space of a board, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line wins. If there are no more free spaces, the game is declared a draw.

    Args:
      board_size: The size of the board (default: 3).
    """

    self.board_size = board_size

    # Create the game board
    self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

    # Create a list of the possible winning combinations
    self.winning_combinations = []
    for i in range(board_size):
      # Horizontal combinations
      self.winning_combinations.append([(i, j) for j in range(board_size)])
      # Vertical combinations
      self.winning_combinations.append([(j, i) for j in range(board_size)])

    # Diagonal combinations
    if board_size >= 3:
      self.winning_combinations.append([(i, i) for i in range(board_size)])
      self.winning_combinations.append([(i, board_size - i - 1) for i in range(board_size)])

    # Create a variable to keep track of the current player
    self.current_player = 'X'

    # Create a variable to keep track of the number of moves that have been made
    self.num_moves = 0

    # Create a variable to keep track of the winner
    self.winner = None

  def check_winner(self, player):
    """
    This function checks if a player has won the game.

    Args:
      player: The player to check for a win.

    Returns:
      True if the player has won, False otherwise.
    """

    # Check each of the possible winning combinations to see if the player has won
    for combination in self.winning_combinations:
      if all(self.board[x][y] == player for x, y in combination):
        return True

    # If the player has not won, return False
    return False

  def get_next_move(self, player):
    """
    This function gets the next move from a player.

    Args:
      player: The player to get the next move from.

    Returns:
      A tuple representing the next move.
    """

    # Get the player's move
    while True:
      try:
        move = input(f"{player}'s turn. Enter your move (row, column): ")
        move = tuple(int(x) for x in move.split(','))

        # Check if the player's move is valid
        if move[0] < 0 or move[0] >= self.board_size or move[1] < 0 or move[1] >= self.board_size or self.board[move[0]][move[1]] != ' ':
          print("Invalid move. Please try again.")
          continue
      except ValueError:
        print("Invalid input. Please enter two integers separated by a comma.")
        continue
      break

    # Return the player's move
    return move

  def play(self):
    """
    This function plays the game until someone wins or there is a draw.
    """

    # Play the game until someone wins or there is a draw
    while not self.winner and self.num_moves < self.board_size**2:
      # Get the next move from the current player
      move = self.get_next_move(self.current_player)

      # Place the player's piece on the board
      self.board[move[0]][move[1]] = self.current_player

      # Increment the number of moves
      self.num_moves += 1

      # Check if the current player has won
      self.winner = self.check_winner(self.current_player)

      # If the current player has not won, switch to the other player
      if not self.winner:
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    # Print the game board
    for row in self.board:
      print(' '.join([Fore.RED + x if x == 'X' else (Fore.BLUE + x if x == 'O' else x) for x in row]))

    # Declare the winner or draw
    if self.winner:
      print(f"{self.winner} wins!")
    else:
      print("Draw!")

# Play the game
jdv = Jdv()
jdv.play()
