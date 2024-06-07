
# Create a 3x3 grid
grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

# Get player names
player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")

# Set player symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Set current player
current_player = player1

# Game loop
while True:
    # Print the grid
    print("Current grid:")
    for row in grid:
        print(' '.join(row))

    # Get player input
    row = int(input("Enter row (1-3): "))
    col = int(input("Enter column (1-3): "))

    # Check if the space is free
    if grid[row-1][col-1] == '-':
        # Place the player's symbol in the space
        grid[row-1][col-1] = current_player

        # Check if the player has won
        if check_win(grid, current_player):
            print(f"{current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw(grid):
            print("It's a draw!")
            break

        # Switch the current player
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
    else:
        print("Invalid move. Please try again.")

# Check if a player has won
def check_win(grid, player):
    # Check horizontally
    for row in grid:
        if all(element == player for element in row):
            return True

    # Check vertically
    for col in range(3):
        if all(grid[row][col] == player for row in range(3)):
            return True

    # Check diagonally
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True

    return False

# Check if the game is a draw
def check_draw(grid):
    for row in grid:
        for element in row:
            if element == '-':
                return False
    return True
