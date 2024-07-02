import os

def display_grid(grid):
    """Displays the game grid."""
    print("+---+---+---+")
    for row in grid:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+")

def check_winner(grid):
    """Checks if there is a winner or a draw."""

    # Check rows
    for row in grid:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        column = [grid[0][col], grid[1][col], grid[2][col]]
        if len(set(column)) == 1 and column[0] != " ":
            return column[0]

    # Check diagonals
    diagonals = [[grid[0][0], grid[1][1], grid[2][2]],
                 [grid[0][2], grid[1][1], grid[2][0]]]
    for diagonal in diagonals:
        if len(set(diagonal)) == 1 and diagonal[0] != " ":
            return diagonal[0]

    # Check if there are no more free spaces
    if " " not in [item for sublist in grid for item in sublist]:
        return "Draw"

    # No winner yet
    return None

def play_jdv():
    """Plays the jdv game."""

    # Create a 3x3 grid
    grid = [[" " for _ in range(3)] for _ in range(3)]

    # Display the grid
    display_grid(grid)

    # Get the names of the players
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")

    # Set the current player to player 1
    current_player = player1

    # Set the initial move count to 0
    move_count = 0

    # Play the game until there is a winner or a draw
    while True:
        # Get the player's move
        while True:
            move = input(f"{current_player}'s move (row, column): ")
            try:
                row, col = map(int, move.split(","))
                if 0 <= row < 3 and 0 <= col < 3 and grid[row][col] == " ":
                    break
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid move. Please try again.")

        # Place the player's piece on the grid
        grid[row][col] = current_player[0].upper()

        # Increment the move count
        move_count += 1

        # Display the grid
        display_grid(grid)

        # Check if there is a winner or a draw
        winner = check_winner(grid)
        if winner is not None:
            if winner == "Draw":
                print("Draw!")
            else:
                print(f"{winner} wins in {move_count} moves!")
            break

        # Switch the current player
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    while True:
        play_jdv()
        again = input("Play again? (y/n): ")
        if again.lower() == "n":
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
