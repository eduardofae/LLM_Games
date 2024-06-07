import numpy as np
import tkinter as tk

# Create the game board
board = np.zeros((10, 10), dtype=int)

# Define the players
player1 = 1
player2 = -1

# Define the current player
current_player = player1

# Create the Tkinter window
window = tk.Tk()
window.title("Connect Four")

# Create the menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create the game menu
game_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Game", menu=game_menu)
game_menu.add_command(label="New Game", command=lambda: reset_game())
game_menu.add_command(label="Quit", command=window.destroy)

# Create the options menu
options_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Change Board Size", command=lambda: change_board_size())

# Create the game board canvas
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create the game board squares
for i in range(10):
    for j in range(10):
        square = tk.Rectangle(canvas, i*40, j*40, (i+1)*40, (j+1)*40, fill="white")
        canvas.create_window(i*40+20, j*40+20, window=square)

# Define the click function
def click(event):
    global current_player

    # Get the column of the click
    column = event.x // 40

    # Place the player's piece on the board
    board[column, np.argmin(board[:, column])] = current_player

    # Check if the player has won
    if check_win():
        print("Player {} wins!".format(current_player))
        window.destroy()

    # Check if the game is a draw
    if np.all(board != 0):
        print("Draw!")
        window.destroy()

    # Switch to the other player
    current_player = -current_player

# Define the check win function
def check_win():
    # Check for horizontal wins
    for i in range(board.shape[0]):
        for j in range(board.shape[1]-3):
            if np.all(board[i, j:j+4] == current_player):
                return True

    # Check for vertical wins
    for i in range(board.shape[0]-3):
        for j in range(board.shape[1]):
            if np.all(board[i:i+4, j] == current_player):
                return True

    # Check for diagonal wins
    for i in range(board.shape[0]-3):
        for j in range(board.shape[1]-3):
            if np.all(board[i:i+4, j:j+4] == current_player):
                return True

    return False

# Bind the click event to the canvas
canvas.bind("<Button-1>", click)

# Define the reset game function
def reset_game():
    global board, current_player
    board = np.zeros((10, 10), dtype=int)
    current_player = player1
    canvas.delete("all")
    create_game_board_squares()

# Define the change board size function
def change_board_size():
    global board, canvas
    new_size = int(input("Enter the new board size: "))
    board = np.zeros((new_size, new_size), dtype=int)
    canvas.delete("all")
    create_game_board_squares()

# Create the game board squares
def create_game_board_squares():
    for i in range(board