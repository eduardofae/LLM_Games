import pygame
import unittest

# Create a 3x3 grid
grid = [[' ' for _ in range(3)] for _ in range(3)]

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Get the players' names
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")

# Function to check if a player has won
def check_win(symbol):
    """
    Checks if a player has won the game.

    Args:
        symbol (str): The player's symbol.

    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check for horizontal wins
    for row in grid:
        if check_line(symbol, row):
            return True

    # Check for vertical wins
    for col in range(3):
        column = [row[col] for row in grid]
        if check_line(symbol, column):
            return True

    # Check for diagonal wins
    diagonal1 = [grid[0][0], grid[1][1], grid[2][2]]
    diagonal2 = [grid[0][2], grid[1][1], grid[2][0]]
    if check_line(symbol, diagonal1) or check_line(symbol, diagonal2):
        return True

    # No win yet
    return False

# Function to check if a line (row, column, or diagonal) has three of the same symbol
def check_line(symbol, line):
    """
    Checks if a line (row, column, or diagonal) has three of the same symbol.

    Args:
        symbol (str): The symbol to check for.
        line (list): The line to check.

    Returns:
        bool: True if the line has three of the same symbol, False otherwise.
    """
    return line[0] == line[1] == line[2] == symbol

# Function to print the grid
def print_grid():
    for row in grid:
        print(' '.join(row))

# Function to get a valid move from the player
def get_move(player_symbol):
    while True:
        try:
            move = input(f"{player_symbol}'s turn (row, column): ")
            row, col = map(int, move.split(','))
            if 0 <= row < 3 and 0 <= col < 3 and grid[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid move. Try again.")

# Game loop
player_turn = 0
while True:
    # Get the current player's symbol
    if player_turn % 2 == 0:
        symbol = player1_symbol
        player_name = player1_name
    else:
        symbol = player2_symbol
        player_name = player2_name

    # Get the player's move
    row, col = get_move(symbol)

    # Place the player's symbol on the grid
    grid[row][col] = symbol

    # Print the grid
    print_grid()

    # Check if the player has won
    if check_win(symbol):
        print(f"{player_name} wins!")
        break

    # Check if the game is a draw
    if all(all(cell != ' ' for cell in row) for row in grid):
        print("It's a draw!")
        break

    # Switch turns
    player_turn += 1

# Ask the players if they want to play again
while True:
    play_again = input("Do you want to play again (y/n)? ")
    if play_again == 'y':
        # Reset the grid and start a new game
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        player_turn = 0
        print_grid()
    else:
        break


# Unit tests
class JdvTests(unittest.TestCase):

    def test_check_win_horizontal(self):
        grid[0] = ['X', 'X', 'X']
        self.assertTrue(check_win('X'))

    def test_check_win_vertical(self):
        grid[0][0] = 'X'
        grid[1][0] = 'X'
        grid[2][0] = 'X'
        self.assertTrue(check_win('X'))

    def test_check_win_diagonal(self):
        grid[0][0] = 'X'
        grid[1][1] = 'X'
        grid[2][2] = 'X'
        self.assertTrue(check_win('X'))

    def test_check_win_no_win(self):
        self.assertFalse(check_win('X'))


# PyGame GUI
pygame.init()

# Set the game window size
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color
background_color = (255, 255, 255)
screen.fill(background_color)

# Create a font object
font = pygame.font.SysFont('Arial', 40)

# Create a text surface for the player's turn
player_turn_text = font.render("Player 1's turn", True, (0, 0, 0))
player_turn_rect = player_turn_text.get_rect()
player_turn_rect.center = (screen_width // 2, screen_height // 2)

# Create a text surface for the game status
game_status_text = font.render(" ", True, (0, 0, 0))
game_status_rect = game_status_text.get_rect()
game_status_rect.center = (screen_width // 2, screen_height // 2 + 50)

# Draw the initial game state
screen.blit(player_turn_text, player_turn_rect)
screen.blit(game_status_text, game_status_rect)
pygame.display.update()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Convert the mouse position to a grid coordinate
            row = mouse_pos[1] // 200
            col = mouse_pos[0] // 200

            # Check if the grid coordinate is valid and empty
            if 0 <= row < 3 and 0 <= col < 3 and grid[row][col] == ' ':
                # Place the player's symbol on the grid
                if player_turn % 2 == 0:
                    symbol = player1_symbol
                else:
                    symbol = player2_symbol
                grid[row][col] = symbol

                # Update the game state
                if check_win(symbol):
                    game_status_text = font.render(f"{player_name} wins!", True, (0, 0, 0))
                    running = False
                elif all(all(cell != ' ' for cell in row) for row in grid):
                    game_status_text = font.render("It's a draw!", True, (0, 0, 0))
                    running = False
                else:
                    # Switch turns
                    player_turn += 1
                    if player_turn % 2 == 0:
                        player_turn_text = font.render("Player 1's turn", True, (0, 0, 0))
                    else:
                        player_turn_text = font.render("Player 2's turn", True, (0, 0, 0))

                # Redraw the game state
                screen.fill(background_color)
                print_grid()
                screen.blit(player_turn_text, player_turn_rect)
                screen.blit(game_status_text, game_status_rect)
                pygame.display.update()

        # Handle errors
        except Exception as e:
            print(f"Error: {e}")
            running = False

# Quit pygame
pygame.quit()
