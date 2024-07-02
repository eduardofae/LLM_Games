import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the game state
game_state = 'ongoing'

# Get the players' names
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")

# Start the game loop
while game_state == 'ongoing':
  # Get the player's move
  if game_state == 'ongoing':
    player1_move = input(f"{player1_name}'s turn. Enter the column number (1-10): ")
    player1_move = int(player1_move) - 1
    grid[9, player1_move] = 1
    game_state = check_winner(grid)
  if game_state == 'ongoing':
    player2_move = input(f"{player2_name}'s turn. Enter the column number (1-10): ")
    player2_move = int(player2_move) - 1
    grid[9, player2_move] = 2
    game_state = check_winner(grid)

# Print the final grid
print(grid)

# Print the winner
if game_state == 'draw':
  print("Draw!")
else:
  if grid[9, player1_move] == 1:
    print(f"{player1_name} wins!")
  else:
    print(f"{player2_name} wins!")

# Check if there is a winner
def check_winner(grid):
  # Check for a horizontal win
  for row in range(10):
    if all(grid[row, col] == grid[row, col+1] for col in range(7)):
      return 'win'

  # Check for a vertical win
  for col in range(10):
    if all(grid[row, col] == grid[row+1, col] for row in range(7)):
      return 'win'

  # Check for a diagonal win
  for row in range(7):
    for col in range(7):
      if all(grid[row+i, col+i] == grid[row+i+1, col+i+1] for i in range(3)):
        return 'win'

      if all(grid[row+i, col-i] == grid[row+i+1, col-i-1] for i in range(3)):
        return 'win'

  # Check for a draw
  if all(grid[row, col] != 0 for row in range(10) for col in range(10)):
    return 'draw'

  # No winner yet
  return 'ongoing'
