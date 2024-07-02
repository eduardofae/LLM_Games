import tkinter as tk
import numpy as np
from playsound import playsound

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
player1 = 1
player2 = 2

# Define the current player
current_player = player1

# Create the GUI
root = tk.Tk()
root.title("Pong")
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Draw the grid
for i in range(10):
    for j in range(10):
        canvas.create_rectangle(i*30, j*30, (i+1)*30, (j+1)*30, fill="white")

# Define the game loop
def game_loop():
    global current_player

    # Get the column where the current player wants to place their piece
    column = int(input("Player {}'s turn. Enter a column (0-9): ".format(current_player)))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please try again.")
        return

    # Check if the column is full
    if grid[9, column] != 0:
        print("Column {} is full. Please try again.".format(column))
        return

    # Place the current player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row, column] == 0:
            grid[row, column] = current_player
            break

    # Draw the current player's piece
    if current_player == player1:
        color = "red"
    else:
        color = "blue"
    canvas.create_oval(column*30, row*30, (column+1)*30, (row+1)*30, fill=color)

    # Play a sound effect
    if check_win(grid, current_player):
        playsound('win.wav')
    elif np.all(grid != 0):
        playsound('draw.wav')
    else:
        playsound('place.wav')

    # Check if the current player has won
    if check_win(grid, current_player):
        print("Player {} has won!".format(current_player))
        return

    # Check if the game is a draw
    if np.all(grid != 0):
        print("The game is a draw.")
        return

    # Switch the current player
    current_player = 3 - current_player

    # Call the game loop again
    root.after(100, game_loop)

# Define the function to check if a player has won
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
        if np.all(grid[i, i] == player):
            return True
        if np.all(grid[i, 9 - i] == player):
            return True

    # No wins found
    return False

# Start the game loop
game_loop()

# Start the GUI event loop
root.mainloop()
