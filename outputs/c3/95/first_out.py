import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the players
player1 = 1
player2 = 2

# Define the game status
game_status = "ongoing"

# Define the winning combinations
winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

# Get the player's move
def get_player_move(player):
    while True:
        try:
            column = int(input(f"Player {player}, choose a column (0-9): "))
            if column < 0 or column > 9:
                raise ValueError
            return column
        except ValueError:
            print("Invalid input. Please choose a column between 0 and 9.")

# Place the player's piece on the board
def place_piece(player, column):
    for i in range(9, -1, -1):
        if board[i][column] == 0:
            board[i][column] = player
            return

# Check if the game is over
def check_game_over():
    # Check if there are any winning combinations
    for combination in winning_combinations:
        if board[combination[0][0]][combination[0][1]] == board[combination[1][0]][combination[1][1]] == board[combination[2][0]][combination[2][1]] != 0:
            return True, board[combination[0][0]][combination[0][1]]

    # Check if there are any empty spaces
    for row in board:
        for cell in row:
            if cell == 0:
                return False, None

    # If there are no empty spaces, the game is a draw
    return True, 0

# Print the game board
def print_board():
    for row in board:
        print(" ".join([str(int(cell)) for cell in row]))

# Main game loop
while game_status == "ongoing":
    # Get the player 1's move
    column = get_player_move(player1)
    
    # Place the player 1's piece on the board
    place_piece(player1, column)
    
    # Print the game board
    print_board()

    # Check if the game is over
    game_status, winner = check_game_over()
    
    if game_status:
        if winner == 0:
            print("Draw!")
        else:
            print(f"Player {winner} wins!")
        break

    # Get the player 2's move
    column = get_player_move(player2)
    
    # Place the player 2's piece on the board
    place_piece(player2, column)
    
    # Print the game board
    print_board()
    
    # Check if the game is over
    game_status, winner = check_game_over()
    
    if game_status:
        if winner == 0:
            print("Draw!")
        else:
            print(f"Player {winner} wins!")
        break
