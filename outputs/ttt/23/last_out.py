import numpy as np

def jdv():
    # Get the size of the grid from the user
    while True:
        try:
            size = int(input("Enter the size of the grid (e.g. 3 for a 3x3 grid): "))
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            continue

        if size < 3:
            print("The grid must be at least 3x3.")
            continue

        break

    # Create the grid
    grid = np.zeros((size, size))

    # Set the player's turns
    player1 = 1
    player2 = -1

    # Set the game over flag to False
    game_over = False

    # Set the number of wins and losses for each player to 0
    player1_wins = 0
    player2_wins = 0

    # Get the difficulty of the AI opponent
    while True:
        try:
            difficulty = int(input("Enter the difficulty of the AI opponent (1 for easy, 2 for hard): "))
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
            continue

        if difficulty not in [1, 2]:
            print("Invalid difficulty. Please enter 1 or 2.")
            continue

        break

    # Main game loop
    while not game_over:
        # Get the player's move
        if player1 == 1:
            while True:
                move = input("Player {}'s turn. Enter a row and column (e.g. 1,2): ".format(player1 if player1 == 1 else player2))
                try:
                    row, col = map(int, move.split(","))
                except ValueError:
                    print("Invalid input. Please enter two numbers separated by a comma.")
                    continue

                if row < 0 or row > size - 1 or col < 0 or col > size - 1:
                    print("Invalid move. Please enter a row and column between 0 and {}.".format(size - 1))
                    continue

                if grid[row, col] != 0:
                    print("Invalid move. Please enter an empty space.")
                    continue

                break
        else:
            # Get the AI opponent's move
            row, col = get_ai_move(grid, player1, difficulty)

        # Place the player's piece on the grid
        grid[row, col] = player1 if player1 == 1 else player2

        # Display the current state of the board
        print(grid)

        # Check if the player has won
        if check_win(grid, player1 if player1 == 1 else player2):
            game_over = True
            if player1 == 1:
                player1_wins += 1
            else:
                player2_wins += 1
            print("Player {} wins!".format(player1 if player1 == 1 else player2))
            break

        # Check if the game is a draw
        if np.all(grid != 0):
            game_over = True
            print("Draw!")
            break

        # Switch the player's turns
        player1, player2 = player2, player1

    # Print the number of wins and losses for each player
    print("Player 1 wins:", player1_wins)
    print("Player 2 wins:", player2_wins)

def check_win(grid, player):
    # Check if there are three adjacent pieces in a row
    for i in range(grid.shape[0]):
        if np.all(grid[i, :] == player):
            return True

    # Check if there are three adjacent pieces in a column
    for j in range(grid.shape[1]):
        if np.all(grid[:, j] == player):
            return True

    # Check if there are three adjacent pieces in a diagonal
    if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
        return True

    # Otherwise, return False
    return False

def get_ai_move(grid, player, difficulty):
    # Get all possible moves for the AI opponent
    possible_moves = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 0:
                possible_moves.append((i, j))

    # Choose the best move for the AI opponent
    best_move = None
    if difficulty == 1:
        # Easy AI: Choose a random move from the list of possible moves
        best_move = random.choice(possible_moves)
    elif difficulty == 2:
        # Hard AI: Choose the move that gives the AI opponent the best chance of winning
        best_score = -np.inf
        for move in possible_moves:
            # Make the move on the grid
            grid[move[0], move[1]] = player

            # Check if the move results in a win for the AI opponent
            if check_win(grid, player):
                # The move results in a win, so it is the best move
                best_move = move
                break

            # Check if the move results in a draw
            elif np.all(grid != 0):
                # The move results in a draw, so it is not a good move
                continue

            # Check if the move results in a loss for the AI opponent
            else:
                # The move results in a loss, so it is not a good move
                continue

            # Get the score for the move
            score = minimax(grid, player, depth=0, maximizing=False)

            # If the score is better than the best score so far, then update the best move and score
            if score > best_score:
                best_move = move
                best_score = score

            # Undo the move
            grid[move[0], move[1]] = 0

    return best_move

def minimax(grid, player, depth, maximizing):
    # Check if the game is over
    if check_win(grid, player1 if player1 == 1 else player2):
        return 1 if player == player1 else -1
    elif np.all(grid != 0):
        return 0

    # Get all possible moves for the current player
    possible_moves = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 0:
                possible_moves.append((i, j))

    # Evaluate the possible moves for the current player
    scores = []
    for move in possible_moves:
        # Make the move on the grid
        grid[move[0], move[1]] = player

        # Get the score for the move
        score = minimax(grid, player, depth + 1, not maximizing)

        # Undo the move
        grid[move[0], move[1]] = 0

        # Add the score to the list of scores
        scores.append(score)

    # Return the best score for the current player
    if maximizing:
        return max(scores)
    else:
        return min(scores)

if __name__ == "__main__":
    jdv()
