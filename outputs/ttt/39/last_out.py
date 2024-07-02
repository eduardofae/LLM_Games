import numpy as np
import unittest

def print_game_board(game_board):
  """Prints the game board to the console."""
  for i in range(3):
    for j in range(3):
      print(game_board[i][j], end=" ")
    print()

def get_winner(game_board):
  """Returns the winner of the game, or None if there is no winner yet."""
  # Check rows
  for i in range(3):
    if game_board[i][0] == game_board[i][1] == game_board[i][2] and game_board[i][0] != ' ':
      return game_board[i][0]

  # Check columns
  for j in range(3):
    if game_board[0][j] == game_board[1][j] == game_board[2][j] and game_board[0][j] != ' ':
      return game_board[0][j]

  # Check diagonals
  if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] != ' ':
    return game_board[0][0]
  if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] != ' ':
    return game_board[0][2]

  # Check for draw
  if not any(' ' in row for row in game_board):
    return 'Draw'

  # No winner or draw yet
  return None

def play_jdv():
  """Plays a game of JDV."""

  # Get the game board size
  while True:
    try:
      game_board_size = int(input("Enter the game board size (e.g. 3 for a 3x3 game board): "))
      if game_board_size < 3:
        print("Invalid game board size. Please enter a value greater than or equal to 3.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter an integer.")

  # Create the game board
  game_board = [[' ' for _ in range(game_board_size)] for _ in range(game_board_size)]

  # Get player names
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Determine who goes first
  first_player = input("Who wants to go first? ({} or {}) ".format(player1, player2))

  # Keep track of the current player
  current_player = first_player

  # Play the game until there is a winner or draw
  while True:
    # Print the game board
    print_game_board(game_board)

    # Get the player's move
    while True:
      try:
        row, col = map(int, input("{}, enter your move (row, column): ".format(current_player)).split())
        if not (0 <= row < game_board_size and 0 <= col < game_board_size):
          print("Invalid move. Please enter a row and column within the game board size.")
          continue
        if game_board[row][col] != ' ':
          print("Invalid move. That space is already occupied.")
          continue
        break
      except ValueError:
        print("Invalid input. Please enter two integers separated by a comma.")

    # Place the player's piece on the game board
    game_board[row][col] = current_player

    # Check if the player has won
    winner = get_winner(game_board)
    if winner:
      print("{} wins!".format(winner))
      break

    # Switch to the other player
    current_player = player1 if current_player == player2 else player2

  # Ask if the players want to play again
  play_again = input("Do you want to play again? (y/n) ")
  if play_again == 'y':
    play_jdv()

# Unit tests
class JDVTests(unittest.TestCase):

  def test_get_winner_row(self):
    game_board = [['X', 'X', 'X'],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
    winner = get_winner(game_board)
    self.assertEqual(winner, 'X')

  def test_get_winner_column(self):
    game_board = [[' ', 'X', ' '],
                   [' ', 'X', ' '],
                   [' ', 'X', ' ']]
    winner = get_winner(game_board)
    self.assertEqual(winner, 'X')

  def test_get_winner_diagonal1(self):
    game_board = [['X', ' ', ' '],
                   [' ', 'X', ' '],
                   [' ', ' ', 'X']]
    winner = get_winner(game_board)
    self.assertEqual(winner, 'X')

  def test_get_winner_diagonal2(self):
    game_board = [[' ', ' ', 'X'],
                   [' ', 'X', ' '],
                   ['X', ' ', ' ']]
    winner = get_winner(game_board)
    self.assertEqual(winner, 'X')

  def test_get_winner_draw(self):
    game_board = [['X', 'O', 'X'],
                   ['O', 'X', 'O'],
                   ['X', 'O', 'X']]
    winner = get_winner(game_board)
    self.assertEqual(winner, 'Draw')

  def test_get_winner_no_winner(self):
    game_board = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
    winner = get_winner(game_board)
    self.assertEqual(winner, None)

# Play the game
if __name__ == "__main__":
  unittest.main()
  play_jdv()
