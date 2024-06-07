import numpy as np

def jdv():
  """
  This function implements the jdv game.
  """

  # Create the game board.
  board = np.zeros((3, 3))

  # Create a list of player symbols.
  player_symbols = ['X', 'O']

  # Keep track of the current player.
  current_player = 0

  # Keep track of the number of moves made.
  num_moves = 0

  # Main game loop.
  while True:
    # Get the player's move.
    print(f"Player {player_symbols[current_player]}'s turn.")
    row, col = map(int, input("Enter the row and column of your move (0-2): ").split())

    # Check if the move is valid.
    if board[row, col] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board.
    board[row, col] = player_symbols[current_player]

    # Increment the number of moves made.
    num_moves += 1

    # Check if the player has won.
    if check_win(board, player_symbols[current_player]):
      print(f"Player {player_symbols[current_player]} wins!")
      break

    # Check if the game is a draw.
    if num_moves == 9:
      print("Draw!")
      break

    # Switch to the other player.
    current_player = (current_player + 1) % 2


def check_win(board, player_symbol):
  """
  This function checks if the player has won the game.

  Args:
    board: The game board.
    player_symbol: The player's symbol.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row.
  for row in range(3):
    if all(board[row, :] == player_symbol):
      return True

  # Check for a win in each column.
  for col in range(3):
    if all(board[:, col] == player_symbol):
      return True

  # Check for a win in each diagonal.
  if all(board.diagonal() == player_symbol) or all(np.flip(board).diagonal() == player_symbol):
    return True

  # No win yet.
  return False


if __name__ == "__main__":
  jdv()
