import numpy as np
import pygame
import socket
import threading

# Create the game board
board = np.zeros((10, 10))

# Create a list of player symbols
player_symbols = ["X", "O"]

# Define the game state
game_state = "ongoing"

# Define the current player
current_player = 0

# Define the winning condition
winning_condition = 3

# Create a list to store the game history
game_history = []

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the font
font = pygame.font.SysFont("Arial", 24)

# Create a socket for online multiplayer
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 5000))
sock.listen(1)

# Define a function to handle incoming connections
def handle_connection(conn, addr):
    global game_state, current_player, board, game_history

    # Receive the player's symbol from the client
    symbol = conn.recv(1024).decode("utf-8")

    # Set the player's symbol
    if symbol == "X":
        current_player = 0
    elif symbol == "O":
        current_player = 1

    # Game loop
    while game_state == "ongoing":
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position
                mouse_pos = pygame.mouse.get_pos()

                # Convert the mouse position to a column number
                move = int(mouse_pos[0] / 40) + 1

                # Check if the move is valid
                if move < 1 or move > 10 or board[9, move - 1] != 0:
                    continue

                # Place the player's piece on the board
                for i in range(9, -1, -1):
                    if board[i, move - 1] == 0:
                        board[i, move - 1] = current_player + 1
                        break

                # Add the move to the game history
                game_history.append((move, current_player))

                # Send the move to the other player
                conn.sendall(f"{move},{current_player}".encode("utf-8"))

                # Check for a win
                for i in range(10):
                    for j in range(10):
                        if board[i, j] != 0 and board[i, j] == board[i, (j + 1) % 10] and board[i, j] == board[i, (j + 2) % 10]:
                            game_state = "win"
                            winner = current_player
                        elif board[i, j] != 0 and board[i, j] == board[(i + 1) % 10, j] and board[i, j] == board[(i + 2) % 10, j]:
                            game_state = "win"
                            winner = current_player
                        elif board[i, j] != 0 and board[i, j] == board[(i + 1) % 10, (j + 1) % 10] and board[i, j] == board[(i + 2) % 10, (j + 2) % 10]:
                            game_state = "win"
                            winner = current_player
                        elif board[i, j] != 0 and board[i, j] == board[(i + 1) % 10, (j - 1) % 10] and board[i, j] == board[(i + 2) % 10, (j - 2) % 10]:
                            game_state = "win"
                            winner = current_player

                # Check for a draw
                if np.all(board != 0):
                    game_state = "draw"

                # Switch the current player
                current_player = (current_player + 1) % 2

    # Send the game state to the other player
    conn.sendall(game_state.encode("utf-8"))

    # Close the connection
    conn.close()

# Create a thread to handle incoming connections
conn, addr = sock.accept()
thread = threading.Thread(target=handle_connection, args=(conn, addr))
thread.start()

# Game loop
while game_state == "ongoing":
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Convert the mouse position to a column number
            move = int(mouse_pos[0] / 40) + 1

            # Check if the move is valid
            if move < 1 or move > 10 or board[9, move - 1] != 0:
                continue

            # Place the player's piece on the board
            for i in range(9, -1, -1):
                if board[i, move - 1] == 0:
                    board[i, move - 1] = current_player + 1
                    break

            # Add the move to the game history
            game_history.append((move, current_player))

            # Check for a win
            for i in range(10):
                for j in range(10):
                    if board[i, j] != 0 and board[i, j] == board[i, (j + 1) % 10] and board[i, j] == board[i, (j + 2) % 10]:
                        game_state = "win"
                        winner = current_player
                    elif board[i, j] != 0 and board[i, j] == board[(i + 1) % 10, j] and board[i, j] == board[(i + 2) % 10, j]:
                        game_state = "win"
                        winner = current_player
                    elif board[i, j] != 0 and board[i, j] == board[(i + 1) % 10, (j + 1) % 10] and board[i, j] == board[(i + 2) % 10, (j + 2) % 10]:
                        game_state = "win"
                        winner = current_player
                    elif board[i, j] != 0 and board[i, j] == board[(i + 1) % 10, (j - 1) % 10] and board[i, j] == board[(i + 2) % 10, (j - 2) % 10]:
                        game_state = "win"
                        winner = current_player

            # Check for a draw
            if np.all(board != 0):
                game_state = "draw"

            # Switch the current player
            current_player = (current_player + 1) % 2

    # Draw the game board
    screen.fill(BLACK)
    for i in range(10):
        for j in range(10):
            if board[i, j] == 1:
                pygame.draw.circle(screen, RED, (j * 40 + 20, i * 40 + 20), 15)
            elif board[i, j] == 2:
                pygame.draw.circle(screen, BLUE, (j * 40 + 20, i * 40 + 20), 15)

    # Draw the game history
    text = font.render("Game History:", True, WHITE)
    screen.blit(text, (10, 410))
    for i, move in enumerate(game_history):
        text = font.render(f"{i + 1}. Player {player_symbols[move[1]]} moved to column {move[0]}", True)