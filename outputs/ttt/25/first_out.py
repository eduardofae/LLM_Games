import numpy as np

def jdv():
  # Create a 3x3 grid
  grid = np.zeros((3,3), dtype=int)

  # Define the players
  players = [1, 2]

  # Define the current player
  current_player = 0

  # Define the game loop
  while True:
    # Get the current player's move
    move = int(input("Player {}'s move (row, column): ".format(players[current_player])))

    # Convert the move to a row and column index
    row = move // 3
    column = move % 3

    # Check if the move is valid
    if grid[row, column] != 0:
      print("Invalid move")
      continue

    # Place the current player's piece on the grid
    grid[row, column] = players[current_player]

    # Check if the current player has won
    if check_win(grid, players[current_player]):
      print("Player {} wins!".format(players[current_player]))
      break

    # Check if the game is a draw
    if np.all(grid != 0):
      print("Draw!")
      break

    # Switch to the other player
    current_player = (current_player + 1) % 2


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
  if np.all(np.diag(grid) == player):
    return True

  if np.all(np.diag(np.flipud(grid)) == player):
    return True

  # No win
  return False


if __name__ == "__main__":
  jdv()
