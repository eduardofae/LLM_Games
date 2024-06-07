
import numpy as np

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()

def check_win(grid):
    # Check rows and columns
    for row in grid:
        if len(set(row)) == 1 and row[0] != 0:
            return True
    for col in range(10):
        column = [row[col] for row in grid]
        if len(set(column)) == 1 and column[0] != 0:
            return True

    # Check diagonals
    diagonals = [
        [grid[i][i] for i in range(10)],
        [grid[i][9-i] for i in range(10)]
    ]
    for diagonal in diagonals:
        if len(set(diagonal)) == 1 and diagonal[0] != 0:
            return True

    return False

def check_draw(grid):
    return np.all(grid != 0)

def main():
    grid = np.zeros((10, 10), dtype=int)

    player = 1
    while True:
        print_grid(grid)

        # Get player input
        while True:
            try:
                column = int(input(f"Player {player}, choose a column (0-9): "))
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 9.")
            else:
                if 0 <= column <= 9:
                    break
                else:
                    print("Invalid input. Please enter a number between 0 and 9.")

        # Check if the column is full
        if grid[0][column] != 0:
            print("Column is full. Please choose another column.")
            continue

        # Place the player's piece in the column
        for row in range(9, -1, -1):
            if grid[row][column] == 0:
                grid[row][column] = player
                break

        # Check if the player has won
        if check_win(grid):
            print_grid(grid)
            print(f"Player {player} wins!")
            break

        # Check if the game is a draw
        if check_draw(grid):
            print_grid(grid)
            print("Draw!")
            break

        # Switch player
        player = 3 - player

if __name__ == "__main__":
    main()
