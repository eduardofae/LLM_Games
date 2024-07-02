import sys

# Create a 3x3 game board
game_board = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

# Get the names of the players
player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2 (or AI for AI opponent): ")

# Set the current player to player 1
current_player = player1

# Main game loop
while True:
    # Display the game board
    print("Current game board:")
    for row in game_board:
        print(" ".join(row))

    # Get the player's move
    if current_player == "AI":
        # Randomly select a valid move for the AI opponent
        while True:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if game_board[row][column] == ' ':
                break
    else:
        try:
            move = input(f"{current_player}'s turn (row, column): ")
            row, column = map(int, move.split(","))
        except ValueError:
            print("Invalid move. Please try again.")
            continue

    # Check if the move is valid
    if not (0 <= row < 3 and 0 <= column < 3) or game_board[row][column] != ' ':
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the game board
    game_board[row][column] = current_player

    # Check if the player has won
    if check_win(game_board, current_player):
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw
    if all(all(cell != ' ' for cell in row) for row in game_board):
        print("Draw!")
        break

    # Switch to the other player
    current_player = player2 if current_player == player1 else player1

# Check if the player has won
def check_win(game_board, player):
    # Check for horizontal wins
    for row in game_board:
        if all(cell == player for cell in row):
            return True

    # Check for vertical wins
    for i in range(3):
        if all(game_board[j][i] == player for j in range(3)):
            return True

    # Check for diagonal wins
    if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
        return True
    if game_board[0][2] == player and game_board[1][1] == player and game_board[2][0] == player:
        return True

    # No win yet
    return False
