import numpy as np

def print_grid(grid):
  for i in range(3):
    for j in range(3):
      print(grid[i][j], end=" ")
    print()

def check_winner(grid):
  # Check rows
  for i in range(3):
    if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != ' ':
      return grid[i][0]

  # Check columns
  for j in range(3):
    if grid[0][j] == grid[1][j] == grid[2][j] and grid[0][j] != ' ':
      return grid[0][j]

  # Check diagonals
  if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
    return grid[0][0]
  if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
    return grid[0][2]

  # Check for draw
  if not any(' ' in row for row in grid):
    return 'Draw'

  # No winner or draw yet
  return None

def play_jdv():
  # Create a 3x3 grid
  grid = [[' ' for _ in range(3)] for _ in range(3)]

  # Get player names
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Determine who goes first
  first_player = input("Who wants to go first? ({} or {}) ".format(player1, player2))

  # Keep track of the current player
  current_player = first_player

  # Play the game until there is a winner or draw
  while True:
    # Print the grid
    print_grid(grid)

    # Get the player's move
    row, col = map(int, input("{}, enter your move (row, column): ".format(current_player)).split())

    # Check if the move is valid
    if grid[row][col] != ' ':
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the grid
    grid[row][col] = current_player

    # Check if the player has won
    winner = check_winner(grid)
    if winner:
      print("{} wins!".format(winner))
      break

    # Switch to the other player
    current_player = player1 if current_player == player2 else player2

# Play the game
play_jdv()
