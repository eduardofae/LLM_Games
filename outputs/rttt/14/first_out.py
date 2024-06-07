def jdv():
    # Initialize the game board
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    # Get the player names
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    # Set the current player to player 1
    current_player = player1

    # Keep track of the number of moves
    moves = 0

    # Main game loop
    while True:
        # Get the player's move
        print(f"{current_player}'s turn:")
        row = int(input("Enter the row (1-3): ")) - 1
        col = int(input("Enter the column (1-3): ")) - 1

        # Check if the move is valid
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue

        # Place the player's piece on the board
        board[row][col] = 'X' if current_player == player1 else 'O'

        # Display the game board
        print("Game board:")
        for row in board:
            for cell in row:
                print(cell, end=' ')
            print()

        # Check if the player has won
        if check_win(board):
            print(f"{current_player} wins!")
            break

        # Check if there are no more moves left
        if moves >= 9:
            print("Draw!")
            break

        # Switch the current player
        current_player = player2 if current_player == player1 else player1

        # Increment the number of moves
        moves += 1


# Check if the board has a winning line
def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    # No winning line found
    return False


# Play the game
if __name__ == "__main__":
    jdv()
