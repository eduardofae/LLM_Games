import numpy as np

def print_grid(game_board):
  for row in game_board:
    print(' '.join([str(cell) for cell in row]))

def check_winner(game_board):
  # Check rows
  for row in game_board:
    if all(cell == row[0] for cell in row) and row[0] != 0:
      return row[0]

  # Check columns
  for col in range(len(game_board[0])):
    if all(game_board[row][col] == game_board[0][col] for row in range(len(game_board))) and game_board[0][col] != 0:
      return game_board[0][col]

  # Check diagonals
  if all(game_board[row][row] == game_board[0][0] for row in range(len(game_board))) and game_board[0][0] != 0:
    return game_board[0][0]
  if all(game_board[row][len(game_board)-row-1] == game_board[0][len(game_board)-1] for row in range(len(game_board))) and game_board[0][len(game_board)-1] != 0:
    return game_board[0][len(game_board)-1]

  # Check for draw
  if all(cell != 0 for row in game_board for cell in row):
    return -1

  # No winner yet
  return 0

def play_game():
  # Create a 3x3 game board
  game_board = np.zeros((3,3), dtype=int)

  # Create a class to represent each player
  class Player:
    def __init__(self, name, symbol):
      self.name = name
      self.symbol = symbol

  # Create two player objects
  player1 = Player("Player 1", "X")
  player2 = Player("Player 2", "O")

  # Player 1 starts
  current_player = player1

  # Play until there is a winner or a draw
  while True:
    # Print the game board and instructions
    print_grid(game_board)
    print(f"{current_player.name}'s turn. Enter your move (row, column):")

    # Get the player's move
    while True:
      try:
        row, col = map(int, input().split(','))
      except ValueError:
        print("Invalid move. Please enter a comma-separated pair of integers.")
        continue
      if not (0 <= row < 3 and 0 <= col < 3):
        print("Invalid move: row or column out of bounds.")
        continue
      if game_board[row, col] != 0:
        print("Invalid move: space already taken.")
        continue
      break

    # Place the player's piece in the game board
    game_board[row, col] = current_player.symbol

    # Check for a winner or a draw
    winner = check_winner(game_board)
    if winner != 0:
      print_grid(game_board)
      if winner == -1:
        print("Draw!")
      else:
        print(f"{current_player.name} wins!")
      break

    # Switch players
    current_player = player2 if current_player == player1 else player1

# Play the game
if __name__ == "__main__":
  play_game()
