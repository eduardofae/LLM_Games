import numpy as np
import socket
import threading

# Create the game board
board = np.zeros((3, 3))

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Keep track of the current player
current_player = player1_symbol

# Keep track of the game status
game_status = 'ongoing'

# Create an AI opponent
ai = AI()

# Configure the difficulty level
difficulty_level = 'medium'

# Create a socket for online multiplayer
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen()

# Main game loop
while game_status == 'ongoing':

    # Print the game board
    print_board(board)

    # Get the player's move
    if current_player == player1_symbol:
        try:
            row, col = map(int, input(f"Player {current_player}, enter your move (row, col): ").split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by a comma.")
            continue
    else:
        # Get AI's move
        row, col = ai.get_move(board, difficulty_level)

    # Check if the move is valid
    if not (0 <= row < 3 and 0 <= col < 3):
        print("Invalid move. Please enter a valid row and column.")
        continue
    if board[row, col] != 0:
        print("Invalid move. Please choose an empty space.")
        continue

    # Place the player's piece on the board
    board[row, col] = current_player

    # Check if the player has won
    if check_win(board, current_player):
        game_status = 'over'
        print(f"Player {current_player} wins!")
        break

    # Check if the game is a draw
    if np.all(board != 0):
        game_status = 'draw'
        print("The game is a draw!")
        break

    # Switch the current player
    current_player = player2_symbol if current_player == player1_symbol else player1_symbol

# Print the final game board
print_board(board)

# Print the game status
print(game_status)


# Function to print the game board in a visually appealing format
def print_board(board):
    # Create a visual representation of the game board using ASCII art
    visual_board = [[' ' for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            if board[row, col] == player1_symbol:
                visual_board[row][col] = 'X'
            elif board[row, col] == player2_symbol:
                visual_board[row][col] = 'O'

    # Print the visual board
    for row in visual_board:
        print(' '.join(row))


# Function to check if the player has won the game
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
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # No win found
    return False


# AI class to generate moves
class AI:
    def __init__(self):
        self.symbol = player2_symbol

    def get_move(self, board, difficulty_level):
        # Get all possible moves
        possible_moves = []
        for row in range(3):
            for col in range(3):
                if board[row, col] == 0:
                    possible_moves.append((row, col))

        # Evaluate each move using a simple heuristic
        scores = [self.evaluate_move(board, move) for move in possible_moves]

        # Get the move with the highest score
        best_move = possible_moves[np.argmax(scores)]

        return best_move

    def evaluate_move(self, board, move):
        # Place the AI's piece on the board
        board[move[0], move[1]] = self.symbol

        # Check if the AI has won
        if check_win(board, self.symbol):
            return 100

        # Check if the opponent has won
        if check_win(board, player1_symbol):
            return -100

        # Evaluate the board using a simple heuristic
        score = 0
        # Check for rows with two AI pieces and one empty space
        for row in range(3):
            if np.all(board[row, :] == [self.symbol, self.symbol, 0]):
                score += 10
        # Check for columns with two AI pieces and one empty space
        for col in range(3):
            if np.all(board[:, col] == [self.symbol, self.symbol, 0]):
                score += 10
        # Check for diagonals with two AI pieces and one empty space
        if np.all(board.diagonal() == [self.symbol, self.symbol, 0]):
            score += 10
        if np.all(np.flip(board).diagonal() == [self.symbol, self.symbol, 0]):
            score += 10

        # Remove the AI's piece from the board
        board[move[0], move[1]] = 0

        return score
