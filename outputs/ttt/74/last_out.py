import numpy as np

# Create a 3x3 game board
board = np.zeros((3, 3))

# Define the players
player_x = 'X'
player_o = 'O'

# Define the current player
current_player = player_x

# Define the winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]

# Define a function to print the game board
def print_board():
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == 0:
                print(" ", end="|")
            elif cell == player_x:
                print("X", end="|")
            elif cell == player_o:
                print("O", end="|")
        print()
    print("-------------")


# Define a function to check if a player has won
def check_win(player):
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False


# Define a function to place a piece on the board
def place_piece(player, move):
    if move < 1 or move > 9 or board[move-1] != 0:
        return False
    board[move-1] = player
    return True


# Main game loop
while True:
    try:
        # Print the game board
        print_board()

        # Get the player's move
        move = int(input(f"{current_player}'s turn (1-9): "))

        # Place the piece on the board
        if not place_piece(current_player, move):
            print("Invalid move. Try again.")
            continue

        # Check if the player has won
        if check_win(current_player):
            print(f"{current_player} wins!")
            break

        # Check if there are no more free spaces
        if np.all(board != 0):
            print("Draw!")
            break

        # Switch the current player
        current_player = player_o if current_player == player_x else player_x

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
