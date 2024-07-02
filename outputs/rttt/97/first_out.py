import numpy as np

def jdv():
  # Create a 3x3 grid
  grid = np.zeros((3, 3))

  # Get the player's names
  player1 = input("Player 1, enter your name: ")
  player2 = input("Player 2, enter your name: ")

  # Set the current player to player 1
  current_player = player1

  # Game loop
  while True:
    # Get the player's move
    move = input(f"{current_player}, enter your move (row, column): ")
    row, column = map(int, move.split(","))

    # Check if the move is valid
    if grid[row, column] != 0:
      print("Invalid move. That space is already taken.")
      continue

    # Place the player's piece in the grid
    grid[row, column] = 1 if current_player == player1 else 2

    # Check if the player has won
    if check_win(grid, current_player):
      print(f"{current_player} wins!")
      break

    # Check if the game is a draw
    if np.all(grid != 0):
      print("Draw!")
      break

    # Switch the current player
    current_player = player2 if current_player == player1 else player1

def check_win(grid, player):
  # Check for a win in each row
  for row in grid:
    if np.all(row == player):
      return True

  # Check for a win in each column
  for column in grid.T:
    if np.all(column == player):
      return True

  # Check for a win in each diagonal
  if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
    return True

  # No win found
  return False

# Play the game
jdv()
