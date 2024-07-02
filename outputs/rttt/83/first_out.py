
import numpy as np

def print_board(board):
  for i in range(3):
    for j in range(3):
      print(board[i][j], end=" ")
    print()

def check_winner(board):
  # Check rows
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != 0:
      return board[i][0]

  # Check columns
  for j in range(3):
    if board[0][j] == board[1][j] == board[2][j] != 0:
      return board[0][j]

  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] != 0:
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] != 0:
    return board[0][2]

  # Check draw
  if np.all(board != 0):
    return 3

  # No winner yet
  return 0

def main():
  # Create a 3x3 board
  board = np.zeros((3, 3), dtype=int)

  # Player 1 starts
  player = 1

  while True:
    # Print the board
    print_board(board)

    # Get the player's move
    row = int(input("Player {} enter row: ".format(player)))
    col = int(input("Player {} enter column: ".format(player)))

    # Check if the move is valid
    if board[row][col] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board
    board[row][col] = player

    # Check if there is a winner
    winner = check_winner(board)

    # If there is a winner, print the winner and break out of the loop
    if winner != 0:
      if winner == 3:
        print("Draw!")
      else:
        print("Player {} wins!".format(winner))
      break

    # Switch players
    player = 3 - player

if __name__ == "__main__":
  main()
