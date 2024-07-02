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
        while True:
            try:
                row = int(input("Enter the row (1-3): ")) - 1
                col = int(input("Enter the column (1-3): ")) - 1
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")

        # Place the player's piece on the board
        board[row][col] = 'X' if current_player == player1 else 'O'

        # Display the game board
        print("Game board:")
        print(board)

        # Check if the player has won
        if check_win(board):
            print(f"{current_player} wins!")
            print(f"Winning line: {get_winning_line(board)}")
            break

        # Check if there are no more moves left
        if is_draw(board):
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


# Check if the board is a draw
def is_draw(board):
    # Check if there are any empty spaces left
    for row in board:
        for cell in row:
            if cell == ' ':
                return False

    # No empty spaces left, so it's a draw
    return True


# Get the winning line
def get_winning_line(board):
    # Check rows
    for i, row in enumerate(board):
        if row[0] == row[1] == row[2] != ' ':
            return f"Row {i + 1}"

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return f"Column {i + 1}"

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return "Diagonal from top left to bottom right"
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return "Diagonal from top right to bottom left"

    # No winning line found
    return None


# Play the game
if __name__ == "__main__":
    jdv()
