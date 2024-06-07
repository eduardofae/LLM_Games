import os

# Create a 3x3 grid
grid = [[' ' for _ in range(3)] for _ in range(3)]

# Define player turns
players = ['X', 'O']

# Function to print the grid
def print_grid():
    for row in grid:
        print(' | '.join(row))

# Function to check if a player has won
def check_win(player):
    # Check rows
    for row in grid:
        if all(x == player for x in row):
            return True
    # Check columns
    for col in range(3):
        if all(grid[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True

    # No winner yet
    return False

# Function to get a valid move from the player
def get_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row, column): ")
            row, col = map(int, move.split(','))
            if row < 0 or row > 2 or col < 0 or col > 2:
                raise ValueError
            if grid[row][col] != ' ':
                raise ValueError
        except ValueError:
            print("Invalid move. Please try again.")
            continue
        else:
            return row, col


# Main game loop
while True:
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the grid
    print_grid()

    # Get the move from the current player
    row, col = get_move(players[0])

    # Place the player's piece on the grid
    grid[row][col] = players[0]

    # Check if the player has won
    if check_win(players[0]):
        print(f"Player {players[0]} wins!")
        break

    # Check if the grid is full
    if all(x != ' ' for row in grid for x in row):
        print("Draw!")
        break

    # Swap players
    players[0], players[1] = players[1], players[0]
