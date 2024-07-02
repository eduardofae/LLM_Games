import numpy as np

def jdv():
  """
  This function implements the game jdv.

  The game is played on a 3x3 grid, and two players take turns placing
  their pieces in a free space on the grid. The first player to make a
  line of three adjacent pieces wins the game. If there are no more free
  spaces, the game is declared a draw.

  The function returns the winner of the game, or None if the game is a
  draw.
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3), dtype=int)

  # Get the player names
  player1 = input("Player 1 name: ")
  player2 = input("Player 2 name: ")

  # Set the player turn
  player_turn = 1

  # Play the game
  while True:
    # Get the player move
    if player_turn == 1:
      move = input(f"{player1}'s move: ")
    else:
      move = input(f"{player2}'s move: ")

    # Check if the move is valid
    if not move or move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      print("Invalid move.")
      continue

    # Convert the move to a grid index
    row = (int(move) - 1) // 3
    col = (int(move) - 1) % 3

    # Check if the space is free
    if grid[row, col] != 0:
      print("Space already occupied.")
      continue

    # Place the player's piece on the grid
    grid[row, col] = player_turn

    # Check if the player has won
    if check_win(grid, player_turn):
      if player_turn == 1:
        print(f"{player1} wins!")
      else:
        print(f"{player2} wins!")
      return player_turn

    # Check if the game is a draw
    if not np.any(grid == 0):
      print("Draw!")
      return None

    # Switch the player turn
    player_turn = 3 - player_turn


def check_win(grid, player_turn):
  """
  This function checks if the given player has won the game.

  The function takes a 3x3 grid and the player turn as input, and returns
  True if the player has won, or False otherwise.
  """

  # Check for a win in each row
  for row in range(3):
    if np.all(grid[row, :] == player_turn):
      return True

  # Check for a win in each column
  for col in range(3):
    if np.all(grid[:, col] == player_turn):
      return True

  # Check for a win in each diagonal
  if np.all(grid.diagonal() == player_turn):
    return True
  if np.all(np.flip(grid).diagonal() == player_turn):
    return True

  # No win
  return False


if __name__ == "__main__":
  jdv()
