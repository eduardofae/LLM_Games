import numpy as np

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def check_winner(grid):
    # Check rows
    for row in grid:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        column = [row[col] for row in grid]
        if len(set(column)) == 1 and column[0] != " ":
            return column[0]

    # Check diagonals
    diagonals = [[grid[0][0], grid[1][1], grid[2][2]],
                   [grid[0][2], grid[1][1], grid[2][0]]]
    for diagonal in diagonals:
        if len(set(diagonal)) == 1 and diagonal[0] != " ":
            return diagonal[0]

    return None

def play_jdv():
    grid = np.array([[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]])

    player = "X"

    while True:
        print_grid(grid)

        # Get player's move
        while True:
            try:
                row, col = map(int, input("Enter your move (row, column): ").split())
                if grid[row, col] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        # Update grid
        grid[row, col] = player

        # Check for winner
        winner = check_winner(grid)
        if winner is not None:
            print_grid(grid)
            print(f"{winner} wins!")
            break

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

        # Check for draw
        if np.all(grid != " "):
            print_grid(grid)
            print("Draw!")
            break

if __name__ == "__main__":
    play_jdv()
