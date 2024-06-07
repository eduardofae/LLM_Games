import numpy as np

def jdv():
  """Game of JDV (3x3 grid with 2 players placing pieces until one makes a line of 3)."""

  # Initialize the game board
  board = np.zeros((3, 3), dtype=int)

  # Initialize the player turn
  player = 1

  # Keep track of the number of moves made
  moves = 0

  # Game loop
  while True:
    # Get the player's move
    print(f"Player {player}'s turn:")
    row, col = map(int, input("Enter row and column (e.g. 1 2): ").split())

    # Check if the move is valid
    if board[row-1][col-1] != 0:
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the board
    board[row-1][col-1] = player

    # Increment the number of moves made
    moves += 1

    # Check if the player has made a line of 3
    if check_win(board, player):
      print(f"Player {player} wins!")
      break

    # Check if the game is a draw
    if moves == 9:
      print("Draw!")
      break

    # Switch the player turn
    player = 3 - player

def check_win(board, player):
  """Check if the player has made a line of 3."""

  # Check the rows
  for i in range(3):
    if np.all(board[i] == player):
      return True

  # Check the columns
  for j in range(3):
    if np.all(board[:, j] == player):
      return True

  # Check the diagonals
  if np.all(np.diag(board) == player) or np.all(np.diag(np.flip(board)) == player):
    return True

  # No line of 3 found
  return False

if __name__ == "__main__":
  jdv()
