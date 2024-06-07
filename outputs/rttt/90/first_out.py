import numpy as np

def jdv():
  """
  jdv game
  """

  # Create the game board
  board = np.zeros((3, 3))

  # Player 1 is 'X' and Player 2 is 'O'
  player1 = 'X'
  player2 = 'O'

  # Keep track of whose turn it is
  turn = player1

  # Game loop
  while True:
    # Print the game board
    print(board)

    # Get the player's move
    move = input(f"{turn}'s turn. Enter a row and column (e.g. 1,2): ")
    row, col = map(int, move.split(','))

    # Check if the move is valid
    if board[row, col] != 0:
      print("Invalid move. That space is already taken.")
      continue

    # Place the player's piece on the board
    board[row, col] = turn

    # Check if the player has won
    if check_win(board, turn):
      print(f"{turn} wins!")
      break

    # Check if the game is a draw
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch turns
    if turn == player1:
      turn = player2
    else:
      turn = player1

# Function to check if a player has won
def check_win(board, player):
  """
  Checks if a player has won the game.
  
  Args:
    board: The game board.
    player: The player to check for.
  
  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row
  for row in board:
    if np.all(row == player):
      return True

  # Check for a win in each column
  for col in board.T:
    if np.all(col == player):
      return True

  # Check for a win in each diagonal
  if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
    return True

  # No win yet
  return False

if __name__ == "__main__":
  jdv()
