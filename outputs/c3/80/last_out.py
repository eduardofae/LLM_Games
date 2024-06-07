import numpy as np
import pygame
import socketIO_client

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Create a list of players
players = ['X', 'O']

# Set the current player to 'X'
currentPlayer = 0

# Create a socketIO client
socketIO = socketIO_client.SocketIO('localhost', 3000)

# Game loop
while True:
    # Get the column where the player wants to place their piece
    while True:
        try:
            column = int(input("Player {} choose a column (0-9): ".format(currentPlayer + 1)))
            if column < 0 or column > 9:
                print("Invalid column number. Please choose a column between 0 and 9.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 9.")

    # Check if the column is full
    if grid[9, column] != 0:
        print("Column {} is full. Please choose another column.".format(column))
        continue

    # Place the player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row, column] == 0:
            grid[row, column] = currentPlayer + 1
            break

    # Check if the player has won
    if check_win(grid, currentPlayer + 1):
        print("Player {} wins!".format(currentPlayer + 1))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch to the other player
    currentPlayer = (currentPlayer + 1) % 2


# Function to check if a player has won
def check_win(grid, player):
    # Check for horizontal wins
    for row in range(10):
        if np.all(grid[row, :] == player):
            return True

    # Check for vertical wins
    for column in range(10):
        if np.all(grid[:, column] == player):
            return True

    # Check for diagonal wins
    for i in range(10):
        if np.all(np.diagonal(grid[i:, :i])[::-1] == player):
            return True
        if np.all(np.diagonal(grid[:i, i:]) == player):
            return True

    return False

# Function to print the game board
def print_board(grid):
    for row in grid:
        print(' '.join([str(x) for x in row]))

# Main game loop
if __name__ == "__main__":
    while True:
        print_board(grid)
        currentPlayer = (currentPlayer + 1) % 2
        column = int(input("Player {} choose a column (0-9): ".format(currentPlayer + 1)))
        grid[9 - column, column] = currentPlayer + 1
        if check_win(grid, currentPlayer + 1):
            print_board(grid)
            print("Player {} wins!".format(currentPlayer + 1))
            break
        if np.all(grid != 0):
            print_board(grid)
            print("Draw!")
            break
