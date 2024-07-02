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

# Define the player pieces
player1_piece = 1
player2_piece = 2

# Define the game status
game_over = False
draw = False

# Start the game
while not game_over:
    # Check if it's player 1's turn
    if player1_turn:
        # Get the column where the player wants to place their piece
        while True:
            try:
                column = int(input("Player 1, choose a column (0-9): "))
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 9.")
                continue
            if column < 0 or column > 9:
                print("Invalid column. Please choose a column between 0 and 9.")
                continue
            if grid[:, column].all():
                print("Column is full. Please choose another column.")
                continue
            break

        # Place the player's piece in the lowest free space of the column
        row = np.where(grid[:, column] == 0)[0][0]
        grid[row, column] = player1_piece

        # Check if the player has won
        if check_win(grid, player1_piece, winning_conditions):
            print("Player 1 wins!")
            game_over = True
            break

    # Check if it's player 2's turn
    else:
        # Get the column where the player wants to place their piece
        while True:
            try:
                column = int(input("Player 2, choose a column (0-9): "))
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 9.")
                continue
            if column < 0 or column > 9:
                print("Invalid column. Please choose a column between 0 and 9.")
                continue
            if grid[:, column].all():
                print("Column is full. Please choose another column.")
                continue
            break

        # Place the player's piece in the lowest free space of the column
        row = np.where(grid[:, column] == 0)[0][0]
        grid[row, column] = player2_piece

        # Check if the player has won
        if check_win(grid, player2_piece, winning_conditions):
            print("Player 2 wins!")
            game_over = True
            break

    # Print the grid
    print(grid)

    # Check if the game is a draw
    if grid.all():
        print("Draw!")
        draw = True
        game_over = True

    # Switch turns
    player1_turn = not player1_turn
    player2_turn = not player2_turn

# Check if there was a draw
if draw:
    print("The game ended in a draw.")


# Function to check if a player has won
def check_win(grid, player_piece, winning_conditions):
    for winning_condition in winning_conditions:
        if all(grid[winning_condition[0][0], winning_condition[0][1]] == player_piece for winning_condition in winning_conditions):
            return True
    return False
