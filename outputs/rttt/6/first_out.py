def jdv():
    # Create a 3x3 grid
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    # Get player names
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")

    # Choose player 1 symbol
    player1_symbol = input(f"{player1}, choose your symbol (X or O): ")
    while player1_symbol.upper() not in ["X", "O"]:
        player1_symbol = input("Invalid symbol. Choose again (X or O): ")

    # Player 2 symbol is the opposite of player 1 symbol
    player2_symbol = "X" if player1_symbol == "O" else "O"

    # Start the game loop
    current_player = player1
    while True:
        # Print the grid
        print("Current grid:")
        for row in grid:
            print(" ".join(row))

        # Get the player's move
        row, column = map(int, input(f"{current_player}, enter your move (row, column): ").split())
        while row < 0 or row > 2 or column < 0 or column > 2 or grid[row][column] != ' ':
            row, column = map(int, input("Invalid move. Enter again (row, column): ").split())

        # Place the player's symbol in the grid
        grid[row][column] = player1_symbol if current_player == player1 else player2_symbol

        # Check if the player has won
        if check_win(grid, player1_symbol):
            print(f"{player1} has won!")
            break
        elif check_win(grid, player2_symbol):
            print(f"{player2} has won!")
            break

        # Check if the game is a draw
        if is_draw(grid):
            print("It's a draw!")
            break

        # Switch players
        current_player = player2 if current_player == player1 else player1

def check_win(grid, symbol):
    # Check rows
    for row in grid:
        if all(cell == symbol for cell in row):
            return True

    # Check columns
    for column in range(3):
        if all(grid[row][column] == symbol for row in range(3)):
            return True

    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] == symbol:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == symbol:
        return True

    # No win yet
    return False

def is_draw(grid):
    # Check if there are any empty cells
    return all(all(cell != ' ' for cell in row) for row in grid)

# Play the game
jdv()
