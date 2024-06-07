import numpy as np

def jdv():
    # Create a 3x3 grid
    grid = np.zeros((3, 3), dtype=int)

    # Player 1 is 'X' and Player 2 is 'O'
    players = ['X', 'O']

    # Keep track of whose turn it is
    turn = 0

    # Main game loop
    while True:
        # Get the current player's move
        row, col = input(f"Player {players[turn]}, enter your move (row, col): ").split()

        # Check if the move is valid
        if not (0 <= row < 3 and 0 <= col < 3 and grid[int(row), int(col)] == 0):
            print("Invalid move. Try again.")
            continue

        # Place the player's piece on the grid
        grid[int(row), int(col)] = players[turn]

        # Check if the player has won
        if check_win(grid, players[turn]):
            print(f"Player {players[turn]} wins!")
            break

        # Check if there are no more free spaces
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch turns
        turn = (turn + 1) % 2

def check_win(grid, player):
    # Check for horizontal wins
    for row in range(3):
        if np.all(grid[row, :] == player):
            return True

    # Check for vertical wins
    for col in range(3):
        if np.all(grid[:, col] == player):
            return True

    # Check for diagonal wins
    if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
        return True

    # No win
    return False

if __name__ == "__main__":
    jdv()
