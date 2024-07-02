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
    diagonal1 = [grid[0][0], grid[1][1], grid[2][2]]
    diagonal2 = [grid[0][2], grid[1][1], grid[2][0]]
    if len(set(diagonal1)) == 1 and diagonal1[0] != " ":
        return diagonal1[0]
    if len(set(diagonal2)) == 1 and diagonal2[0] != " ":
        return diagonal2[0]

    # Check draw
    if " " not in [item for sublist in grid for item in sublist]:
        return "Draw"

    # No winner yet
    return None

def play_game():
    grid = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_grid(grid)
        row, col = map(int, input("Enter row and column: ").split())
        if grid[row][col] != " ":
            print("Invalid move")
            continue

        grid[row][col] = players[current_player]

        winner = check_winner(grid)
        if winner:
            print(f"{winner} wins!")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_game()
