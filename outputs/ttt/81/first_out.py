import numpy as np

def jdv():
    # Create a 3x3 grid
    grid = np.zeros((3, 3))

    # Define the players
    players = ["X", "O"]

    # Set the current player
    current_player = 0

    # Game loop
    while True:
        # Get the current player's move
        move = input("Player {}'s turn: ".format(players[current_player]))

        # Check if the move is valid
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid move. Please enter a number between 1 and 9.")
            continue

        # Convert the move to a grid index
        row = (int(move) - 1) // 3
        col = (int(move) - 1) % 3

        # Check if the space is free
        if grid[row, col] != 0:
            print("That space is already taken. Please choose another space.")
            continue

        # Place the player's piece in the grid
        grid[row, col] = players[current_player]

        # Check if the player has won
        if check_win(grid, players[current_player]):
            print("Player {} wins!".format(players[current_player]))
            break

        # Check if there are no more free spaces
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch to the other player
        current_player = (current_player + 1) % 2

def check_win(grid, player):
    # Check the rows
    for row in grid:
        if np.all(row == player):
            return True

    # Check the columns
    for col in grid.T:
        if np.all(col == player):
            return True

    # Check the diagonals
    if np.all(grid.diagonal() == player):
        return True

    if np.all(np.flip(grid).diagonal() == player):
        return True

    # No win
    return False

if __name__ == "__main__":
    jdv()
