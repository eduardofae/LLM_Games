import tkinter as tk

# Initialize the game board
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Initialize the player's turn
turn = 'X'

# Initialize the number of wins and losses for each player
wins = {'X': 0, 'O': 0}
losses = {'X': 0, 'O': 0}

# Create a function to check if a player has won
def check_win(board, player):
    # Check for horizontal wins
    for row in board:
        if all(row[i] == player for i in range(3)):
            return True

    # Check for vertical wins
    for col in range(3):
        if all(board[i][col] == player for i in range(3)):
            return True

    # Check for diagonal wins
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # Otherwise, return False
    return False

# Create a function to print the game board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Create a function to get a valid move from the player
def get_move(board, player):
    while True:
        # Get the player's move
        move = input(f"{player}'s turn. Enter a row and column (e.g. 1 2): ")

        # Parse the player's move
        try:
            row, col = map(int, move.split())
        except ValueError:
            print("Invalid move. Please try again.")
            continue

        # Check if the move is valid
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != ' ':
            print("Invalid move. Please try again.")
            continue

        # Return the valid move
        return row - 1, col - 1

# Create a function to start a new game
def new_game():
    global board, turn

    # Reset the game board
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    # Reset the player's turn
    turn = 'X'

    # Print the game board
    print_board(board)

# Create a function to handle the game over
def game_over(winner):
    global wins, losses

    # Print the winning board
    print_board(board)

    # Print the winning player
    print(f"{winner} wins!")

    # Update the wins and losses for each player
    wins[winner] += 1
    losses[winner] += 1

    # Ask the players if they want to play again
    play_again = input("Do you want to play again? (y/n) ")

    # If the players want to play again, start a new game
    if play_again == 'y':
        new_game()

    # Otherwise, exit the game
    else:
        exit()

# Create the game window
window = tk.Tk()
window.title("Jdv")

# Create the game board
game_board = tk.Frame(window)
game_board.pack()

# Create the game board buttons
buttons = []
for row in range(3):
    for col in range(3):
        button = tk.Button(game_board, text=' ', width=4, height=2, command=lambda row=row, col=col: make_move(row, col))
        button.grid(row=row, column=col)
        buttons.append(button)

# Create the game status label
status_label = tk.Label(window, text=f"{turn}'s turn")
status_label.pack()

# Create the new game button
new_game_button = tk.Button(window, text="New Game", command=new_game)
new_game_button.pack()

# Create the wins and losses label
wins_losses_label = tk.Label(window, text=f"Wins: X - {wins['X']}, O - {wins['O']}\nLosses: X - {losses['X']}, O - {losses['O']}")
wins_losses_label.pack()

# Define the make_move function
def make_move(row, col):
    global board, turn

    # Place the player's piece on the board
    board[row][col] = turn

    # Update the game board buttons
    buttons[row * 3 + col]['text'] = turn

    # Check if a player has won
    if check_win(board, turn):
        game_over(turn)
        return

    # Check if the game is a draw
    if all(all(space != ' ' for space in row) for row in board):
        game_over("Draw")
        return

    # Switch to the other player's turn
    turn = 'X' if turn == 'O' else 'O'

    # Update the game status label
    status_label['text'] = f"{turn}'s turn"

    # Update the wins and losses label
    wins_losses_label['text'] = f"Wins: X - {wins['X']}, O - {wins['O']}\nLosses: X - {losses['X']}, O - {losses['O']}"

# Start the game
new_game()

# Run the game window
window.mainloop()
