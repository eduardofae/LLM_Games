
# Import the necessary libraries
import tkinter as tk
from tkinter import messagebox

# Create a 10x10 grid
grid = [[' ' for _ in range(10)] for _ in range(10)]

# Define the players
player1 = 'X'
player2 = 'O'

# Define the current player
current_player = player1

# Create the graphical user interface
root = tk.Tk()
root.title("Tic-Tac-Toe")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create the grid lines
for i in range(10):
    canvas.create_line(i*30, 0, i*30, 300)
    canvas.create_line(0, i*30, 300, i*30)

# Create the click handlers
def click(event):
    global current_player

    # Get the column where the player clicked
    column = event.x // 30

    # Check if the column is full
    if grid[0][column] != ' ':
        return

    # Place the player's piece in the lowest free space of the column
    for i in range(9, -1, -1):
        if grid[i][column] == ' ':
            grid[i][column] = current_player
            break

    # Check if the player has won
    if has_won(grid, current_player):
        messagebox.showinfo("Tic-Tac-Toe", f"{current_player} wins!")
        return

    # Check if the game is a draw
    if is_draw(grid):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        return

    # Switch the current player
    current_player = player1 if current_player == player2 else player2

# Bind the click handler to the canvas
canvas.bind("<Button-1>", click)

# Create the reset button
reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack()

# Create the score label
score_label = tk.Label(root, text="Score")
score_label.pack()

# Start the game loop
root.mainloop()


# Function to reset the game
def reset_game():
    global grid, current_player

    # Reset the grid
    grid = [[' ' for _ in range(10)] for _ in range(10)]

    # Reset the current player
    current_player = player1


# Function to check if a player has won
def has_won(grid, player):
    # Check for horizontal wins
    for row in grid:
        if row.count(player) == 3:
            return True

    # Check for vertical wins
    for column in range(10):
        column_values = [row[column] for row in grid]
        if column_values.count(player) == 3:
            return True

    # Check for diagonal wins
    for i in range(7):
        # Check for diagonal wins from top left to bottom right
        diagonal_values = [grid[i+j][j] for j in range(10-i)]
        if diagonal_values.count(player) == 3:
            return True

        # Check for diagonal wins from bottom left to top right
        diagonal_values = [grid[i+j][9-j] for j in range(10-i)]
        if diagonal_values.count(player) == 3:
            return True

    return False


# Function to check if the game is a draw
def is_draw(grid):
    for row in grid:
        for cell in row:
            if cell == ' ':
                return False

    return True
