import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' turns
player1 = 1
player2 = -1

# Define the winning conditions
winning_conditions = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

# Main game loop
while True:
    # Get the player's move
    if player1 == 1:
        move = input("Player 1, enter your move (row, column): ")
    else:
        move = input("Player 2, enter your move (row, column): ")

    # Convert the move to a tuple
    move = tuple(int(x) for x in move.split(","))

    # Check if the move is valid
    if move[0] < 0 or move[0] > 9 or move[1] < 0 or move[1] > 9 or grid[move[0], move[1]] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the grid
    grid[move[0], move[1]] = player1

    # Check if the player has won
    for condition in winning_conditions:
        if all(grid[x, y] == player1 for x, y in condition):
            print("Player 1 wins!")
            break
    else:
        # Check if the game is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch the player's turns
        player1 = -player1
