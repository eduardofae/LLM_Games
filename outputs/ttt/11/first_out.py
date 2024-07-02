def jdv():
  """
  This function implements the jdv game.

  The game is played on a 3x3 grid, and two players take turns placing their pieces in a free space.
  The first player to make a line of three adjacent pieces wins the game.
  If there are no more free spaces, the game is declared a draw.

  The function takes no arguments and returns the winner of the game.
  """

  # Create the game board.
  board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

  # Get the names of the two players.
  player1 = input("Player 1, enter your name: ")
  player2 = input("Player 2, enter your name: ")

  # Set the current player to player 1.
  current_player = player1

  # Play the game until someone wins or there are no more free spaces.
  while True:
    # Get the current player's move.
    move = input("{}'s turn. Enter a row and column number (e.g. 1,2): ".format(current_player))

    # Split the move into row and column numbers.
    row, column = map(int, move.split(','))

    # Check if the move is valid.
    if row < 1 or row > 3 or column < 1 or column > 3 or board[row-1][column-1] != ' ':
      print("Invalid move. Try again.")
      continue

    # Place the current player's piece on the board.
    board[row-1][column-1] = 'X' if current_player == player1 else 'O'

    # Check if the current player has won.
    if check_for_win(board):
      print("{} wins!".format(current_player))
      break

    # Check if there are no more free spaces.
    if all(all(space != ' ' for space in row) for row in board):
      print("Draw!")
      break

    # Switch the current player.
    current_player = player2 if current_player == player1 else player1


def check_for_win(board):
  """
  This function checks if a player has won the game.

  The function takes a game board as input and returns True if a player has won, or False otherwise.

  The function checks for wins in all possible directions (horizontally, vertically, and diagonally).
  """

  # Check for wins in each row.
  for row in board:
    if all(space == 'X' or space == 'O' for space in row):
      return True

  # Check for wins in each column.
  for column in range(3):
    if all(board[row][column] == 'X' or board[row][column] == 'O' for row in range(3)):
      return True

  # Check for wins in each diagonal.
  if all(board[row][row] == 'X' or board[row][row] == 'O' for row in range(3)):
    return True

  if all(board[row][2-row] == 'X' or board[row][2-row] == 'O' for row in range(3)):
    return True

  # No wins found.
  return False


if __name__ == "__main__":
  jdv()
