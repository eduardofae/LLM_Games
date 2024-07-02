import os

# Create a 3x3 grid
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Generate a list of the winning combinations
def generate_winning_combos():
    """
    Generate a list of all possible winning combinations in the game.

    Returns:
        A list of tuples, each representing a winning combination.
    """
    winning_combos = []
    for row in range(3):
        for col in range(3):
            for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8)]:
                if row in combo and col in combo:
                    winning_combos.append((row, col))
    return winning_combos

# Get the player's names
player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")

# Set the current player to player 1
current_player = player1

# Loop until the game is over
while True:
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display the game grid
    print("JDV (Three-in-a-Row)")
    print("-" * 15)
    for row in grid:
        print(" | ".join(row) + " |")
        print("-" * 15)

    # Get the player's move
    move = input(f"{current_player}, enter your move (row, column): ")

    # Check if the move is valid
    try:
        row, column = map(int, move.split(","))
        if row < 0 or row > 2 or column < 0 or column > 2:
            raise ValueError("Invalid move. Please enter a valid row and column within the bounds of the grid.")
        if grid[row][column] != ' ':
            raise ValueError("That space is already taken. Please try again.")
    except ValueError as e:
        print(e)
        continue

    # Place the player's piece in the grid
    grid[row][column] = current_player

    # Check if the player has won
    winning_combos = generate_winning_combos()
    for combo in winning_combos:
        if all(grid[r][c] == current_player for r, c in combo):
            # Clear the console screen
            os.system('cls' if os.name == 'nt' else 'clear')

            # Display the game grid
            print("JDV (Three-in-a-Row)")
            print("-" * 15)
            for row in grid:
                print(" | ".join(row) + " |")
                print("-" * 15)

            print(f"{current_player} wins!")
            break

    # Check if the game is a draw
    if all(space != ' ' for row in grid for space in row):
        # Clear the console screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Display the game grid
        print("JDV (Three-in-a-Row)")
        print("-" * 15)
        for row in grid:
            print(" | ".join(row) + " |")
            print("-" * 15)

        print("The game is a draw!")
        break

    # Switch the current player
    current_player = player2 if current_player == player1 else player1
