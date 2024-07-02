def jdv():
  """
  A simple command-line game of Jdv.

  The game is played on a 3x3 grid, and two players take turns placing their pieces in the free spaces.
  The first player to get three of their pieces in a row, either horizontally, vertically, or diagonally, wins the game.
  If there are no more free spaces, the game is declared a draw.
  """

  # Create the game board.
  board = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]

  # Create a list of the available spaces.
  available_spaces = [(row, column) for row in range(3) for column in range(3)]

  # Create a dictionary of the players' pieces.
  players = {
      'A': 'X',
      'B': 'O'
  }

  # Get the players' names.
  player_a_name = input("Player A's name: ")
  player_b_name = input("Player B's name: ")

  # Start the game.
  current_player = 'A'
  game_over = False

  while not game_over:

    # Get the current player's move.
    move = input(f"{current_player}'s move: ")

    # Check if the move is valid.
    if move not in available_spaces:
      print("Invalid move.")
      continue

    # Place the current player's piece on the board.
    row, column = move
    board[row][column] = players[current_player]

    # Check if the current player has won.
    if check_for_win(board, current_player):
      game_over = True
      print(f"{current_player} wins!")

    # Check if there are no more available spaces.
    if len(available_spaces) == 0:
      game_over = True
      print("Draw!")

    # Switch to the other player.
    current_player = 'A' if current_player == 'B' else 'B'

  # Print the final board.
  for row in board:
    print(' '.join(row))


def check_for_win(board, player):
  """
  Checks if the given player has won the game.

  Args:
    board: The game board.
    player: The player to check for a win.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row.
  for row in board:
    if all(cell == player for cell in row):
      return True

  # Check for a win in each column.
  for column in range(3):
    if all(board[row][column] == player for row in range(3)):
      return True

  # Check for a win in each diagonal.
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True

  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True

  # No win found.
  return False


if __name__ == "__main__":
  jdv()
