import numpy as np
import pygame
import time
import socket
import json

# Initialize the game board
board = np.array([[' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']])

# Initialize the player's turn
player = 1

# Initialize the computer's difficulty level
difficulty = 1

# Initialize the game mode
game_mode = "timed"

# Initialize the pygame display
pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the font
font = pygame.font.SysFont("Arial", 24)

# Initialize the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 5000))
sock.listen(1)

# Initialize the leaderboard
leaderboard = []

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Convert the mouse position to a row and column on the board
            row = mouse_y // 100
            column = mouse_x // 100
            
            # Check if the move is valid
            if 0 <= row < 3 and 0 <= column < 3 and board[row][column] == ' ':
                # Place the player's piece on the board
                board[row][column] = 'X'
                
                # Check if the player has won
                if check_winner(board) == 'X':
                    print("Player 1 wins!")
                    pygame.quit()
                    sys.exit()
                
                # Check if the board is full
                if np.all(board != ' '):
                    print("It's a draw.")
                    pygame.quit()
                    sys.exit()
                
                # Send the move to the other player
                data = {'row': row, 'column': column}
                sock.sendall(json.dumps(data).encode('utf-8'))
                
                # Get the other player's move
                data = sock.recv(1024).decode('utf-8')
                data = json.loads(data)
                row = data['row']
                column = data['column']
                
                # Check if the move is valid
                if 0 <= row < 3 and 0 <= column < 3 and board[row][column] == ' ':
                    # Place the other player's piece on the board
                    board[row][column] = 'O'
                    
                    # Check if the other player has won
                    if check_winner(board) == 'O':
                        print("Player 2 wins!")
                        pygame.quit()
                        sys.exit()
                    
                    # Check if the board is full
                    if np.all(board != ' '):
                        print("It's a draw.")
                        pygame.quit()
                        sys.exit()

    # Draw the game board
    screen.fill(BLACK)
    for row in range(3):
        for column in range(3):
            if board[row][column] == 'X':
                pygame.draw.circle(screen, RED, (column * 100 + 50, row * 100 + 50), 40)
            elif board[row][column] == 'O':
                pygame.draw.circle(screen, BLUE, (column * 100 + 50, row * 100 + 50), 40)

    # Display the game mode
    text_surface = font.render(game_mode, True, WHITE)
    screen.blit(text_surface, (10, 10))

    # Display the difficulty level
    text_surface = font.render("Difficulty: {}".format(difficulty), True, WHITE)
    screen.blit(text_surface, (10, 30))

    # Display the leaderboard
    text_surface = font.render("Leaderboard:", True, WHITE)
    screen.blit(text_surface, (10, 60))
    for i, score in enumerate(leaderboard):
        text_surface = font.render("{}. {}".format(i + 1, score), True, WHITE)
        screen.blit(text_surface, (10, 80 + 20 * i))

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Check if the player has won
def check_winner(board):
    # Check the rows
    for row in board:
        if np.all(row == row[0]) and row[0] != ' ':
            return row[0]

    # Check the columns
    for column in range(3):
        if np.all(board[:, column] == board[0, column]) and board[0, column] != ' ':
            return board[0, column]

    # Check the diagonals
    if np.all(board.diagonal() == board[0, 0]) and board[0, 0] != ' ':
        return board[0, 0]
    if np.all(np.flip(board).diagonal() == board[0, 2]) and board[0, 2] != ' ':
        return board[0, 2]

    # No winner yet
    return None

# Minimax algorithm
def minimax(board, player):
    # Check if the game is over
    winner = check_winner(board)
    if winner is not None:
        if winner == 'X':
            return -1
        elif winner == 'O':
            return 1
        else:
            return 0

    # Get all possible moves
    moves = []
    for row in range(3):
        for column in range(3):
            if board[row][column] == ' ':
                moves.append((row, column))

    # Evaluate each possible move
    scores = []
    for move in moves:
        board[move[0]][move[1]] = 'O'
        score = -minimax(board, 1)
        board[move[0]][move[1]] = ' '
        scores.append(score)

    # Get the best move
    best_move = moves[np.argmax(scores)]

    return best_move

# Reset the game
def reset_game():
    board[:] = ' '
    player = 1

# Main game loop
while True:
    jdv()
    choice = input("Play again? (y/n) ")
    if choice == 'y':
        reset_game()
    else:
        break
