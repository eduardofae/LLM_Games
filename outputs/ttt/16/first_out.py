import numpy as np

def jdv():
    # Create a 3x3 grid
    grid = np.zeros((3, 3), dtype=int)

    # Get the player names
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")

    # Set the current player to player 1
    current_player = player1

    # Game loop
    while True:
        # Print the grid
        print(grid)

        # Get the player's move
        row, col = map(int, input("Enter your move (row, col): ").split())

        # Check if the move is valid
        if grid[row, col] != 0:
            print("Invalid move. Try again.")
            continue

        # Place the player's piece on the grid
        grid[row, col] = 1 if current_player == player1 else 2

        # Check if the player has won
        if check_win(grid, current_player):
            print(f"{current_player} wins!")
            break

        # Check if the game is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch the current player
        current_player = player2 if current_player == player1 else player1

def check_win(grid, player):
    """
    Checks if the given player has won the game.

    Args:
        grid: The game grid.
        player: The player to check.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win in each row
    for row in range(3):
        if np.all(grid[row, :] == player):
            return True

    # Check for a win in each column
    for col in range(3):
        if np.all(grid[:, col] == player):
            return True

    # Check for a win in each diagonal
    if np.all(grid.diagonal() == player) or np.all(np.flipud(grid).diagonal() == player):
        return True

    return False

if __name__ == "__main__":
    jdv()
