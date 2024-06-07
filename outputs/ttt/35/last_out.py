import numpy as np

def jdv():
  """
  A simple 3x3 grid game where two players take turns placing their pieces
  in a free space until one of them makes a line with 3 (horizontally,
  vertically or diagonally) adjacent pieces.

  If there are no more free spaces, the game is declared a draw.

  Args:
    None

  Returns:
    None
  """

  # Create a 3x3 grid
  board = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

  # Create a list of player symbols
  symbols = ['X', 'O']

  # Get the names of the two players
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")

  # Set the current player to player 1
  current_player = 1

  # Loop until the game is over
  while True:
    # Get the current player's symbol
    symbol = symbols[current_player - 1]

    # Get the current player's move
    try:
      row = int(input(f"{player1_name if current_player == 1 else player2_name}'s turn. Enter row (1-3): ")) - 1
      column = int(input("Enter column (1-3): ")) - 1
    except ValueError:
      print("Invalid input. Please enter a valid row and column number.")
      continue

    # Check if the move is valid
    if row < 0 or row > 2 or column < 0 or column > 2 or board[row][column] != ' ':
      print("Invalid move.")
      continue

    # Place the player's piece on the grid
    board[row][column] = symbol

    # Check if the player has won
    if check_win(board, symbol):
      print(f"{player1_name if current_player == 1 else player2_name} wins!")
      break

    # Check if the game is a draw
    if check_draw(board):
      print("Draw!")
      break

    # Switch to the other player
    current_player = 3 - current_player


def check_win(board, symbol):
  """
  Checks if the given symbol has won the game.

  Args:
    board: A 3x3 grid.
    symbol: The symbol to check for.

  Returns:
    True if the symbol has won, False otherwise.
  """

  # Check for horizontal wins
  for row in board:
    if np.all(row == symbol):
      return True

  # Check for vertical wins
  for column in range(3):
    if np.all(board[:, column] == symbol):
      return True

  # Check for diagonal wins
  if np.all(board.diagonal() == symbol):
    return True

  if np.all(np.flip(board).diagonal() == symbol):
    return True

  return False


def check_draw(board):
  """
  Checks if the game is a draw.

  Args:
    board: A 3x3 grid.

  Returns:
    True if the game is a draw, False otherwise.
  """

  return np.all(board != ' ')


def reset_game():
  """
  Resets the game board to its initial state.
  """

  board[:] = ' '


if __name__ == "__main__":
  while True:
    jdv()
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
      break
