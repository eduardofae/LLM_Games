def jdv():
    # Create a 3x3 grid
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    # Get the names of the two players
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    # Determine who goes first
    turn = 1

    # Game loop
    while True:
        # Print the grid
        print("Current grid:")
        for row in grid:
            print(" ".join(row))

        # Get the player's move
        if turn == 1:
            row = int(input(f"{player1}, enter the row (1-3): "))
            col = int(input(f"{player1}, enter the column (1-3): "))
        else:
            row = int(input(f"{player2}, enter the row (1-3): "))
            col = int(input(f"{player2}, enter the column (1-3): "))

        # Check if the move is valid
        if grid[row - 1][col - 1] != ' ':
            print("Invalid move. That space is already occupied.")
            continue

        # Place the player's piece in the grid
        if turn == 1:
            grid[row - 1][col - 1] = 'X'
        else:
            grid[row - 1][col - 1] = 'O'

        # Check if the player has won
        if check_win(grid):
            if turn == 1:
                print(f"{player2} wins!")
            else:
                print(f"{player1} wins!")
            break

        # Check if the game is a draw
        if check_draw(grid):
            print("Draw!")
            break

        # Switch turns
        turn *= -1

def check_win(grid):
    # Check for a win in the rows
    for row in grid:
        if row[0] != ' ' and row[0] == row[1] and row[1] == row[2]:
            return True

    # Check for a win in the columns
    for col in range(3):
        if grid[0][col] != ' ' and grid[0][col] == grid[1][col] and grid[1][col] == grid[2][col]:
            return True

    # Check for a win in the diagonals
    if grid[0][0] != ' ' and grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
        return True
    if grid[0][2] != ' ' and grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
        return True

    # No win yet
    return False

def check_draw(grid):
    # Check if there are any empty spaces left
    for row in grid:
        for space in row:
            if space == ' ':
                return False

    # No empty spaces left, so it's a draw
    return True

if __name__ == "__main__":
    jdv()
