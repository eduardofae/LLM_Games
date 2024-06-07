import numpy as np

def jdv():
  """
  This function implements the jdv game.

  The game is played on a grid of the size chosen by the players, and two players take turns placing their pieces in the grid.
  The first player to get three of their pieces in a row, either horizontally, vertically, or diagonally, wins the game.
  If all the squares in the grid are filled and neither player has won, the game is declared a draw.
  """

  # Get the size of the grid from the players
  grid_size = int(input("What size grid would you like to play on? (e.g., 3, 4, 5) "))

  # Create the game board
  board = np.empty((grid_size, grid_size), dtype=str)
  board[:] = ' '

  # Get the names of the two players
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Set the current player to player 1
  current_player = player1

  # Keep track of the number of moves that have been made
  moves = 0

  # Game loop
  while True:
    # Print the grid
    print_grid(board)

    # Get the player's move
    move = input(f"{current_player}, where would you like to place your piece? (row, column) ")
    row, column = map(int, move.split(","))

    # Check if the move is valid
    if not is_valid_move(board, row, column):
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece in the grid
    board[row, column] = current_player

    # Check if the player has won
    if check_win(board, current_player):
      print(f"{current_player} wins!")
      break

    # Increment the number of moves
    moves += 1

    # Check if the game is a draw
    if moves == grid_size ** 2:
      print("Draw!")
      break

    # Switch the current player
    current_player = player2 if current_player == player1 else player1


def is_valid_move(board, row, column):
  """
  Checks if the given move is valid.

  Args:
    board: The game board.
    row: The row of the move.
    column: The column of the move.

  Returns:
    True if the move is valid, False otherwise.
  """

  return board[row, column] == ' '


def check_win(board, player):
  """
  Checks if the given player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for horizontal wins
  for row in range(board.shape[0]):
    if all(board[row] == player):
      return True

  # Check for vertical wins
  for column in range(board.shape[1]):
    if all(board[:, column] == player):
      return True

  # Check for diagonal wins
  if all(board.diagonal() == player):
    return True

  if all(np.flip(board).diagonal() == player):
    return True

  # No wins found
  return False


def print_grid(board):
  """
  Prints the game board.
  """

  # Print the column numbers
  print("   ", end="")
  for i in range(board.shape[1]):
    print(i, end=" ")
  print()

  # Print the grid
  for i in range(board.shape[0]):
    print(i, "|", end=" ")
    for j in range(board.shape[1]):
      print(board[i, j], end=" ")
    print()


if __name__ == "__main__":
  jdv()
