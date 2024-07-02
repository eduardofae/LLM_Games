import numpy as np
import pygame
import sys

# Initialize PyGame
pygame.init()

# Set the screen size
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Connect Four")

# Define the colors
colors = {'X': (255, 0, 0), 'O': (0, 255, 0), 'empty': (0, 0, 0)}

# Define the sound effects
sound_effects = {'place': pygame.mixer.Sound('place.wav'), 'win': pygame.mixer.Sound('win.wav')}

# Define the animations
animations = {'place': pygame.sprite.GroupSingle(), 'win': pygame.sprite.GroupSingle()}

# Create a function to load an image
def load_image(path):
    image = pygame.image.load(path).convert_alpha()
    return image

# Create a class for the game board
class Board:
    def __init__(self):
        self.grid = np.zeros((10, 10), dtype=int)

    def place_piece(self, column, player):
        for i in range(9, -1, -1):
            if self.grid[i, column] == 0:
                self.grid[i, column] = player
                break

    def check_win(self, player):
        # Check for horizontal win
        for row in range(10):
            if all(self.grid[row, i] == player for i in range(10)):
                return True

        # Check for vertical win
        for col in range(10):
            if all(self.grid[i, col] == player for i in range(10)):
                return True

        # Check for diagonal win
        for i in range(10):
            if all(self.grid[i, i] == player):
                return True
            if all(self.grid[i, 9-i] == player):
                return True

        # No win yet
        return False

# Create a class for the AI player
class AI:
    def __init__(self, difficulty_level):
        self.difficulty_level = difficulty_level

    def get_move(self, board):
        if self.difficulty_level == 'easy':
            return self.get_random_move(board)
        elif self.difficulty_level == 'medium':
            return self.get_minimax_move(board)
        elif self.difficulty_level == 'hard':
            return self.get_alphabeta_move(board)

    def get_random_move(self, board):
        while True:
            column = np.random.randint(10)
            if board.grid[0, column] == 0:
                return column

    def get_minimax_move(self, board):
        best_score = -np.inf
        best_column = None
        for column in range(10):
            if board.grid[0, column] == 0:
                board.place_piece(column, 'O')
                score = self.minimax(board, False)
                board.grid[0, column] = 0
                if score > best_score:
                    best_score = score
                    best_column = column
        return best_column

    def get_alphabeta_move(self, board):
        best_score = -np.inf
        best_column = None
        alpha = -np.inf
        beta = np.inf
        for column in range(10):
            if board.grid[0, column] == 0:
                board.place_piece(column, 'O')
                score = self.alphabeta(board, False, alpha, beta)
                board.grid[0, column] = 0
                if score > best_score:
                    best_score = score
                    best_column = column
        return best_column