import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
player1 = 1
player2 = 2

# Define the game loop
while True:
    # Get the player's move
    while True:
        try:
            move = int(input("Player {}'s turn. Enter a column number (1-10): ".format(player1 if player1 == 1 else player2))) - 1
            if move < 0 or move > 9:
                raise ValueError
            break
        except ValueError:
            print("Invalid move. Please try again.")

    # Check if the move is valid
    if grid[9, move] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the grid
    for i in range(9, -1, -1):
        if grid[i, move] == 0:
            grid[i, move] = player1 if player1 == 1 else player2
            break

    # Check if the player has won
    if np.any(np.all(grid == player1, axis=0)) or np.any(np.all(grid == player2, axis=1)) or np.any(np.all(np.diag(grid) == player1)) or np.any(np.all(np.diag(np.fliplr(grid)) == player1)):
        print("Player {} wins!".format(player1 if player1 == 1 else player2))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch players
    player1, player2 = player2, player1
