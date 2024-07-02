import numpy as np

def jdv():
    # Create a 3x3 grid
    grid = np.zeros((3,3))

    # Set the player's turns
    player1 = 1
    player2 = -1

    # Set the game over flag to False
    game_over = False

    # Main game loop
    while not game_over:
        # Get the player's move
        move = input("Player {}'s turn. Enter a row and column (e.g. 1,2): ".format(player1 if player1 == 1 else player2))
        row, col = map(int, move.split(","))

        # Check if the move is valid
        if grid[row, col] != 0:
            print("Invalid move. Try again.")
            continue

        # Place the player's piece on the grid
        grid[row, col] = player1 if player1 == 1 else player2

        # Check if the player has won
        if check_win(grid, player1 if player1 == 1 else player2):
            game_over = True
            print("Player {} wins!".format(player1 if player1 == 1 else player2))
            break

        # Check if the game is a draw
        if np.all(grid != 0):
            game_over = True
            print("Draw!")
            break

        # Switch the player's turns
        player1, player2 = player2, player1

def check_win(grid, player):
    # Check if there are three adjacent pieces in a row
    for i in range(3):
        if np.all(grid[i, :] == player):
            return True

    # Check if there are three adjacent pieces in a column
    for j in range(3):
        if np.all(grid[:, j] == player):
            return True

    # Check if there are three adjacent pieces in a diagonal
    if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
        return True

    # Otherwise, return False
    return False

if __name__ == "__main__":
    jdv()
