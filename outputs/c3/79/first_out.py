# Create a 10x10 grid
grid = [[' ' for _ in range(10)] for _ in range(10)]

# Define the players
player1 = 'X'
player2 = 'O'

# Set the current player to player 1
current_player = player1

# Main game loop
while True:
    # Get the column number from the current player
    column = int(input(f"{current_player}'s turn: "))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column number.")
        continue

    # Check if the column is full
    if grid[0][column] != ' ':
        print("Column is full.")
        continue

    # Place the current player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row][column] == ' ':
            grid[row][column] = current_player
            break

    # Check if the current player has won
    if check_for_win(grid, current_player):
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw
    if all(all(cell != ' ' for cell in row) for row in grid):
        print("Draw!")
        break

    # Switch the current player
    current_player = player2 if current_player == player1 else player1

# Print the grid
for row in grid:
    print(' '.join(row))

# Check for a win in the grid
def check_for_win(grid, player):
    # Check for a horizontal win
    for row in grid:
        if all(cell == player for cell in row):
            return True

    # Check for a vertical win
    for column in range(10):
        if all(grid[row][column] == player for row in range(10)):
            return True

    # Check for a diagonal win
    for i in range(10):
        if all(grid[i][i] == player for i in range(10)):
            return True
        if all(grid[i][9 - i] == player for i in range(10)):
            return True

    # No win found
    return False
