import numpy as np

def jdv():
  # Create a 3x3 grid
  grid = np.zeros((3, 3))

  # Set the player turn to 1 (player 1 starts)
  player_turn = 1

  # Game loop
  while True:
    # Get the player's move
    while True:
      try:
        move = int(input("Player {}'s turn: ".format(player_turn)))
        if 0 <= move < 9 and grid[move // 3, move % 3] == 0:
          break
        else:
          print("Invalid move. Please enter a number between 0 and 8 that corresponds to a free space on the grid.")
      except ValueError:
        print("Invalid input. Please enter a number.")

    # Place the player's piece on the grid
    grid[move // 3, move % 3] = player_turn

    # Check if the player has won
    if check_win(grid, player_turn):
      print("Player {} wins!".format(player_turn))
      break

    # Check if the game is a draw
    if np.all(grid != 0):
      print("Draw!")
      break

    # Switch the player turn
    player_turn = 3 - player_turn

# Function to check if a player has won
def check_win(grid, player):
  # Check for horizontal wins
  for i in range(3):
    if np.all(grid[i, :] == player):
      return True

  # Check for vertical wins
  for j in range(3):
    if np.all(grid[:, j] == player):
      return True

  # Check for diagonal wins
  if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
    return True

  # No win
  return False

def main():
  """
  Main function to start the game.
  """

  # Start the game
  jdv()

if __name__ == "__main__":
  main()
