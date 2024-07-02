import numpy as np

def check_winner(board):
  """
  Checks if there is a winner in the board.

  Args:
    board: A numpy array representing the game board.

  Returns:
    The player number of the winner, or 0 if there is no winner.
  """

  # Check for horizontal wins
  for row in range(10):
    for col in range(7):
      if board[row, col] != 0 and board[row, col] == board[row, col + 1] and board[row, col] == board[row, col + 2]:
        return board[row, col]

  # Check for vertical wins
  for col in range(10):
    for row in range(7):
      if board[row, col] != 0 and board[row, col] == board[row + 1, col] and board[row, col] == board[row + 2, col]:
        return board[row, col]

  # Check for diagonal wins
  for row in range(7):
    for col in range(7):
      if board[row, col] != 0 and board[row, col] == board[row + 1, col + 1] and board[row, col] == board[row + 2, col + 2]:
        return board[row, col]

      if board[row, col] != 0 and board[row, col] == board[row + 1, col - 1] and board[row, col] == board[row + 2, col - 2]:
        return board[row, col]

  # No winner yet
  return 0

def print_board(board):
  """
  Prints the game board to the console.

  Args:
    board: A numpy array representing the game board.
  """

  for row in range(10):
    for col in range(10):
      if board[row, col] == 0:
        print(" ", end=" ")
      elif board[row, col] == 1:
        print("X", end=" ")
      elif board[row, col] == 2:
        print("O", end=" ")
    print()

def main():
  """
  The main game loop.
  """

  # Create the game board
  board = np.zeros((10, 10), dtype=int)

  # Set the player number
  player = 1

  # Game loop
  while True:
    # Print the game board
    print_board(board)

    # Get the player's move
    move = int(input("Player {}'s turn: ".format(player)))

    # Place the player's piece on the board
    for row in range(9, -1, -1):
      if board[row, move - 1] == 0:
        board[row, move - 1] = player
        break

    # Check for a winner
    winner = check_winner(board)
    if winner != 0:
      print("Player {} wins!".format(winner))
      break

    # Check for a draw
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch to the other player
    player = 3 - player

if __name__ == "__main__":
  main()
