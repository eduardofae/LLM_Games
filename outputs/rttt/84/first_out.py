import numpy as np

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()

def check_winner(grid):
    # Check rows
    for row in grid:
        if all(cell == row[0] for cell in row) and row[0] != 0:
            return row[0]

    # Check columns
    for col in range(3):
        if all(grid[row][col] == grid[0][col] for row in range(3)) and grid[0][col] != 0:
            return grid[0][col]

    # Check diagonals
    if all(grid[i][i] == grid[0][0] for i in range(3)) and grid[0][0] != 0:
        return grid[0][0]
    if all(grid[i][2-i] == grid[0][2] for i in range(3)) and grid[0][2] != 0:
        return grid[0][2]

    # Check draw
    if all(cell != 0 for cell in grid.flatten()):
        return -1

    # No winner yet
    return 0

def play_jdv():
    grid = np.zeros((3, 3), dtype=int)
    player = 1  # Player 1 starts

    while True:
        print_grid(grid)

        # Get player's move
        while True:
            try:
                row, col = map(int, input("Player {}'s turn (row, col): ".format(player)).split())
                if 0 <= row < 3 and 0 <= col < 3 and grid[row, col] == 0:
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        # Place player's piece
        grid[row, col] = player

        # Check for winner or draw
        winner = check_winner(grid)
        if winner != 0:
            if winner == -1:
                print("Draw!")
            else:
                print("Player {} wins!".format(winner))
            break

        # Switch player
        player = 3 - player

if __name__ == "__main__":
    play_jdv()
