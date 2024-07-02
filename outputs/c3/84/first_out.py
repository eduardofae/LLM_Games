import numpy as np

def print_board(board):
  for row in board:
    for cell in row:
      print(cell, end=" ")
    print()

def check_win(board):
  # Check for horizontal wins
  for row in board:
    if len(set(row)) == 1 and row[0] != " ":
      return True

  # Check for vertical wins
  for col in range(len(board[0])):
    column = [row[col] for row in board]
    if len(set(column)) == 1 and column[0] != " ":
      return True

  # Check for diagonal wins
  diagonals = [
    [board[i][i] for i in range(len(board))],
    [board[i][len(board)-i-1] for i in range(len(board))],
  ]
  for diagonal in diagonals:
    if len(set(diagonal)) == 1 and diagonal[0] != " ":
      return True

  return False

def check_draw(board):
  return " " not in np.array(board).ravel()

def play_game():
  board = np.full((10, 10), " ")
  player = 1
  while True:
    print_board(board)
    print("Player", player, "turn")

    while True:
      try:
        col = int(input("Choose a column (0-9): "))
        if 0 <= col <= 9:
          break
        else:
          print("Invalid column")
      except ValueError:
        print("Invalid input")

    for row in range(len(board)-1, -1, -1):
      if board[row][col] == " ":
        board[row][col] = "X" if player == 1 else "O"
        break

    if check_win(board):
      print_board(board)
      print("Player", player, "wins!")
      break

    if check_draw(board):
      print_board(board)
      print("Draw!")
      break

    player = 2 if player == 1 else 1

if __name__ == "__main__":
  play_game()
