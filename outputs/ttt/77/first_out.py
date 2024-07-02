# Game grid
grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

# Players' turns
player1 = True
player2 = False

# Main game loop
while True:
    # Print the game grid
    for row in grid:
        print(' '.join(row))

    # Get the player's move
    if player1:
        player = 'X'
    else:
        player = 'O'

    move = input(f"Player {player}, enter your move (row, column): ")
    row, column = map(int, move.split(','))

    # Check if the move is valid
    if grid[row][column] != ' ':
        print("Invalid move. Try again.")
        continue

    # Place the player's piece on the grid
    grid[row][column] = player

    # Check if the player has won
    if check_win(grid, player):
        print(f"Player {player} wins!")
        break

    # Check if there are no more free spaces
    if not any(' ' in row for row in grid):
        print("Draw!")
        break

    # Switch players
    player1, player2 = player2, player1


# Function to check if a player has won
def check_win(grid, player):
    # Check for a win in a row
    for row in grid:
        if all(cell == player for cell in row):
            return True

    # Check for a win in a column
    for column in range(3):
        if all(grid[row][column] == player for row in range(3)):
            return True

    # Check for a win in a diagonal
    if grid[0][0] == grid[1][1] == grid[2][2] == player:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True

    # No win yet
    return False
