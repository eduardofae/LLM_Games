
import numpy as np

def print_board(board):
  for row in board:
    print(' '.join(row))

def check_winner(board):
  # Check for horizontal wins
  for row in board:
    if len(set(row)) == 1 and row[0] != '.':
      return row[0]

  # Check for vertical wins
  for col in range(len(board[0])):
    column = [row[col] for row in board]
    if len(set(column)) == 1 and column[0] != '.':
      return column[0]

  # Check for diagonal wins
  diagonals = [[board[i][i] for i in range(len(board))],
               [board[i][len(board)-i-1] for i in range(len(board))]]
  for diagonal in diagonals:
    if len(set(diagonal)) == 1 and diagonal[0] != '.':
      return diagonal[0]

  # Check for draw
  if '.' not in np.array(board).flatten():
    return 'Draw'

  # No winner yet
  return None

def main():
  # Create a 10x10 grid
  board = [['.' for _ in range(10)] for _ in range(10)]

  # Get the number of players
  num_players = int(input("Enter the number of players (2): "))

  # Get the player names
  player_names = [input("Enter player {}'s name: ".format(i+1)) for i in range(num_players)]

  # Get the starting player
  starting_player = int(input("Enter the starting player (1 or 2): ")) - 1

  # Play the game
  while True:
    # Print the board
    print_board(board)

    # Get the current player's move
    player = player_names[starting_player]
    print("{}'s turn: ".format(player))
    col = int(input("Enter a column (1-10): ")) - 1

    # Check if the move is valid
    if col < 0 or col > 9 or board[0][col] != '.':
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the board
    for i in range(9,-1,-1):
      if board[i][col] == '.':
        board[i][col] = player
        break

    # Check for a winner
    winner = check_winner(board)
    if winner:
      print_board(board)
      print("{} wins!".format(winner))
      break

    # Switch to the next player
    starting_player = (starting_player + 1) % num_players

if __name__ == "__main__":
  main()
