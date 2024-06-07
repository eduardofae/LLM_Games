import turtle

def jdv():
    # Create a 3x3 grid
    game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    # Get the names of the two players
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    # Determine who goes first
    turn = 1

    # Create a turtle object to draw the game board
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    for i in range(4):
        t.forward(200)
        t.left(90)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    for i in range(4):
        t.forward(200)
        t.left(90)

    # Game loop
    while True:
        # Print the game board
        print("Current game board:")
        for row in game_board:
            print(" ".join(row))

        # Get the player's move
        if turn == 1:
            try:
                row = int(input(f"{player1}, enter the row (1-3): "))
                col = int(input(f"{player1}, enter the column (1-3): "))
            except ValueError:
                print("Invalid input. Please enter a valid row and column number.")
                continue
        else:
            try:
                row = int(input(f"{player2}, enter the row (1-3): "))
                col = int(input(f"{player2}, enter the column (1-3): "))
            except ValueError:
                print("Invalid input. Please enter a valid row and column number.")
                continue

        # Check if the move is valid
        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Invalid move. Please enter a valid row and column number.")
            continue
        if game_board[row - 1][col - 1] != ' ':
            print("Invalid move. That space is already occupied.")
            continue

        # Place the player's piece in the game board
        if turn == 1:
            game_board[row - 1][col - 1] = 'X'
            t.penup()
            t.goto(-100 + (col - 1) * 66.66, 100 - (row - 1) * 66.66)
            t.pendown()
            t.write("X", font=("Arial", 60, "bold"))
        else:
            game_board[row - 1][col - 1] = 'O'
            t.penup()
            t.goto(-100 + (col - 1) * 66.66, 100 - (row - 1) * 66.66)
            t.pendown()
            t.write("O", font=("Arial", 60, "bold"))

        # Check if the player has won
        if check_win(game_board):
            if turn == 1:
                print(f"{player2} wins!")
            else:
                print(f"{player1} wins!")
            break

        # Check if the game is a draw
        if check_draw(game_board):
            print("Draw!")
            break

        # Switch turns
        turn *= -1

def check_win(game_board):
    # Check for a win in the rows
    for row in game_board:
        if row[0] != ' ' and row[0] == row[1] and row[1] == row[2]:
            return True

    # Check for a win in the columns
    for col in range(3):
        if game_board[0][col] != ' ' and game_board[0][col] == game_board[1][col] and game_board[1][col] == game_board[2][col]:
            return True

    # Check for a win in the diagonals
    if game_board[0][0] != ' ' and game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2]:
        return True
    if game_board[0][2] != ' ' and game_board[0][2] == game_board[1][1] and game_board[1][1] == game_board[2][0]:
        return True

    # No win yet
    return False

def check_draw(game_board):
    # Check if there are any empty spaces left
    for row in game_board:
        for space in row:
            if space == ' ':
                return False

    # No empty spaces left, so it's a draw
    return True

if __name__ == "__main__":
    jdv()
