import numpy as np

def jdv():
  """
  This function plays a game of jdv, a 2-player game where players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line wins. If there are no more free spaces, the game is declared a draw.
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3))

  # Set the current player to 1
  current_player = 1

  # While there are no winners and free spaces
  while not check_winner(grid) and not check_draw(grid):
    # Get the current player's move
    move = get_move(grid, current_player)

    # Place the current player's piece in the grid
    grid[move[0], move[1]] = current_player

    # Print the current state of the grid
    print_grid(grid)

    # Switch the current player
    current_player = 3 - current_player

  # Check if there is a winner
  if check_winner(grid):
    print(f"Player {current_player} wins!")
  else:
    print("Draw!")

def get_move(grid, player):
  """
  This function gets the player's move.

  Args:
    grid: The current state of the grid.
    player: The player whose turn it is.

  Returns:
    A tuple representing the row and column of the player's move.
  """

  # Get the player's input
  while True:
    try:
      move = input(f"Player {player}, enter your move (row, column): ")
      move = tuple(int(x) - 1 for x in move.split(","))

      # Check if the move is valid
      if not is_valid_move(grid, move):
        print("Invalid move. Please enter a number between 1 and 3 for both row and column.")
      else:
        return move
    except ValueError:
      print("Invalid input. Please enter two numbers separated by a comma.")

def check_winner(grid):
  """
  This function checks if there is a winner.

  Args:
    grid: The current state of the grid.

  Returns:
    True if there is a winner, False otherwise.
  """

  # Check for horizontal wins
  for row in grid:
    if np.all(row == row[0]) and row[0] != 0:
      return True

  # Check for vertical wins
  for col in grid.T:
    if np.all(col == col[0]) and col[0] != 0:
      return True

  # Check for diagonal wins
  if np.all(grid.diagonal() == grid.diagonal()[0]) and grid.diagonal()[0] != 0:
    return True
  if np.all(np.flip(grid).diagonal() == np.flip(grid).diagonal()[0]) and np.flip(grid).diagonal()[0] != 0:
    return True

  # No winner yet
  return False

def check_draw(grid):
  """
  This function checks if the game is a draw.

  Args:
    grid: The current state of the grid.

  Returns:
    True if the game is a draw, False otherwise.
  """

  return np.all(grid != 0)

def print_grid(grid):
  """
  This function prints the current state of the grid.

  Args:
    grid: The current state of the grid.
  """

  for row in grid:
    for cell in row:
      if cell == 0:
        print(" ", end=" ")
      else:
        print(cell, end=" ")
    print()

def is_valid_move(grid, move):
  """
  This function checks if a move is valid.

  Args:
    grid: The current state of the grid.
    move: A tuple representing the row and column of the move.

  Returns:
    True if the move is valid, False otherwise.
  """

  # Check if the move is within the bounds of the grid
  if not (0 <= move[0] < 3 and 0 <= move[1] < 3):
    return False

  # Check if the space is empty
  if grid[move[0], move[1]] != 0:
    return False

  # The move is valid
  return True

def reset_game():
  """
  This function resets the game.
  """

  # Create a new 3x3 grid
  grid = np.zeros((3, 3))

  # Set the current player to 1
  current_player = 1

  # Return the new grid and current player
  return grid, current_player

# Play the game
while True:
  # Get the current state of the grid and the current player
  grid, current_player = jdv()

  # Check if the game is over
  if check_winner(grid) or check_draw(grid):
    # Ask the players if they want to play again
    play_again = input("Do you want to play again? (y/n) ")

    # If the players want to play again, reset the game
    if play_again == "y":
      grid, current_player = reset_game()
    else:
      break
