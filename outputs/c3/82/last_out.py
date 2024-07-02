import numpy as np

def print_board(board):
  for row in board:
    print(' '.join(row))

def check_win(board):
  # Check for horizontal wins
  for row in board:
    if len(set(row)) == 1 and row[0] != ' ':
      return True

  # Check for vertical wins
  for col in range(len(board[0])):
    column = [row[col] for row in board]
    if len(set(column)) == 1 and column[0] != ' ':
      return True

  # Check for diagonal wins
  diagonals = [
    [board[i][i] for i in range(len(board))],
    [board[i][len(board)-i-1] for i in range(len(board))]
  ]
  for diagonal in diagonals:
    if len(set(diagonal)) == 1 and diagonal[0] != ' ':
      return True

  # Check for draw
  if np.all(board != ' '):
    return 'draw'

  # No win or draw yet
  return False

def get_valid_moves(board):
  valid_moves = []
  for col in range(len(board[0])):
    if board[0][col] == ' ':
      valid_moves.append(col)
  return valid_moves

def make_move(board, player, col):
  for i in range(len(board)-1, -1, -1):
    if board[i][col] == ' ':
      board[i][col] = player
      break

def is_game_over(board):
  return check_win(board) or np.all(board != ' ')

def reset_board(board):
  board[:] = ' '

def display_winner(player):
  print(f"Player {player} wins!")

def play_game():
  # Create a new game board
  board = np.full((10, 10), ' ')

  # Set the current player to 1
  player = 1

  # Loop until the game is over
  while not is_game_over(board):
    # Print the game board
    print_board(board)

    # Get the valid moves for the current player
    valid_moves = get_valid_moves(board)

    # If there are no valid moves, the game is a draw
    if not valid_moves:
      print("It's a draw!")
      break

    # Get the player's move
    while True:
      try:
        move = int(input(f"Player {player}, choose a column (1-{len(board[0])}): ")) - 1
        if move not in valid_moves:
          print("Invalid move. Please choose a valid column.")
          continue
        break
      except ValueError:
        print("Invalid input. Please enter a number.")

    # Make the move
    make_move(board, player, move)

    # Check if the move resulted in a win or a draw
    result = check_win(board)
    if result:
      if result == 'draw':
        print("It's a draw!")
      else:
        display_winner(player)
      break

    # Switch to the other player
    player = 2 if player == 1 else 1

  # Reset the game board for the next game
  reset_board(board)

if __name__ == "__main__":
  play_game()
