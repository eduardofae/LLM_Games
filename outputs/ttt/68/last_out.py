import numpy as np

def jdv():
    # Create the game board
    board = np.zeros((3, 3))

    # Define the players
    players = [1, 2]
    player_names = ["Player 1", "Player 2"]

    # Create the AI opponent
    ai_player = AIPlayer()

    # Start the game
    while True:
        # Get the current player
        player = players[0]
        player_name = player_names[0]

        # Display the game board
        print_board(board)

        # Get the player's move
        if player == 1:
            move = input(f"{player_name}, enter your move (row, column): ")
        else:
            move = ai_player.get_move(board)

        # Check if the move is valid
        if not is_valid_move(move, board):
            print("Invalid move. Please try again.")
            continue

        # Convert the move to row and column indices
        row, col = map(int, move.split(","))

        # Place the player's piece on the board
        board[row, col] = player

        # Check if the player has won
        if check_win(board, player):
            print(f"{player_name} wins!")
            break

        # Check if the game is a draw
        if np.all(board != 0):
            print("It's a draw!")
            break

        # Switch to the other player
        players = [players[1], players[0]]
        player_names = [player_names[1], player_names[0]]

def print_board(board):
    for row in board:
        print("|".join([str(int(x)) for x in row]))

def is_valid_move(move, board):
    # Check if the move is in the correct format
    if not move or len(move.split(",")) != 2:
        return False

    # Convert the move to row and column indices
    row, col = map(int, move.split(","))

    # Check if the row and column are within bounds
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False

    # Check if the space is empty
    if board[row, col] != 0:
        return False

    # The move is valid
    return True

def check_win(board, player):
    # Check for a win in each row
    for row in range(3):
        if np.all(board[row, :] == player):
            return True

    # Check for a win in each column
    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    # Check for a win in each diagonal
    if np.all(np.diag(board) == player):
        return True
    if np.all(np.diag(np.flip(board)) == player):
        return True

    # No win yet
    return False

class AIPlayer:
    def __init__(self):
        pass

    def get_move(self, board):
        # Implement the AI algorithm to determine the best move
        # For simplicity, we randomly choose an empty space
        while True:
            row = np.random.randint(3)
            col = np.random.randint(3)
            if board[row, col] == 0:
                return f"{row},{col}"

if __name__ == "__main__":
    while True:
        jdv()
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
