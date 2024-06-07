import numpy as np

# Create a 3x3 grid to represent the game board
grid = np.zeros((3, 3), dtype=int)

# Define the players' symbols
player1_symbol = "X"
player2_symbol = "O"

# Initialize the current player to player 1
current_player = player1_symbol

# Create a function to check if a player has won
def check_win(grid, player_symbol):
    # Check if the player has won horizontally
    for row in range(3):
        if all(grid[row] == player_symbol):
            return True

    # Check if the player has won vertically
    for col in range(3):
        if all(grid[:, col] == player_symbol):
            return True

    # Check if the player has won diagonally
    if all(grid.diagonal() == player_symbol) or all(np.flip(grid).diagonal() == player_symbol):
        return True

    return False

# Create a function to get the next move from a player
def get_move(player_symbol):
    while True:
        try:
            # Get the player's move
            move = input(f"Player {player_symbol}, enter your move (row, column): ")
            row, col = map(int, move.split(","))

            # Check if the move is valid
            if row < 0 or row > 2 or col < 0 or col > 2 or grid[row, col] != 0 or player_symbol != current_player:
                print("Invalid move. Please try again.")
                continue

            # Return the player's move
            return row, col
        except ValueError:
            print("Invalid move. Please try again.")

# Create a function to switch to the other player
def switch_player():
    global current_player
    current_player = player2_symbol if current_player == player1_symbol else player1_symbol

# Create a function to display the game board
def display_board():
    for row in grid:
        for cell in row:
            if cell == 0:
                print(" ", end=" ")
            elif cell == 1:
                print("X", end=" ")
            elif cell == 2:
                print("O", end=" ")
        print()

# Play the game
while True:
    # Display the game board
    display_board()

    # Get the next move from the current player
    row, col = get_move(current_player)

    # Place the player's piece on the grid
    grid[row, col] = 1 if current_player == player1_symbol else 2

    # Check if the player has won
    if check_win(grid, 1 if current_player == player1_symbol else 2):
        print(f"Player {current_player} has won!")
        break

    # Check if the game is a draw
    if all(grid != 0):
        print("The game is a draw.")
        break

    # Switch to the other player
    switch_player()
