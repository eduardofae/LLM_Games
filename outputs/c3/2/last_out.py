import numpy as np
import random
import time

# Create the game board
board = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

# Define the current player
current_player = 0

# Define the game state
game_state = "playing"

# Create a graphical user interface
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pong")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Game loop
while game_state == "playing":
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = "quit"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = "quit"
            elif event.key == pygame.K_SPACE:
                # Undo the last move
                if len(moves) > 0:
                    board[moves[-1]] = 0
                    moves.pop()
                    current_player = (current_player + 1) % 2

    # Get the column where the player wants to place their piece
    column = get_column(current_player)

    # Check if the column is full
    if board[9, column] != 0:
        print("The column is full. Please choose another column.")
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if board[i, column] == 0:
            board[i, column] = players[current_player]
            moves.append((i, column))
            break

    # Check if the player has won
    if check_win(board, players[current_player]):
        print(f"Player {players[current_player]} wins!")
        game_state = "over"

    # Check if the game is a draw
    if np.all(board != 0):
        print("The game is a draw.")
        game_state = "over"

    # Switch to the other player
    current_player = (current_player + 1) % 2

    # Draw the game board
    draw_board(board)

    # Update the display
    pygame.display.update()

    # Clock tick
    clock.tick(60)

# Quit the game
pygame.quit()
