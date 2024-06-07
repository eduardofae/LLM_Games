# Create a 3x3 grid
grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

# Get the names of the players
player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")

# Set the current player to player 1
current_player = player1

# Main game loop
while True:
    # Display the grid
    print("Current grid:")
    for row in grid:
        print(" ".join(row))

    # Get the player's move
    move = input(f"{current_player}'s turn (row, column): ")
    row, column = map(int, move.split(","))

    # Check if the move is valid
    if grid[row][column] != ' ':
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the grid
    grid[row][column] = current_player

    # Check if the player has won
    if check_win(grid, current_player):
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw
    if all(all(cell != ' ' for cell in row) for row in grid):
        print("Draw!")
        break

    # Switch to the other player
    current_player = player2 if current_player == player1 else player1

# Check if the player has won
def check_win(grid, player):
    # Check for horizontal wins
    for row in grid:
        if all(cell == player for cell in row):
            return True

    # Check for vertical wins
    for i in range(3):
        if all(grid[j][i] == player for j in range(3)):
            return True

    # Check for diagonal wins
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True

    # No win yet
    return False
