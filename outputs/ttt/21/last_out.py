import numpy as np

def jdv():
  """
  This function implements the jdv game.
  """

  # Get the game board size.
  board_size = int(input("Enter the size of the game board (3-5): "))
  while board_size not in range(3, 6):
    board_size = int(input("Invalid size. Please enter a size between 3 and 5: "))

  # Create the game board.
  board = np.zeros((board_size, board_size))

  # Create a list of player symbols.
  player_symbols = ['X', 'O']

  # Get the players' symbols.
  player1_symbol = input("Player 1, choose your symbol (X or O): ")
  while player1_symbol not in player_symbols:
    player1_symbol = input("Invalid symbol. Please choose X or O: ")
  player2_symbol = 'X' if player1_symbol == 'O' else 'O'

  # Keep track of the current player.
  current_player = 0

  # Keep track of the number of moves made.
  num_moves = 0

  # Keep track of the game history.
  game_history = []

  # Main game loop.
  while True:
    # Get the player's move.
    print(f"Player {player_symbols[current_player]}'s turn.")
    try:
      row, col = map(int, input("Enter the row and column of your move (0-2): ").split())
    except ValueError:
      print("Invalid move. Please try again.")
      continue

    # Check if the move is valid.
    if board[row, col] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board.
    board[row, col] = player_symbols[current_player]

    # Add the move to the game history.
    game_history.append((row, col, player_symbols[current_player]))

    # Increment the number of moves made.
    num_moves += 1

    # Check if the player has won.
    if check_win(board, player_symbols[current_player]):
      print(f"Player {player_symbols[current_player]} wins!")
      break

    # Check if the game is a draw.
    if num_moves == board_size ** 2:
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
  for row in range(board.shape[0]):
    if all(board[row, :] == player_symbol):
      return True

  # Check for a win in each column.
  for col in range(board.shape[1]):
    if all(board[:, col] == player_symbol):
      return True

  # Check for a win in each diagonal.
  if all(board.diagonal() == player_symbol) or all(np.flip(board).diagonal() == player_symbol):
    return True

  # No win yet.
  return False


if __name__ == "__main__":
  while True:
    jdv()

    # Ask the players if they want to play again.
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
      break
