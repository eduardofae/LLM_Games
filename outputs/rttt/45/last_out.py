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
            if not (0 <= row <= 2 and 0 <= col <= 2):
                raise ValueError("Invalid coordinates. Please enter a valid row and column (0-2).")
            if grid[row][col] != ' ':
                raise ValueError("Space already occupied. Please choose an empty space.")
        except ValueError as e:
            print(e)
            continue
        else:
            return row, col

# Function to reset the game
def play_again():
    for row in range(3):
        for col in range(3):
            grid[row][col] = ' '

# AI opponent (simple strategy)
def ai_move():
    # Check if there is a winning move
    for row in range(3):
        for col in range(3):
            if grid[row][col] == ' ':
                grid[row][col] = 'O'
                if check_win('O'):
                    return
                else:
                    grid[row][col] = ' '

    # Check if there is a blocking move
    for row in range(3):
        for col in range(3):
            if grid[row][col] == ' ':
                grid[row][col] = 'X'
                if check_win('X'):
                    grid[row][col] = 'O'
                    return
                else:
                    grid[row][col] = ' '

    # Choose a random empty space
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if grid[row][col] == ' ':
            grid[row][col] = 'O'
            return

# Undo move (up to 3 moves)
undo_stack = []
def undo_move():
    if len(undo_stack) > 0:
        row, col, player = undo_stack.pop()
        grid[row][col] = ' '
        if player == 'X':
            players[0], players[1] = players[1], players[0]

# Main game loop
while True:
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the grid
    print_grid()

    # Get the move from the current player
    if players[0] == 'X':
        row, col = get_move(players[0])
    else:
        ai_move()

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

    # Push the current move to the undo stack
    undo_stack.append((row, col, players[0]))

    # Ask if the players want to play again
    play_again_input = input("Do you want to play again? (y/n) ")
    if play_again_input.lower() == 'y':
        play_again()
    else:
        break
