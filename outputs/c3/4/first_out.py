import numpy as np

def print_board(board):
  for row in board:
    print(' '.join(row))

def check_win(board):
  # Check rows
  for row in board:
    if len(set(row)) == 1 and row[0] != ' ':
      return row[0]

  # Check columns
  for col in range(len(board[0])):
    column = [row[col] for row in board]
    if len(set(column)) == 1 and column[0] != ' ':
      return column[0]

  # Check diagonals
  diagonals = [
      [board[i][i] for i in range(len(board))],
      [board[i][len(board)-i-1] for i in range(len(board))]
  ]
  for diagonal in diagonals:
    if len(set(diagonal)) == 1 and diagonal[0] != ' ':
      return diagonal[0]

  # Check draw
  if all(row.count(' ') == 0 for row in board):
    return 'draw'

  # No win or draw yet
  return None


def play_game():
  # Create a 10x10 board
  board = np.full((10, 10), ' ')

  # Get player names
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")

  # Determine who goes first
  first_player = input("Who goes first? (1 or 2): ")
  if first_player == '1':
    current_player = player1_name
  else:
    current_player = player2_name

  # Game loop
  while True:
    # Print the board
    print_board(board)

    # Get the player's move
    column = int(input(f"{current_player}'s turn. Choose a column (1-10): ")) - 1

    # Check if the move is valid
    if column < 0 or column > 9 or board[0][column] != ' ':
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the board
    for row in range(9,-1,-1):
      if board[row][column] == ' ':
        board[row][column] = 'X' if current_player == player1_name else 'O'
        break

    # Check if the player has won
    winner = check_win(board)
    if winner:
      if winner == 'draw':
        print("Draw!")
      else:
        print(f"{winner} wins!")
      break

    # Switch players
    if current_player == player1_name:
      current_player = player2_name
    else:
      current_player = player1_name


if __name__ == "__main__":
  play_game()
