
# Create a 10x10 grid
grid = [[' ' for _ in range(10)] for _ in range(10)]

# Define the players
player1 = 'X'
player2 = 'O'

# Define the current player
current_player = player1

# Game loop
while True:
    # Get the column where the player wants to place their piece
    column = int(input(f"{current_player}'s turn. Choose a column (1-10): ")) - 1

    # Check if the column is valid
    if column < 0 or column >= 10:
        print("Invalid column. Please choose a column between 1 and 10.")
        continue

    # Check if the column is full
    if grid[0][column] != ' ':
        print("This column is full. Please choose another column.")
        continue

    # Place the player's piece in the lowest free space of the column
    for i in range(9, -1, -1):
        if grid[i][column] == ' ':
            grid[i][column] = current_player
            break

    # Check if the player has won
    if has_won(grid, current_player):
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw
    if is_draw(grid):
        print("It's a draw!")
        break

    # Switch the current player
    current_player = player1 if current_player == player2 else player2

# Print the final grid
for row in grid:
    print(' '.join(row))


# Function to check if a player has won
def has_won(grid, player):
    # Check for horizontal wins
    for row in grid:
        if row.count(player) == 3:
            return True

    # Check for vertical wins
    for column in range(10):
        column_values = [row[column] for row in grid]
        if column_values.count(player) == 3:
            return True

    # Check for diagonal wins
    for i in range(7):
        # Check for diagonal wins from top left to bottom right
        diagonal_values = [grid[i+j][j] for j in range(10-i)]
        if diagonal_values.count(player) == 3:
            return True

        # Check for diagonal wins from bottom left to top right
        diagonal_values = [grid[i+j][9-j] for j in range(10-i)]
        if diagonal_values.count(player) == 3:
            return True

    return False


# Function to check if the game is a draw
def is_draw(grid):
    for row in grid:
        for cell in row:
            if cell == ' ':
                return False

    return True
