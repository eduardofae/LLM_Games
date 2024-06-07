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
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move: Row or column out of bounds")
            continue
        if grid[row][col] != " ":
            print("Invalid move: Cell already occupied")
            continue

        grid[row][col] = players[current_player]

        winner = check_winner(grid)
        if winner:
            print(f"{winner} wins!")
            break

        current_player = (current_player + 1) % 2

    while True:
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            play_game()
        else:
            break

if __name__ == "__main__":
    play_game()
