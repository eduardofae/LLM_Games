import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' turns
player1_turn = True
player2_turn = False

# Define the winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                       (0, 3, 6), (1, 4, 7), (2, 5, 8),
                       (0, 4, 8), (2, 4, 6)]

# Start the game loop
while True:
    # Print the grid
    print(grid)

    # Get the player's move
    if player1_turn:
        move = input("Player 1, enter a column number (0-9): ")
    else:
        move = input("Player 2, enter a column number (0-9): ")

    # Check if the move is valid
    if move not in range(0, 10) or grid[0][int(move)] != 0:
        print("Invalid move. Please enter a valid column number.")
        continue

    # Place the player's piece in the grid
    for i in range(9, -1, -1):
        if grid[i][int(move)] == 0:
            if player1_turn:
                grid[i][int(move)] = 1
            else:
                grid[i][int(move)] = 2
            break

    # Check if the player has won
    for combination in winning_combinations:
        if grid[combination[0]][combination[1]][combination[2]] == grid[combination[0]][combination[1]][combination[2]] != 0:
            if player1_turn:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch the player's turns
    player1_turn = not player1_turn
    player2_turn = not player2_turn
