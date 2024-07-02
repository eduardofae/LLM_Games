# Create a 3x3 grid
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Create a list of the winning combinations
winning_combos = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)],
]

# Get the player's names
player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")

# Set the current player to player 1
current_player = player1

# Loop until the game is over
while True:
    # Get the player's move
    move = input(f"{current_player}, enter your move (row, column): ")
    row, column = map(int, move.split(","))

    # Check if the move is valid
    if grid[row][column] != ' ':
        print("That space is already taken. Please try again.")
        continue

    # Place the player's piece in the grid
    grid[row][column] = current_player

    # Check if the player has won
    for combo in winning_combos:
        if grid[combo[0][0]][combo[0][1]] == grid[combo[1][0]][combo[1][1]] == grid[combo[2][0]][combo[2][1]] != ' ':
            print(f"{current_player} wins!")
            break

    # Check if the game is a draw
    if all(space != ' ' for row in grid for space in row):
        print("The game is a draw!")
        break

    # Switch the current player
    current_player = player2 if current_player == player1 else player1
