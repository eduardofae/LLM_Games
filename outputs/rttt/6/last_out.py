def jdv():
    """
    Play a game of jdv.

    jdv is a two-player game played on a 3x3 grid. Players take turns placing their pieces in a free space on the grid. The first player to get three of their pieces in a row, column, or diagonal wins. If all the spaces on the grid are filled without either player getting three in a row, the game is a draw.

    Args:
        None

    Returns:
        None
    """

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
        try:
            row, column = map(int, input(f"{current_player}, enter your move (row, column): ").split())
        except ValueError:
            print("Invalid move. Enter again (row, column): ")
            continue

        # Check if the move is valid
        if not (0 <= row <= 2 and 0 <= column <= 2 and grid[row][column] == ' '):
            print("Invalid move. Enter again (row, column): ")
            continue

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
    """
    Check if the player with the given symbol has won.

    Args:
        grid (list): The game grid.
        symbol (str): The player's symbol.

    Returns:
        bool: True if the player has won, False otherwise.
    """

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
    """
    Check if the game is a draw.

    Args:
        grid (list): The game grid.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """

    # Check if there are any empty cells
    return all(all(cell != ' ' for cell in row) for row in grid)

# Play the game
if __name__ == "__main__":
    jdv()
