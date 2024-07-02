def print_grid(grid):
    """Prints the current state of the grid."""
    for row in grid:
        print(" ".join(row))


def check_winner(grid):
    """Checks if there is a winner in the grid.

    Args:
        grid: The current state of the grid.

    Returns:
        The winner's symbol, or None if there is no winner yet.
    """

    # Check for horizontal wins
    for row in grid:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]

    # Check for vertical wins
    for col in range(3):
        column = [row[col] for row in grid]
        if len(set(column)) == 1 and column[0] != " ":
            return column[0]

    # Check for diagonal wins
    diagonals = [
        [grid[0][0], grid[1][1], grid[2][2]],
        [grid[0][2], grid[1][1], grid[2][0]],
    ]
    for diagonal in diagonals:
        if len(set(diagonal)) == 1 and diagonal[0] != " ":
            return diagonal[0]

    # No winner yet
    return None


def get_player_move(grid, player):
    """Gets the player's move.

    Args:
        grid: The current state of the grid.
        player: The player whose turn it is.

    Returns:
        The player's move as a tuple (row, col).
    """

    while True:
        move = input(f"Player {player}, enter your move (row, col): ")
        try:
            row, col = map(int, move.split(","))
        except ValueError:
            print("Invalid move. Please enter a valid row and column number.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move. Please enter a row and column number between 0 and 2.")
            continue

        if grid[row][col] != " ":
            print("Invalid move. That space is already taken.")
            continue

        return row, col


def main():
    """Runs the game."""

    # Create a new grid
    grid = [[" " for _ in range(3)] for _ in range(3)]

    # Print the initial grid
    print_grid(grid)

    # Get the players' names
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    # Set the current player to player 1
    current_player = player1

    # Game loop
    while True:
        # Get the player's move
        row, col = get_player_move(grid, current_player)

        # Update the grid
        grid[row][col] = current_player

        # Print the updated grid
        print_grid(grid)

        # Check for a winner
        winner = check_winner(grid)
        if winner is not None:
            print(f"Player {winner} wins!")
            break

        # Check for a draw
        if all(space != " " for row in grid for space in row):
            print("Draw!")
            break

        # Switch the current player
        current_player = player2 if current_player == player1 else player1


if __name__ == "__main__":
    main()
