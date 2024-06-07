import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Define the players
players = ['X', 'O']

# Define the game status
game_status = 'ongoing'

# Define the game mode
game_mode = 'human vs. human'

# Define the board size
board_size = 3

# Start the game loop
while game_status == 'ongoing':
    
    # Get the current player
    current_player = players[0]

    # Get the player's move
    if game_mode == 'human vs. human':
        while True:
            try:
                row, col = map(int, input(f'{current_player}, enter your move (row, col): ').split())
                if row < 0 or row > board_size - 1 or col < 0 or col > board_size - 1:
                    print('Invalid move. Please enter coordinates within the bounds of the game board.')
                    continue
                if board[row, col] != 0:
                    print('Invalid move. Please try again.')
                    continue
                break
            except ValueError:
                print('Invalid input. Please enter two integers separated by a comma.')
    elif game_mode == 'human vs. computer':
        if current_player == 'X':
            # Get the player's move
            while True:
                try:
                    row, col = map(int, input(f'{current_player}, enter your move (row, col): ').split())
                    if row < 0 or row > board_size - 1 or col < 0 or col > board_size - 1:
                        print('Invalid move. Please enter coordinates within the bounds of the game board.')
                        continue
                    if board[row, col] != 0:
                        print('Invalid move. Please try again.')
                        continue
                    break
                except ValueError:
                    print('Invalid input. Please enter two integers separated by a comma.')
        elif current_player == 'O':
            # Computer's move
            row, col = get_computer_move(board)
    elif game_mode == 'computer vs. computer':
        row, col = get_computer_move(board)

    # Place the player's piece on the board
    board[row, col] = current_player

    # Check if the player has won
    if check_win(board, current_player):
        game_status = 'win'
        print(f'{current_player} wins!')
        break

    # Check if the game is a draw
    if np.all(board != 0):
        game_status = 'draw'
        print('The game is a draw.')
        break

    # Switch the current player
    players.reverse()

# Print the final game board
print(board)

# Check if there is a winner
def check_win(board, player):
    
    # Check the rows
    for row in range(board_size):
        if np.all(board[row, :] == player):
            return True

    # Check the columns
    for col in range(board_size):
        if np.all(board[:, col] == player):
            return True

    # Check the diagonals
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # No winner yet
    return False

# Get the computer's move
def get_computer_move(board):
    
    # Get all possible moves
    possible_moves = []
    for row in range(board_size):
        for col in range(board_size):
            if board[row, col] == 0:
                possible_moves.append((row, col))

    # Evaluate each possible move
    scores = []
    for move in possible_moves:
        row, col = move
        board[row, col] = 'O'  # Temporarily place the computer's piece on the board
        score = evaluate_board(board)
        board[row, col] = 0  # Remove the computer's piece from the board
        scores.append(score)

    # Choose the move with the highest score
    best_move = possible_moves[np.argmax(scores)]

    return best_move

# Evaluate the board
def evaluate_board(board):
    
    # Check if the computer has won
    if check_win(board, 'O'):
        return 10

    # Check if the human has won
    if check_win(board, 'X'):
        return -10

    # Check if the board is full
    if np.all(board != 0):
        return 0

    # Evaluate the board based on the number of pieces each player has
    score = 0
    for row in range(board_size):
        for col in range(board_size):
            if board[row, col] == 'O':
                score += 1
            elif board[row, col] == 'X':
                score -= 1

    return score

# Save the game
def save_game(board, game_status):
    with open('game.txt', 'w') as f:
        f.write(f'{board}\n')
        f.write(f'{game_status}\n')

# Load the game
def load_game():
    with open('game.txt', 'r') as f:
        board = np.loadtxt(f, dtype=int)
        game_status = f.readline().strip()
    return board, game_status
