import numpy as np

def check_winner(board):
  """
  Checks if there is a winner in the game.

  Args:
    board: A 3x3 numpy array representing the game board.

  Returns:
    The player number of the winner, or 0 if there is no winner yet.
  """

  # Check for horizontal wins
  for row in board:
    if np.all(row == row[0]) and row[0] != 0:
      return row[0]

  # Check for vertical wins
  for col in board.T:
    if np.all(col == col[0]) and col[0] != 0:
      return col[0]

  # Check for diagonal wins
  if np.all(board.diagonal() == board.diagonal()[0]) and board.diagonal()[0] != 0:
    return board.diagonal()[0]
  if np.all(np.flipud(board).diagonal() == np.flipud(board).diagonal()[0]) and np.flipud(board).diagonal()[0] != 0:
    return np.flipud(board).diagonal()[0]

  # Check for a draw
  if np.all(board != 0):
    return -1

  # No winner yet
  return 0


def print_board(board):
  """
  Prints the game board to the console.

  Args:
    board: A 3x3 numpy array representing the game board.
  """

  for row in board:
    for col in row:
      if col == 0:
        print(" ", end=" ")
      else:
        print(col, end=" ")
    print()


def main():
  """
  Main game loop.
  """

  # Create a new game board
  board = np.zeros((3, 3), dtype=int)

  # Set the current player to player 1
  player = 1

  # Game loop
  while True:
    # Print the game board
    print_board(board)

    # Get the player's move
    move = input("Player {}'s move: ".format(player))

    # Check if the move is valid
    if move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      print("Invalid move. Please try again.")
      continue

    # Convert the move to a row and column index
    row = int(move) // 3
    col = int(move) % 3

    # Check if the space is already occupied
    if board[row, col] != 0:
      print("Space already occupied. Please try again.")
      continue

    # Place the player's piece on the board
    board[row, col] = player

    # Check if there is a winner
    winner = check_winner(board)

    # If there is a winner, print the winner and exit the game loop
    if winner != 0:
      print("Player {} wins!".format(winner))
      break

    # Switch to the other player
    player = 3 - player


if __name__ == "__main__":
  main()
