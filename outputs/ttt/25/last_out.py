import numpy as np

def jdv():
  # Create a 3x3 grid
  grid = np.zeros((3,3), dtype=int)

  # Define the players
  players = [1, 2]

  # Define the current player
  current_player = 0

  # Define the number of wins for each player
  wins = {1: 0, 2: 0}

  # Welcome message and instructions
  print("Welcome to JDV!")
  print("Instructions:")
  print("1. Players take turns placing their pieces on the grid.")
  print("2. The first player to get three of their pieces in a row, column, or diagonal wins.")
  print("3. If all spaces are filled and there is no winner, the game is a draw.")

  # Game loop
  while True:
    # Get the current player's move
    move = input("Player {}'s move (row, column): ".format(players[current_player]))

    # Validate the input
    try:
      row, column = map(int, move.split(","))
      if row < 0 or row > 2 or column < 0 or column > 2:
        raise ValueError("Invalid move: Coordinates must be between 0 and 2")
      if grid[row, column] != 0:
        raise ValueError("Invalid move: Space is already occupied")
    except ValueError:
      print("Invalid move: Please enter coordinates in the format 'row, column'")
      continue

    # Place the current player's piece on the grid
    grid[row, column] = players[current_player]

    # Check if the current player has won
    if check_win(grid, players[current_player]):
      print("Player {} wins!".format(players[current_player]))
      wins[players[current_player]] += 1
      break

    # Check if the game is a draw
    if np.all(grid != 0):
      print("Draw!")
      break

    # Switch to the other player
    current_player = (current_player + 1) % 2

  # Print the number of wins for each player
  print("Wins:")
  for player, wins in wins.items():
    print("Player {}: {}".format(player, wins))

  # Ask if the players want to play again
  play_again = input("Do you want to play again? (y/n) ")
  if play_again == "y":
    jdv()
  else:
    print("Thanks for playing!")


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
