import numpy as np

def check_win(board):
  # Check for rows
  for i in range(3):
    if np.all(board[i] == board[i][0]) and board[i][0] != 0:
      return board[i][0]

  # Check for columns
  for j in range(3):
    if np.all(board[:, j] == board[0, j]) and board[0, j] != 0:
      return board[0, j]

  # Check for diagonals
  if np.all(np.diag(board) == board[0, 0]) and board[0, 0] != 0:
    return board[0, 0]

  if np.all(np.diag(np.flipud(board)) == board[0, 2]) and board[0, 2] != 0:
    return board[0, 2]

  return 0

def print_board(board):
  for i in range(3):
    for j in range(3):
      if board[i, j] == 0:
        print(" ", end=" ")
      elif board[i, j] == 1:
        print("X", end=" ")
      else:
        print("O", end=" ")
    print()

def get_move(board, player):
  while True:
    print("Player", player, "turn:")
    move = input("Enter row and column (e.g. 1 2): ")
    try:
      row, col = map(int, move.split())
      if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid move. Please enter a valid row and column.")
        continue
      if board[row - 1, col - 1] != 0:
        print("That space is already taken. Please enter a valid move.")
        continue
      return row - 1, col - 1
    except ValueError:
      print("Invalid move. Please enter a valid row and column.")

def main():
  # Create a new game board
  board = np.zeros((3, 3), dtype=int)

  # Set the current player to 1 (X)
  player = 1

  # Loop until the game is over
  while True:
    # Get the player's move
    row, col = get_move(board, player)

    # Place the player's piece on the board
    board[row, col] = player

    # Check if the player has won
    winner = check_win(board)
    if winner != 0:
      print("Player", winner, "wins!")
      break

    # Check if the board is full
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch players
    player = 3 - player

    # Print the game board
    print_board(board)

if __name__ == "__main__":
  main()
