import numpy as np

def print_board(board):
  for row in board:
    print(" ".join(row))

def check_winner(board):
  # Check for horizontal wins
  for row in board:
    if len(set(row)) == 1 and row[0] != " ":
      return row[0]

  # Check for vertical wins
  for col in range(10):
    column = [board[row][col] for row in range(10)]
    if len(set(column)) == 1 and column[0] != " ":
      return column[0]

  # Check for diagonal wins
  diagonals = [
    [board[row][row] for row in range(10)],
    [board[row][9 - row] for row in range(10)]
  ]
  for diagonal in diagonals:
    if len(set(diagonal)) == 1 and diagonal[0] != " ":
      return diagonal[0]

  # Check for draw
  if " " not in np.array(board).flatten():
    return "Draw"

  # No winner yet
  return None

def main():
  # Create a 10x10 board
  board = np.full((10, 10), " ", dtype=str)

  # Player 1 is 'X', player 2 is 'O'
  players = ['X', 'O']
  current_player = 0

  # Number of turns
  turn_count = 0

  # Main game loop
  while True:
    # Print the board
    print_board(board)

    # Get the player's move
    try:
      col = int(input(f"Player {players[current_player]}, choose a column (0-9): "))
    except ValueError:
      print("Invalid input. Please enter a number between 0 and 9.")
      continue

    # Check if the move is valid
    if col < 0 or col > 9 or board[9][col] != " ":
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board
    for row in range(9, -1, -1):
      if board[row][col] == " ":
        board[row][col] = players[current_player]
        break

    # Check if there is a winner
    winner = check_winner(board)
    if winner:
      print_board(board)
      print(f"Player {winner} wins!")
      break

    # Check for a draw
    turn_count += 1
    if turn_count == 100:
      print_board(board)
      print("Draw!")
      break

    # Switch to the other player
    current_player = (current_player + 1) % 2

if __name__ == "__main__":
  main()
