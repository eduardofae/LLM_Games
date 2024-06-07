import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3), dtype=int)

# Define the players
player1 = 1
player2 = -1

# Define the winning combinations
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

# Define the game state
game_state = "ongoing"

# Start the game
while game_state == "ongoing":
    # Get the player's move
    move = int(input("Player {}'s turn: ".format(player1 if player1 == 1 else player2)))

    # Place the player's piece in the grid
    grid[move // 3][move % 3] = player1 if player1 == 1 else player2

    # Check if the player has won
    for combination in winning_combinations:
        if grid[combination[0]] == grid[combination[1]] == grid[combination[2]]:
            if grid[combination[0]] == player1:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            game_state = "finished"
            break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        game_state = "finished"
        break

    # Switch the player
    player1, player2 = player2, player1

# Ask the players if they want to play again
play_again = input("Do you want to play again? (y/n) ")

# If the players want to play again, reset the game
if play_again == "y":
    grid = np.zeros((3, 3), dtype=int)
    game_state = "ongoing"
