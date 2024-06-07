import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' turns
player1_turn = True
player2_turn = False

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

# Start the game
while True:
    # Check if it's player 1's turn
    if player1_turn:
        # Get the column where the player wants to place their piece
        column = int(input("Player 1, choose a column (0-9): "))

        # Check if the column is valid
        if column < 0 or column > 9:
            print("Invalid column. Please choose a column between 0 and 9.")
            continue

        # Check if the column is full
        if grid[:, column].all():
            print("Column is full. Please choose another column.")
            continue

        # Place the player's piece in the lowest free space of the column
        row = np.where(grid[:, column] == 0)[0][0]
        grid[row, column] = 1

        # Check if the player has won
        for winning_condition in winning_conditions:
            if all(grid[winning_condition[0][0], winning_condition[0][1]] == 1 for winning_condition in winning_conditions):
                print("Player 1 wins!")
                break

    # Check if it's player 2's turn
    else:
        # Get the column where the player wants to place their piece
        column = int(input("Player 2, choose a column (0-9): "))

        # Check if the column is valid
        if column < 0 or column > 9:
            print("Invalid column. Please choose a column between 0 and 9.")
            continue

        # Check if the column is full
        if grid[:, column].all():
            print("Column is full. Please choose another column.")
            continue

        # Place the player's piece in the lowest free space of the column
        row = np.where(grid[:, column] == 0)[0][0]
        grid[row, column] = 2

        # Check if the player has won
        for winning_condition in winning_conditions:
            if all(grid[winning_condition[0][0], winning_condition[0][1]] == 2 for winning_condition in winning_conditions):
                print("Player 2 wins!")
                break

    # Check if the game is a draw
    if grid.all():
        print("Draw!")
        break

    # Switch turns
    player1_turn = not player1_turn
    player2_turn = not player2_turn
