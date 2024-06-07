# Game board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Players' symbols
players = ['X', 'O']

# Current player
player = 0

# Game loop
while True:
    # Get player's move
    print(f"Player {players[player]}'s turn.")
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1

    # Check if move is valid
    if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
        print("Invalid move. Try again.")
        continue

    # Place player's symbol on the board
    board[row][col] = players[player]

    # Check if there is a winner
    winner = check_winner(board)
    if winner != ' ':
        print(f"Player {winner} wins!")
        break

    # Check if there is a draw
    if board_full(board):
        print("Draw!")
        break

    # Switch to the other player
    player = (player + 1) % 2

# End of game
print("Thanks for playing!")

# Function to check if there is a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # No winner yet
    return ' '

# Function to check if the board is full
def board_full(board):
    for row in board:
        for col in row:
            if col == ' ':
                return False

    return True
