import numpy as np

def jdv():
  """
  Play a game of JDV.

  The game is played on a 3x3 grid. Two players take turns placing their pieces in a free space of the grid.
  The first player to make a line of three adjacent pieces wins. If there are no more free spaces, the game is declared a draw.

  Args:
    None

  Returns:
    None
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Set the current player to 1.
  current_player = 1

  # Create a list to store the winning combinations.
  winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ]

  # Play the game until there is a winner or a draw.
  while True:
    # Get the move from the current player.
    move = get_move(board, current_player)

    # Place the piece on the board.
    board[move[0], move[1]] = current_player

    # Check if the current player has won.
    if check_win(board, current_player, winning_combinations):
      print("Player", current_player, "wins!")
      break

    # Check if there are any more free spaces.
    if not np.any(board == 0):
      print("Draw!")
      break

    # Switch to the other player.
    current_player = 3 - current_player

def get_move(board, player):
  """
  Get a move from the player.

  Args:
    board: The current state of the game board.
    player: The current player.

  Returns:
    A tuple of the row and column of the move.
  """

  # Get the row and column from the player.
  while True:
    try:
      row = int(input("Enter the row (0-2): "))
      column = int(input("Enter the column (0-2): "))

      # Check if the move is valid.
      if board[row, column] != 0:
        print("Invalid move. Please try again.")
        continue
      else:
        break
    except ValueError:
      print("Invalid input. Please enter integers only.")

  # Return the move.
  return row, column

def check_win(board, player, winning_combinations):
  """
  Check if the player has won.

  Args:
    board: The current state of the game board.
    player: The current player.
    winning_combinations: A list of winning combinations.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check each winning combination to see if the player has won.
  for combination in winning_combinations:
    if board[combination[0]] == player and board[combination[1]] == player and board[combination[2]] == player:
      return True

  # No win found.
  return False

if __name__ == "__main__":
  jdv()
