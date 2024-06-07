import numpy as np

def print_board(board):
    for i in range(3):
        print(' '.join(board[i]))

def check_win(board):
    # Check rows
    for i in range(3):
        if np.all(board[i] == board[i][0]) and board[i][0] != '-':
            return board[i][0]

    # Check columns
    for j in range(3):
        if np.all(board[:, j] == board[0, j]) and board[0, j] != '-':
            return board[0, j]

    # Check diagonals
    if np.all(np.diag(board) == np.diag(board)[0]) and np.diag(board)[0] != '-':
        return np.diag(board)[0]

    if np.all(np.diag(np.flip(board)) == np.diag(np.flip(board))[0]) and np.diag(np.flip(board))[0] != '-':
        return np.diag(np.flip(board))[0]

    return '-'

def get_computer_move(board, player, alpha, beta, difficulty):
    # Get all possible moves
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i, j] == '-':
                possible_moves.append((i, j))

    # Evaluate each possible move using the minimax algorithm with alpha-beta pruning
    best_move = None
    best_score = -np.inf
    for move in possible_moves:
        board[move[0], move[1]] = player
        if difficulty == 'easy':
            score = minimax(board, -1, 'X' if player == 'O' else 'O', alpha, beta, True)
        else:
            score = minimax(board, -1, 'X' if player == 'O' else 'O', alpha, beta)
        board[move[0], move[1]] = '-'
        if score > best_score:
            best_move = move
            best_score = score
        alpha = max(alpha, score)
        if alpha >= beta:
            break

    return best_move

def minimax(board, depth, player, alpha, beta, is_easy_mode=False):
    # Check if the game is over
    winner = check_win(board)
    if winner != '-':
        if winner == 'X':
            return 1
        elif winner == 'O':
            return -1
        else:
            return 0

    # Get all possible moves for the current player
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i, j] == '-':
                possible_moves.append((i, j))

    # Evaluate each possible move
    scores = []
    for move in possible_moves:
        board[move[0], move[1]] = player
        if is_easy_mode:
            score = -minimax(board, depth + 1, 'X' if player == 'O' else 'O', alpha, beta)
        else:
            score = minimax(board, depth + 1, 'X' if player == 'O' else 'O', alpha, beta)
        board[move[0], move[1]] = '-'
        scores.append(score)

    # Choose the move with the highest score if it's the computer's turn, or the lowest score if it's the human player's turn
    if depth % 2 == 0:
        best_score = max(scores)
        alpha = max(alpha, best_score)
    else:
        best_score = min(scores)
        beta = min(beta, best_score)

    return best_score

def jdv():
    board = np.array([['-', '-', '-'],
                     ['-', '-', '-'],
                     ['-', '-', '-']])
    player = 'X'
    computer_player = 'O'

    # Get difficulty level from user
    difficulty = input("Choose difficulty level (easy/hard): ")

    while True:
        print_board(board)
        print(f"Player {player}'s turn")

        if player == 'X':
            # Get user input
            try:
                row, col = map(int, input("Enter row and column: ").split())
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
                continue

            if row not in range(3) or col not in range(3):
                print("Invalid row or column. Please enter values between 0 and 2.")
                continue

            if board[row, col] != '-':
                print("Invalid move. Please choose an empty space.")
                continue

            board[row, col] = player
        else:
            # Get computer move
            row, col = get_computer_move(board, computer_player, -np.inf, np.inf, difficulty)
            board[row, col] = player

        if check_win(board) != '-':
            print_board(board)
            print(f"Player {player} wins!")
            break

        player = computer_player if player == 'X' else 'X'

    if check_win(board) == '-':
        print("Draw!")

if __name__ == "__main__":
    jdv()
