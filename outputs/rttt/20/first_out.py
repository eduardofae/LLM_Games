import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3))

# Create two players: "X" and "O"
players = ['X', 'O']

# Start the game
while True:
    # Get the current player
    player = players[0]

    # Get the player's move
    move = input(f"Player {player}, enter your move (row, column): ")
    row, column = map(int, move.split(','))

    # Check if the move is valid
    if grid[row, column] != 0:
        print("Invalid move. Try again.")
        continue

    # Place the player's piece on the grid
    grid[row, column] = player

    # Check if the player has won
    if check_win(grid, player):
        print(f"Player {player} has won!")
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("It's a draw!")
        break

    # Switch to the other player
    players = players[1:]

# Define the function to check if a player has won
def check_win(grid, player):
    # Check the rows
    for row in range(3):
        if np.all(grid[row, :] == player):
            return True

    # Check the columns
    for column in range(3):
        if np.all(grid[:, column] == player):
            return True

    # Check the diagonals
    if np.all(grid.diagonal() == player):
        return True
    if np.all(np.flip(grid).diagonal() == player):
        return True

    # No winner yet
    return False
