import numpy as np
import unittest

# Define constants for board size and player numbers
BOARD_SIZE = 10
PLAYER1 = 1
PLAYER2 = 2

def create_board():
  """Creates a BOARD_SIZE x BOARD_SIZE numpy array to represent the game board."""
  board = np.zeros((BOARD_SIZE, BOARD_SIZE))
  return board

def place_piece(board, player, col):
  """Places a piece for the given player in the lowest free space of the given column."""
  for i in range(BOARD_SIZE-1, -1, -1):
    if board[i][col] == 0:
      board[i][col] = player
      return

def check_win(board, player):
  """Checks if the given player has won the game."""
  # Check for horizontal wins
  for i in range(BOARD_SIZE):
    if np.all(board[i] == player):
      return True

  # Check for vertical wins
  for j in range(BOARD_SIZE):
    if np.all(board[:, j] == player):
      return True

  # Check for diagonal wins
  for i in range(BOARD_SIZE-2):
    for j in range(BOARD_SIZE-2):
      if np.all(board[i:i+3, j:j+3] == player):
        return True

  # Check for diagonal wins in the other direction
  for i in range(BOARD_SIZE-2):
    for j in range(2, BOARD_SIZE):
      if np.all(board[i:i+3, j:j-3:-1] == player):
        return True

  return False

def play_game(player1_moves, player2_moves):
  """Plays the game of pong."""
  board = create_board()
  current_player = PLAYER1
  move_index = 0
  while True:
    # Print game status
    print("Current board:")
    print(board)
    print("Current player: Player {}".format(current_player))
    print("Moves remaining: {}".format(len(player1_moves) + len(player2_moves) - move_index))

    # Get the column where the player wants to place their piece
    try:
        if current_player == PLAYER1:
            col = player1_moves[move_index]
        else:
            col = player2_moves[move_index]

        # Check if the column is within the valid range
        if col < 0 or col >= BOARD_SIZE:
            print("Invalid column. Please enter a number between 0 and {}".format(BOARD_SIZE - 1))
            continue

        # Check if the column has at least one free space
        if np.all(board[:, col] != 0):
            print("Invalid move. Column {} is full.".format(col))
            continue

        # Place the piece
        place_piece(board, current_player, col)

        # Check if the player has won
        if check_win(board, current_player):
            print("Player {} wins!".format(current_player))
            break

        # Check if the game is a draw
        if np.all(board != 0):
            print("Draw!")
            break

        # Switch to the other player
        move_index += 1
        current_player = PLAYER1 if current_player == PLAYER2 else PLAYER2

    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid column number.")

# Define the moves for each player
player1_moves = [0, 2, 4, 6, 8]
player2_moves = [1, 3, 5, 7, 9]

# Play the game
play_game(player1_moves, player2_moves)


class TestPong(unittest.TestCase):

    def test_horizontal_win(self):
        # Create a game board with a horizontal win for Player 1
        board = np.array([[1, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])

        # Check if Player 1 has won
        self.assertTrue(check_win(board, PLAYER1))

    def test_vertical_win(self):
        # Create a game board with a vertical win for Player 2
        board = np.array([[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 2, 2, 2, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])

        # Check if Player 2 has won
        self.assertTrue(check_win(board, PLAYER2))

    def test_diagonal_win(self):
        # Create a game board with a diagonal win for Player 1
        board = np.array([[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 1],
                           [0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 0]])

        # Check if Player 1 has won
        self.assertTrue(check_win(board, PLAYER1))

    def test_draw(self):
        # Create a game board that is a draw
        board = np.array([[1, 2, 1, 2, 1],
                           [2, 1, 2, 1, 2],
                           [1, 2, 1, 2, 1],
                           [2, 1, 2, 1, 2],
                           [1, 2, 1, 2, 1]])

        # Check if the game is a draw
        self.assertTrue(np.all(board != 0))

if __name__ == "__main__":
    unittest.main()
