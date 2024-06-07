import numpy as np

def jdv():
    # Create a 3x3 grid
    grid = np.zeros((3, 3), dtype=int)

    # Define the players
    players = ['X', 'O']

    # Define the game loop
    while True:
        # Get the current player
        player = players[0]

        # Get the player's move
        row, col = map(int, input("Enter your move (row, col): ").split())

        # Check if the move is valid
        if grid[row, col] != 0:
            print("Invalid move")
            continue

        # Place the player's piece on the grid
        grid[row, col] = player

        # Check if the player has won
        if check_win(grid, player):
            print(f"{player} wins!")
            break

        # Check if the game is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch to the other player
        players = players[1:]

def check_win(grid, player):
    # Check if the player has won horizontally
    for i in range(3):
        if np.all(grid[i, :] == player):
            return True

    # Check if the player has won vertically
    for j in range(3):
        if np.all(grid[:, j] == player):
            return True

    # Check if the player has won diagonally
    if np.all(grid.diagonal() == player):
        return True
    if np.all(np.flip(grid).diagonal() == player):
        return True

    # Otherwise, the player has not won
    return False

if __name__ == "__main__":
    jdv()
