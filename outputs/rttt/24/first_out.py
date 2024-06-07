def display_grid(grid):
    for row in grid:
        print(" | ".join(row))

def check_winner(grid):
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
    # Create a 3x3 grid
    grid = [[" " for _ in range(3)] for _ in range(3)]

    # Display the grid
    display_grid(grid)

    # Get the names of the players
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")

    # Set the current player to player 1
    current_player = player1

    # Play the game until there is a winner or a draw
    while True:
        # Get the player's move
        move = input(f"{current_player}'s move (row, column): ")
        row, col = map(int, move.split(","))

        # Check if the move is valid
        if grid[row][col] != " ":
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the grid
        grid[row][col] = current_player[0].upper()

        # Display the grid
        display_grid(grid)

        # Check if there is a winner or a draw
        winner = check_winner(grid)
        if winner is not None:
            if winner == "Draw":
                print("Draw!")
            else:
                print(f"{winner} wins!")
            break

        # Switch the current player
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    play_jdv()
