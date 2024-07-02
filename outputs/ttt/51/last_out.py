import tkinter as tk

# Initialize the game board
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Initialize the players' turns and scores
player1_turn = True
player2_turn = False
player1_score = 0
player2_score = 0

# Initialize the Tkinter window
window = tk.Tk()
window.title("JDV")

# Create a canvas to draw the game board on
canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

# Create a function to draw the game board
def draw_board():
    for row in range(3):
        for column in range(3):
            if board[row][column] == 'X':
                canvas.create_line(column * 100, row * 100, column * 100 + 100, row * 100 + 100, width=5)
                canvas.create_line(column * 100 + 100, row * 100, column * 100, row * 100 + 100, width=5)
            elif board[row][column] == 'O':
                canvas.create_oval(column * 100 + 25, row * 100 + 25, column * 100 + 75, row * 100 + 75, width=5)

# Create a function to handle the player's move
def handle_click(event):
    global player1_turn, player2_turn

    # Get the row and column of the click
    row = event.y // 100
    column = event.x // 100

    # Check if the move is valid
    if board[row][column] != ' ':
        return

    # Place the player's piece on the board
    if player1_turn:
        board[row][column] = 'X'
    else:
        board[row][column] = 'O'

    # Check if the player has won
    if check_win(board, player1_turn):
        if player1_turn:
            print(f"{player1_name} wins!")
            player1_score += 1
        else:
            print(f"{player2_name} wins!")
            player2_score += 1
        reset_board()
        return

    # Check if there are no more free spaces
    if check_draw(board):
        print("Draw!")
        reset_board()
        return

    # Switch the player's turns
    player1_turn = not player1_turn
    player2_turn = not player2_turn

    # Redraw the game board
    draw_board()

# Create a function to reset the game board
def reset_board():
    global board, player1_turn, player2_turn

    # Reset the game board
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    # Reset the players' turns
    player1_turn = True
    player2_turn = False

    # Redraw the game board
    draw_board()

# Create a function to check if the player has won
def check_win(board, player_turn):
    symbol = 'X' if player_turn else 'O'

    # Check for horizontal wins
    for row in board:
        if all(x == symbol for x in row):
            return True

    # Check for vertical wins
    for column in range(3):
        if all(board[row][column] == symbol for row in range(3)):
            return True

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    # No win yet
    return False

# Create a function to check if there are no more free spaces
def check_draw(board):
    return all(x != ' ' for row in board for x in row)

# Bind the click event to the handle_click function
canvas.bind('<Button-1>', handle_click)

# Start the Tkinter event loop
window.mainloop()
