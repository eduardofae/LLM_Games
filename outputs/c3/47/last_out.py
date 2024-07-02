import numpy as np

# Create a 10x10 board
board = np.zeros((10, 10))

# Define the player's turns
player1 = True
player2 = False

# Define the winning conditions
winning_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Define the AI levels
ai_levels = {'easy': 1, 'medium': 2, 'hard': 3}

# Get the AI level
ai_level = ai_levels[input("Choose an AI level (easy, medium, hard): ")]

# Game loop
while True:
    # Print the board
    print(board)

    # Get the player's move
    if player1:
        column = int(input("Player 1, choose a column (0-9): "))
    else:
        # Get the AI's move
        column = get_ai_move(board, ai_level)

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please choose a column between 0 and 9.")
        continue

    # Check if the column is full
    if board[9, column] != 0:
        print("Column is full. Please choose another column.")
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if board[i, column] == 0:
            board[i, column] = 1 if player1 else 2
            break

    # Check if the player has won
    for condition in winning_conditions:
        if board[condition[0], condition[1]] == board[condition[1], condition[2]] and board[condition[1], condition[2]] == board[condition[2], condition[0]] and board[condition[2], condition[0]] != 0:
            print("Player", ("1" if player1 else "2"), "wins!")
            break

    # Check if the game is a draw
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch the player's turns
    player1 = not player1
    player2 = not player2

# Function to get the AI's move
def get_ai_move(board, ai_level):
    # Create a list of all possible moves
    moves = []
    for i in range(10):
        if board[9, i] == 0:
            moves.append(i)

    # Evaluate each possible move using the alpha-beta pruning algorithm
    scores = []
    for move in moves:
        # Make the move
        board[9, move] = 2
        # Evaluate the move
        score = alpha_beta_pruning(board, ai_level, False, -np.inf, np.inf)
        # Undo the move
        board[9, move] = 0
        # Add the score to the list of scores
        scores.append(score)

    # Choose the move with the highest score
    best_move = moves[np.argmax(scores)]

    return best_move

# Function to evaluate a board using the alpha-beta pruning algorithm
def alpha_beta_pruning(board, depth, maximizing_player, alpha, beta):
    # Check if the game is over
    for condition in winning_conditions:
        if board[condition[0], condition[1]] == board[condition[1], condition[2]] and board[condition[1], condition[2]] == board[condition[2], condition[0]] and board[condition[2], condition[0]] != 0:
            return 1 if board[condition[2], condition[0]] == 2 else -1

    if np.all(board != 0):
        return 0

    # Get the list of all possible moves
    moves = []
    for i in range(10):
        if board[9, i] == 0:
            moves.append(i)

    # Evaluate each possible move
    if maximizing_player:
        for move in moves:
            # Make the move
            board[9, move] = 2
            # Evaluate the move
            score = alpha_beta_pruning(board, depth + 1, False, alpha, beta)
            # Undo the move
            board[9, move] = 0
            # Update alpha
            alpha = max(alpha, score)
            # Check if beta is less than alpha
            if beta <= alpha:
                break
        return alpha
    else:
        for move in moves:
            # Make the move
            board[9, move] = 1
            # Evaluate the move
            score = alpha_beta_pruning(board, depth + 1, True, alpha, beta)
            # Undo the move
            board[9, move] = 0
            # Update beta
            beta = min(beta, score)
            # Check if beta is less than alpha
            if beta <= alpha:
                break
        return beta
