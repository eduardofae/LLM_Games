import numpy as np

def create_grid():
    """ Creates a 3x3 grid filled with zeros. """
    grid = np.zeros((3, 3))
    return grid

def print_grid(grid):
    """ Print the grid to the console. """
    for row in grid:
        print(' '.join([str(int(cell)) for cell in row]))

def check_winner(grid):
    """ Checks if there is a winner in the grid. """
    # Check rows
    for row in grid:
        if np.all(row == row[0]) and row[0] != 0:
            return row[0]

    # Check columns
    for col in grid.T:
        if np.all(col == col[0]) and col[0] != 0:
            return col[0]

    # Check diagonals
    if np.all(grid.diagonal() == grid.diagonal()[0]) and grid.diagonal()[0] != 0:
        return grid.diagonal()[0]
    if np.all(np.flip(grid).diagonal() == np.flip(grid).diagonal()[0]) and np.flip(grid).diagonal()[0] != 0:
        return np.flip(grid).diagonal()[0]

    # No winner yet
    return None

def check_draw(grid):
    """ Checks if the game is a draw. """
    return np.all(grid != 0)

def play_jdv():
    """ Main game loop. """
    grid = create_grid()
    players = ['X', 'O']
    current_player = 0

    while True:
        print_grid(grid)

        # Get player's move
        while True:
            row = int(input(f"Player {players[current_player]}, enter the row (0-2): "))
            col = int(input(f"Player {players[current_player]}, enter the column (0-2): "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid move. Please enter a valid row and column.")
            elif grid[row, col] != 0:
                print("That space is already taken. Please enter a valid space.")
            else:
                break

        # Place player's piece in the grid
        grid[row, col] = players[current_player]

        # Check for winner or draw
        winner = check_winner(grid)
        if winner:
            print_grid(grid)
            print(f"Player {winner} wins!")
            break
        elif check_draw(grid):
            print_grid(grid)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_jdv()
