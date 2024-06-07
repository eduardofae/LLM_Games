import numpy as np

# Create the game board
def create_board():
    return np.zeros((10, 10))

# Get the player's move
def get_player_move(board):
    while True:
        try:
            row, col = map(int, input('Enter your move (row, col): ').split())
            if row < 0 or row >= 10 or col < 0 or col >= 10 or board[row, col] != 0:
                print('Invalid move. Try again.')
                continue
            return row, col
        except ValueError:
            print('Invalid input. Please enter two integers.')

# Place the player's piece on the board
def place_piece(board, player, row, col):
    board[row, col] = player

# Check if a player has won
def check_win(board, player):
    # Check for a horizontal win
    for row in range(10):
        if np.all(board[row, :] == player):
            return True

    # Check for a vertical win
    for col in range(10):
        if np.all(board[:, col] == player):
            return True

    # Check for a diagonal win
    for i in range(10):
        if np.all(board[i, i] == player) or np.all(board[i, 9 - i] == player):
            return True

    # No win yet
    return False

# Main game loop
def main():
    # Create the game board
    board = create_board()

    # Create a list of players
    players = ['Player 1', 'Player 2']

    # Keep track of the current player
    currentPlayer = 0

    # Keep track of the winner
    winner = None

    # Main game loop
    while winner is None:
        # Get the current player's move
        row, col = get_player_move(board)

        # Place the player's piece on the board
        place_piece(board, currentPlayer + 1, row, col)

        # Check if the player has won
        if check_win(board, currentPlayer + 1):
            winner = players[currentPlayer]
            break

        # Switch to the other player
        currentPlayer = (currentPlayer + 1) % 2

    # Print the winner
    if winner is not None:
        print('{} wins!'.format(winner))
    else:
        print('Draw!')

# Run the main game loop
if __name__ == '__main__':
    main()
