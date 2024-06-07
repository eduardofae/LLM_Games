# Create a 10x10 grid
grid = [[' ' for _ in range(10)] for _ in range(10)]

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the current player
current_player = player1_symbol

# Define the game loop
while True:
    # Get the player's input
    column = int(input(f"{current_player}'s turn. Enter a column number (0-9): "))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column number. Please enter a number between 0 and 9.")
        continue

    # Check if the column is full
    if all(space != ' ' for space in grid[column]):
        print("That column is full. Please choose another column.")
        continue

    # Find the lowest free space in the column
    row = 9
    while row >= 0 and grid[row][column] != ' ':
        row -= 1

    # Place the player's piece in the grid
    grid[row][column] = current_player

    # Check if the player has won
    if check_for_win(grid, current_player):
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw
    if all(space != ' ' for space in [space for row in grid for space in row]):
        print("Draw!")
        break

    # Switch to the other player
    if current_player == player1_symbol:
        current_player = player2_symbol
    else:
        current_player = player1_symbol

# Define the function to check for a win
def check_for_win(grid, player_symbol):
    # Check for a horizontal win
    for row in grid:
        if all(space == player_symbol for space in row):
            return True

    # Check for a vertical win
    for column in range(10):
        if all(grid[row][column] == player_symbol for row in range(10)):
            return True

    # Check for a diagonal win (top-left to bottom-right)
    for i in range(10):
        if all(grid[i][i] == player_symbol for i in range(10)):
            return True

    # Check for a diagonal win (top-right to bottom-left)
    for i in range(10):
        if all(grid[i][9-i] == player_symbol for i in range(10)):
            return True

    # No win found
    return False
