import numpy as np

def create_board():
  """Creates a new 3x3 game board."""
  board = np.zeros((3, 3))
  return board

def print_board(board):
  """Prints the current game board."""
  for row in board:
    for cell in row:
      if cell == 0:
        print(" ", end=" ")
      elif cell == 1:
        print("X", end=" ")
      else:
        print("O", end=" ")
    print()

def is_valid_move(board, row, col):
  """Checks if the given move is valid."""
  if row < 0 or row >= 3 or col < 0 or col >= 3:
    return False
  if board[row][col] != 0:
    return False
  return True

def make_move(board, player, row, col):
  """Makes the given move on the game board."""
  if not is_valid_move(board, row, col):
    raise ValueError("Invalid move.")
  board[row][col] = player

def check_win(board, player):
  """Checks if the given player has won the game."""
  # Check rows
  for row in board:
    if np.all(row == player):
      return True
  # Check columns
  for col in range(3):
    if np.all(board[:, col] == player):
      return True
  # Check diagonals
  if np.all(np.diagonal(board) == player) or np.all(np.flipud(board).diagonal() == player):
    return True
  return False

def main():
  """Plays the game."""
  # Create the game board
  board = create_board()

  # Get the player names
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")

  # Start the game loop
  while True:
    # Print the game board
    print_board(board)

    # Get the move from player 1
    player1_row = int(input(f"{player1_name}'s turn. Row: "))
    player1_col = int(input("Col: "))

    # Make the move
    make_move(board, 1, player1_row, player1_col)

    # Check if player 1 has won
    if check_win(board, 1):
      print(f"{player1_name} wins!")
      break

    # Get the move from player 2
    player2_row = int(input(f"{player2_name}'s turn. Row: "))
    player2_col = int(input("Col: "))

    # Make the move
    make_move(board, 2, player2_row, player2_col)

    # Check if player 2 has won
    if check_win(board, 2):
      print(f"{player2_name} wins!")
      break

    # Check if the game is a draw
    if np.all(board != 0):
      print("Draw!")
      break

if __name__ == "__main__":
  main()
