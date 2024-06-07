import numpy as np
import tkinter as tk
from playsound import playsound

# Initialize the game board
board = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

# Set the current player
current_player = players[0]

# Create the GUI
root = tk.Tk()
root.title("Pong")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create the game board on the GUI
for i in range(10):
    for j in range(10):
        canvas.create_rectangle(i * 30, j * 30, (i + 1) * 30, (j + 1) * 30, fill="white")

# Create a function to place a piece on the board
def place_piece(event):
    global current_player

    # Get the column that was clicked
    column = int(event.x / 30)

    # Check if the move is valid
    if board[9, column] != 0:
        return

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i, column] == 0:
            board[i, column] = current_player
            canvas.create_oval(column * 30 + 5, i * 30 + 5, (column + 1) * 30 - 5, (i + 1) * 30 - 5, fill="black")
            break

    # Check if the player has won
    if check_win(board, current_player):
        print(f"Player {current_player} wins!")
        playsound("win.wav")
        return

    # Check if the game is a draw
    if np.all(board != 0):
        print("Draw!")
        playsound("draw.wav")
        return

    # Switch to the other player
    current_player = players[(players.index(current_player) + 1) % 2]

# Bind the click event to the place_piece function
canvas.bind("<Button-1>", place_piece)

# Create a function to check if a player has won
def check_win(board, player):

    # Check for a horizontal win
    for i in range(10):
        if np.all(board[i, :] == player):
            return True

    # Check for a vertical win
    for j in range(10):
        if np.all(board[:, j] == player):
            return True

    # Check for a diagonal win
    for i in range(10):
        for j in range(10):
            if board[i, j] == player and i + j < 10:
                if board[i + 1, j + 1] == player and board[i + 2, j + 2] == player:
                    return True
            if board[i, j] == player and i + j >= 10:
                if board[i - 1, j - 1] == player and board[i - 2, j - 2] == player:
                    return True

    # No win
    return False

# Create a function to reset the game
def reset_game():
    global board, current_player

    # Reset the game board
    board = np.zeros((10, 10), dtype=int)

    # Reset the current player
    current_player = players[0]

    # Clear the canvas
    canvas.delete("all")

    # Create the game board on the GUI
    for i in range(10):
        for j in range(10):
            canvas.create_rectangle(i * 30, j * 30, (i + 1) * 30, (j + 1) * 30, fill="white")

# Create a reset button
reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack()

# Create a settings button
settings_button = tk.Button(root, text="Settings", command=open_settings)
settings_button.pack()

# Create a settings window
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    # Create a label for the board size setting
    board_size_label = tk.Label(settings_window, text="Board size:")
    board_size_label.pack()

    # Create a dropdown menu for the board size setting
    board_size_options = ["10x10", "15x15", "20x20"]
    board_size_variable = tk.StringVar(settings_window)
    board_size_variable.set(board_size_options[0])
    board_size_dropdown = tk.OptionMenu(settings_window, board_size_variable, *board_size_options)
    board_size_dropdown.pack()

    # Create a label for the difficulty level setting
    difficulty_level_label = tk.Label(settings_window, text="Difficulty level:")
    difficulty_level_label.pack()

    # Create a dropdown menu for the difficulty level setting
    difficulty_level_options = ["Easy", "Medium", "Hard"]
    difficulty_level_variable = tk.StringVar(settings_window)
    difficulty_level_variable.set(difficulty_level_options[0])
    difficulty_level_dropdown = tk.OptionMenu(settings_window, difficulty_level_variable, *difficulty_level_options)
    difficulty_level_dropdown.pack()

    # Create a button to save the settings
    save_settings_button = tk.Button(settings_window, text="Save", command=save_settings)
    save_settings_button.pack()

# Create a function to save the settings
def save_settings():
    global board_size, difficulty_level

    # Get the selected board size
    board_size = board_size_variable.get()

    # Get the selected difficulty level
    difficulty_level = difficulty_level_variable.get()

    # Close the settings window
    settings_window.destroy()

# Start the GUI
root.mainloop()
