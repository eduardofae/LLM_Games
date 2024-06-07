import numpy as np

def jdv():
  # Initialize the game board
  board = np.zeros((3, 3))

  # Initialize the player turn
  player = 1

  # Game loop
  while True:
    # Print the game board
    print(board)

    # Get the player's move
    row, col = map(int, input("Player {}'s turn (row, col): ".format(player)).split())

    # Check if the move is valid
    if board[row, col] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board
    board[row, col] = player

    # Check if the player has won
    if check_win(board, player):
      print("Player {} wins!".format(player))
      break

    # Switch to the other player
    player = 3 - player

  # Check if the game is a draw
  if np.all(board != 0):
    print("Draw!")

def check_win(board, player):
  # Check for a horizontal win
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check for a vertical win
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check for a diagonal win
  if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
    return True

  # No win yet
  return False

if __name__ == "__main__":
  jdv()
