import numpy as np

def jdv():
  """
  A simple 3x3 grid game where two players take turns placing their pieces in a free space until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line wins. If there are no more free spaces, the game is declared a draw.
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3), dtype=int)

  # Set player 1's piece to 1 and player 2's piece to 2
  player1_piece = 1
  player2_piece = 2

  # Set the current player to player 1
  current_player = player1_piece

  # Keep track of the number of moves made
  num_moves = 0

  # Keep track of the number of wins for each player
  player1_wins = 0
  player2_wins = 0

  # Loop until there is a winner or a draw
  while True:
    # Get the player's input
    while True:
      try:
        row, col = input("Enter the row and column (separated by a space) where you want to place your piece: ").split()
        row = int(row) - 1
        col = int(col) - 1

        # Check if the row and column numbers are valid
        if row < 0 or row > 2 or col < 0 or col > 2:
          print("Invalid row or column number. Please enter a number between 1 and 3.")
          continue

        # Check if the space is free
        if grid[row, col] == 0:
          break
        else:
          print("That space is already taken. Please choose another space.")
      except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")

    # Place the player's piece in the space
    grid[row, col] = current_player

    # Increment the number of moves made
    num_moves += 1

    # Check if the player has won
    if check_win(grid, current_player):
      if current_player == player1_piece:
        player1_wins += 1
      else:
        player2_wins += 1
      print(f"Player {current_player} wins!")
      break

    # Check if there is a draw
    if num_moves == 9:
      print("Draw!")
      break

    # Switch to the other player
    if current_player == player1_piece:
      current_player = player2_piece
    else:
      current_player = player1_piece

  # Reset the game
  grid = np.zeros((3, 3), dtype=int)
  current_player = player1_piece
  num_moves = 0

  # Play again?
  while True:
    play_again = input("Play again? (y/n) ").lower()
    if play_again == "y":
      jdv()
    elif play_again == "n":
      break
    else:
      print("Invalid input. Please enter 'y' or 'n'.")


def check_win(grid, player):
  """
  Checks if a player has won the game.

  Args:
    grid: The game grid.
    player: The player to check for a win.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row
  for row in range(3):
    if np.all(grid[row, :] == player):
      return True

  # Check for a win in each column
  for col in range(3):
    if np.all(grid[:, col] == player):
      return True

  # Check for a win in each diagonal
  if np.all(grid.diagonal() == player):
    return True
  if np.all(np.flip(grid, 1).diagonal() == player):
    return True

  # No win
  return False


if __name__ == "__main__":
  jdv()
