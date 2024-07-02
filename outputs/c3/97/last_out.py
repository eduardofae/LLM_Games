import numpy as np
import tkinter as tk

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
player1 = 1
player2 = 2

# Define the game over flag
game_over = False

# Define the winner flag
winner = 0

# Define the current player
current_player = player1

# Create the game window
window = tk.Tk()
window.title("Connect Four")

# Create the grid
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create the squares
squares = []
for i in range(10):
    for j in range(10):
        square = canvas.create_rectangle(i*40, j*40, (i+1)*40, (j+1)*40, fill="white")
        squares.append(square)

# Define the click event handler
def click(event):
    global current_player, game_over, winner

    # Get the column number
    column = event.x // 40

    # Check if the column is full
    if grid[9, column] != 0:
        print("Column is full. Please choose another column.")
        return

    # Find the lowest free space in the chosen column
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = current_player
            canvas.itemconfig(squares[i*10 + column], fill="red" if current_player == player1 else "blue")
            break

    # Check if the player has won
    if check_win(grid, current_player):
        winner = current_player
        game_over = True

    # Change the current player
    current_player = player1 if current_player == player2 else player2

# Bind the click event to the canvas
canvas.bind("<Button-1>", click)

# Start the game loop
while not game_over:
    window.update()

# Print the winner
if winner != 0:
    print("Player", winner, "wins!")


def check_win(grid, player):

    # Check for a horizontal win
    for i in range(10):
        if np.all(grid[i, :] == player):
            return True

    # Check for a vertical win
    for j in range(10):
        if np.all(grid[:, j] == player):
            return True

    # Check for a diagonal win
    for i in range(6):
        for j in range(6):
            if np.all(grid[i:i+3, j:j+3] == player):
                return True
            if np.all(grid[i:i+3, 9-j-2:9-j+1] == player):
                return True

    # No win found
    return False


# Run the main loop
window.mainloop()
