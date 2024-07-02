import numpy as np
import websockets

async def jdv(websocket, path):
    """
    Plays a game of jdv against another human player online.

    Args:
        websocket: The websocket connection to the other player.
        path: The path to the websocket endpoint.

    Returns:
        None
    """

    # Create a 3x3 grid
    grid = np.zeros((3, 3), dtype=int)

    # Set the current player to 1
    current_player = 1

    # Keep track of the scores of the two players
    player1_score = 0
    player2_score = 0

    # Loop until the game is over
    while True:
        # Print the grid
        print(grid)

        # Get the player's move
        if current_player == 1:
            move = await websocket.recv()
        else:
            move = await get_computer_move(grid, current_player)

        # Convert the move to a row and column
        try:
            row, column = map(int, move.split(","))
        except ValueError:
            print("Invalid move. Please try again.")
            continue

        # Check if the move is valid
        if grid[row, column] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the grid
        grid[row, column] = current_player

        # Check if the player has won
        if check_win(grid, current_player):
            print(f"Player {current_player} wins!")
            if current_player == 1:
                player1_score += 1
            else:
                player2_score += 1
            break

        # Check if the game is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch to the other player
        current_player = 3 - current_player

    # Print the final scores
    print(f"Player 1: {player1_score}")
    print(f"Player 2: {player2_score}")

def check_win(grid, player):
    """
    Checks if a player has won.

    Args:
        grid: A 3x3 grid.
        player: The player to check.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win in each row
    for row in range(3):
        if np.all(grid[row, :] == player):
            return True

    # Check for a win in each column
    for column in range(3):
        if np.all(grid[:, column] == player):
            return True

    # Check for a win in each diagonal
    if np.all(grid.diagonal() == player):
        return True
    if np.all(np.flip(grid).diagonal() == player):
        return True

    # No win found
    return False

def reset_grid():
    """
    Resets the game board to all zeros.
    """

    global grid

    grid = np.zeros((3, 3), dtype=int)

def get_computer_move(grid, player):
    """
    Gets the best move for the computer to make.

    Args:
        grid: A 3x3 grid.
        player: The player to make the move for.

    Returns:
        A tuple representing the row and column of the best move.
    """

    # Get all possible moves for the computer
    possible_moves = []
    for row in range(3):
        for column in range(3):
            if grid[row, column] == 0:
                possible_moves.append((row, column))

    # Evaluate each possible move and choose the best one
    best_move = None
    best_score = -np.inf if player == 1 else np.inf
    for move in possible_moves:
        # Make the move on a copy of the grid
        grid_copy = grid.copy()
        grid_copy[move[0], move[1]] = player

        # Check if the move wins the game
        if check_win(grid_copy, player):
            return move

        # Otherwise, evaluate the move using the minimax algorithm
        score = minimax(grid_copy, 3 - player)

        # If the score is better than the best score so far, update the best move and score
        if player == 1:
            best_score = max(best_score, score)
        else:
            best_score = min(best_score, score)

    # Return the best move
    return best_move

def minimax(grid, player):
    """
    Uses the minimax algorithm to evaluate a move.

    Args:
        grid: A 3x3 grid.
        player: The player to make the move for.

    Returns:
        The score of the move.
    """

    # Check if the game is over
    if check_win(grid, player):
        return 1
    elif check_win(grid, 3 - player):
        return -1
    elif np.all(grid != 0):
        return 0

    # Get all possible moves for the player
    possible_moves = []
    for row in range(3):
        for column in range(3):
            if grid[row, column] == 0:
                possible_moves.append((row, column))

    # Evaluate each possible move and choose the best one
    best_score = -np.inf if player == 1 else np.inf
    for move in possible_moves:
        # Make the move on a copy of the grid
        grid_copy = grid.copy()
        grid_copy[move[0], move[1]] = player

        # Recursively call minimax to evaluate the move
        score = minimax(grid_copy, 3 - player)

        # If the score is better than the best score so far, update the best score
        if player == 1:
            best_score = max(best_score, score)
        else:
            best_score = min(best_score, score)

    # Return the best score
    return best_score

if __name__ == "__main__":
    websockets.serve(jdv, "localhost", 8765)
    websockets.run_forever()
