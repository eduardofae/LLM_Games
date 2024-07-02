import numpy as np

def jdv():
    """
    A simple 2-player game played on a 3x3 grid.
    
    The objective of the game is to be the first player to get three of their pieces in a row, either horizontally, vertically, or diagonally.
    
    The game is played by taking turns placing your pieces into a free space on the grid.
    
    If a player succeeds in getting three of their pieces in a row, they win the game.
    
    If there are no more free spaces on the grid, the game is declared a draw.
    """
    
    # Create a 3x3 grid
    grid = np.zeros((3, 3))
    
    # Set up the players
    player1 = 'X'
    player2 = 'O'
    
    # Set up the game loop
    while True:
    
        # Get the current player's move
        move = input(f"{player1}'s turn: ")
        
        # Check if the move is valid
        if not (0 <= move[0] <= 2 and 0 <= move[1] <= 2 and grid[int(move[0]), int(move[1])] == 0):
            print("Invalid move. Please try again.")
            continue
        
        # Update the grid with the player's move
        grid[int(move[0]), int(move[1])] = player1
    
        # Check if the player has won
        if check_win(grid, player1):
            print(f"{player1} wins!")
            break
    
        # Check if the game is a draw
        if np.all(grid != 0):
            print("Draw!")
            break
    
        # Switch to the other player
        player1, player2 = player2, player1
    

def check_win(grid, player):
    """
    Checks if the given player has won the game.
    
    Args:
        grid (np.array): The current state of the game board.
        player (str): The player to check for a win.
    
    Returns:
        bool: True if the player has won, False otherwise.
    """
    
    # Check for a horizontal win
    for row in grid:
        if np.all(row == player):
            return True
    
    # Check for a vertical win
    for col in grid.T:
        if np.all(col == player):
            return True
    
    # Check for a diagonal win
    if np.all(grid.diagonal() == player):
        return True
    
    if np.all(np.flip(grid).diagonal() == player):
        return True
    
    return False


if __name__ == "__main__":
    jdv()
