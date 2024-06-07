import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, -1]

# Define the game loop
while True:
    # Get the current player
    player = players[0]

    # Get the player's move
    move = int(input("Player {}'s move (1-10): ".format(player))) - 1

    # Check if the move is valid
    if move < 0 or move > 9 or grid[9, move] != 0:
        print("Invalid move")
        continue

    # Place the player's piece on the grid
    for i in range(9, -1, -1):
        if grid[i, move] == 0:
            grid[i, move] = player
            break

    # Check if the player has won
    if abs(grid[i, move]) == 3:
        print("Player {} wins!".format(player))
        break

    # Check if there are no more free spaces
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch to the other player
    players.reverse()