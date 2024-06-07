# Initialize the game board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Define the players
players = ["X", "O"]

# Define the current player
current_player = 0

# Game loop
while True:
    # Get the player's move
    row = int(input("Enter the row: "))
    column = int(input("Enter the column: "))

    # Check if the move is valid
    if board[row][column] != " ":
        print("That space is already taken.")
        continue

    # Place the player's piece on the board
    board[row][column] = players[current_player]

    # Check if the player has won
    if check_win(board, players[current_player]):
        print(f"{players[current_player]} wins!")
        break

    # Check if the game is a draw
    if check_draw(board):
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Define the function to check if the player has won
def check_win(board, player):
    # Check the rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # Check the columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == player:
            return True

    # Check the diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Define the function to check if the game is a draw
def check_draw(board):
    # Check if there are any empty spaces on the board
    for row in board:
        for space in row:
            if space == " ":
                return False

    return True
