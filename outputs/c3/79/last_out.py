import sys

# Create a 10x10 grid
grid = [[' ' for _ in range(10)] for _ in range(10)]

# Define the players
player1 = 'X'
player2 = 'O'

# Set the current player to player 1
current_player = player1

# Main game loop
while True:
    # Print the grid
    print("Connect Four Grid:")
    for row in grid:
        print(' '.join(row))

    # Get the column number from the current player
    while True:
        try:
            column = int(input(f"{current_player}'s turn: "))
        except ValueError:
            print("Invalid column number. Please enter a number between 0 and 9.")
            continue
        if column < 0 or column > 9:
            print("Invalid column number. Please enter a number between 0 and 9.")
            continue
        if grid[0][column] != ' ':
            print("Column is full. Please choose another column.")
            continue
        break

    # Place the current player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row][column] == ' ':
            grid[row][column] = current_player
            break

    # Check if the current player has won
    if check_for_winning_line(grid, current_player):
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw
    if all(all(cell != ' ' for cell in row) for row in grid):
        print("Draw!")
        break

    # Switch the current player
    current_player = player2 if current_player == player1 else player1

# Check for a winning line in the grid
def check_for_winning_line(grid, player):
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

    # No winning line found
    return False

# Ask the user if they want to play again
while True:
    play_again = input("Play again? (y/n): ")
    if play_again == 'y':
        # Reset the grid and start a new game
        grid = [[' ' for _ in range(10)] for _ in range(10)]
        current_player = player1
    elif play_again == 'n':
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
