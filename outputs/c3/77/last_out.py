import numpy as np

# Create a 10x10 grid
game_board = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

def main():
    # Game loop
    while True:
        # Get the current player
        player = players[0]

        # Get the player's input
        while True:
            try:
                column = int(input(f"Player {player}, choose a column (1-10): ")) - 1
                if column < 0 or column > 9:
                    print("Invalid column")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")

        # Check if the column is full
        if game_board[0, column] != 0:
            print("Column is full")
            continue

        # Place the player's piece in the lowest free space of the column
        for i in range(9, -1, -1):
            if game_board[i, column] == 0:
                game_board[i, column] = player
                break

        # Check if the player has won
        if check_win(game_board, player):
            print(f"Player {player} wins!")
            break

        # Check if the game is a draw
        if np.all(game_board != 0):
            print("Draw!")
            break

        # Switch players
        players.reverse()

# Function to check if a player has won
def check_win(board, player):
    # Check for horizontal wins
    for i in range(10):
        if np.all(board[i, :] == player):
            return True

    # Check for vertical wins
    for j in range(10):
        if np.all(board[:, j] == player):
            return True

    # Check for diagonal wins
    # Check for a diagonal win in the northeast direction
    for i in range(7):
        for j in range(7):
            if board[i, j] == player and board[i+1, j+1] == player and board[i+2, j+2] == player:
                return True

    # Check for a diagonal win in the northwest direction
    for i in range(7):
        for j in range(2, 10):
            if board[i, j] == player and board[i+1, j-1] == player and board[i+2, j-2] == player:
                return True

    # Check for a diagonal win in the southeast direction
    for i in range(2, 10):
        for j in range(7):
            if board[i, j] == player and board[i-1, j+1] == player and board[i-2, j+2] == player:
                return True

    # Check for a diagonal win in the southwest direction
    for i in range(2, 10):
        for j in range(2, 10):
            if board[i, j] == player and board[i-1, j-1] == player and board[i-2, j-2] == player:
                return True

    # No win found
    return False

if __name__ == "__main__":
    main()
