import os

# Create a 10x10 grid
grid = [[' ' for _ in range(10)] for _ in range(10)]

# Create a list of players
players = ['X', 'O']

# Get the current player's index
current_player_index = 0

# Get the current player's symbol
current_player_symbol = players[current_player_index]

# Print the grid
print_grid(grid)

# Game loop
while True:
    # Get the column number from the current player
    while True:
        try:
            column_number = int(input(f"{current_player_symbol}'s turn. Enter a column number (1-10): ")) - 1
            if 0 <= column_number <= 9:
                break
            else:
                print("Invalid column number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 10.")

    # Check if the column is full
    if grid[0][column_number] != ' ':
        print("Column is full. Please try again.")
        continue

    # Place the current player's symbol in the lowest free space of the column
    for row_number in range(9, -1, -1):
        if grid[row_number][column_number] == ' ':
            grid[row_number][column_number] = current_player_symbol
            break

    # Print the grid
    print_grid(grid)

    # Check if the current player has won
    if check_win(grid, current_player_symbol):
        print(f"{current_player_symbol} wins!")
        break

    # Check if the game is a draw
    if check_draw(grid):
        print("Draw!")
        break

    # Switch the current player
    current_player_index = (current_player_index + 1) % len(players)
    current_player_symbol = players[current_player_index]

# Define the print_grid() function
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Define the check_win() function
def check_win(grid, symbol):
    # Check for horizontal win
    for row in grid:
        if row.count(symbol) == 3:
            return True

    # Check for vertical win
    for column_number in range(10):
        column = [grid[row_number][column_number] for row_number in range(10)]
        if column.count(symbol) == 3:
            return True

    # Check for diagonal win
    for row_number in range(7):
        for column_number in range(7):
            diagonal = [grid[row_number + i][column_number + i] for i in range(3)]
            if diagonal.count(symbol) == 3:
                return True

    return False

# Define the check_draw() function
def check_draw(grid):
    for row in grid:
        if ' ' in row:
            return False
    return True

# Define the restart_game() function
def restart_game():
    global grid, current_player_index, current_player_symbol
    grid = [[' ' for _ in range(10)] for _ in range(10)]
    current_player_index = 0
    current_player_symbol = players[current_player_index]
    print_grid(grid)

# Play the game
while True:
    # Get user input for whether to restart the game
    while True:
        restart = input("Enter 'y' to restart the game or any other key to exit: ")
        if restart == 'y':
            restart_game()
            break
        else:
            exit()
