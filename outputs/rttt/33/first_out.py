# Create a 3x3 grid
grid = [[' ' for _ in range(3)] for _ in range(3)]

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Get the players' names
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")

# Function to check if a player has won
def check_win(symbol):
    # Check for horizontal wins
    for row in grid:
        if row[0] == row[1] == row[2] == symbol:
            return True

    # Check for vertical wins
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] == symbol:
            return True

    # Check for diagonal wins
    if grid[0][0] == grid[1][1] == grid[2][2] == symbol:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == symbol:
        return True

    # No win yet
    return False

# Function to print the grid
def print_grid():
    for row in grid:
        print(' '.join(row))

# Game loop
while True:
    # Get the current player's symbol
    if turn % 2 == 0:
        symbol = player1_symbol
    else:
        symbol = player2_symbol

    # Get the player's move
    while True:
        move = input("Enter your move (row, column): ")
        try:
            row, col = map(int, move.split(','))
            if 0 <= row < 3 and 0 <= col < 3 and grid[row][col] == ' ':
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid move. Try again.")

    # Place the player's symbol on the grid
    grid[row][col] = symbol

    # Print the grid
    print_grid()

    # Check if the player has won
    if check_win(symbol):
        if symbol == player1_symbol:
            print(f"{player1_name} wins!")
        else:
            print(f"{player2_name} wins!")
        break

    # Check if the game is a draw
    if all(all(cell != ' ' for cell in row) for row in grid):
        print("It's a draw!")
        break

    # Switch turns
    turn += 1
