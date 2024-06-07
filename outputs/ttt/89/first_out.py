# Create the game board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Define the players
players = ['X', 'O']

# Get the player's names
player1_name = input("Player 1 name: ")
player2_name = input("Player 2 name: ")

# Set the current player to player 1
current_player = 0

# Game loop
while True:
    # Get the current player's move
    row = int(input("Enter the row (1-3): ")) - 1
    column = int(input("Enter the column (1-3): ")) - 1

    # Check if the move is valid
    if board[row][column] == ' ':
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
    else:
        print("Invalid move. Please try again.")

# Print the final game board
for row in board:
    print(' '.join(row))


# Function to check if a player has won
def check_win(board, player):
    # Check the rows
    for row in board:
        if all(x == player for x in row):
            return True

    # Check the columns
    for column in range(3):
        if all(board[row][column] == player for row in range(3)):
            return True

    # Check the diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # No win yet
    return False


# Function to check if the game is a draw
def check_draw(board):
    # Check if there are any empty spaces
    for row in board:
        for column in row:
            if column == ' ':
                return False

    # No empty spaces, so the game is a draw
    return True
