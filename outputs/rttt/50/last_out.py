import pygame
import sys

# Initialize pygame
pygame.init()

# Set the screen size
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color
bg_color = (255, 255, 255)

# Create the game grid
grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

# Create a list of the players
players = ['X', 'O']

# Set the current player to the first player in the list
current_player = players[0]

# Create a function to check if a player has won
def check_win(grid):
  # Check for a win horizontally
  for row in grid:
    if row[0] == row[1] == row[2] and row[0] != ' ':
      return True

  # Check for a win vertically
  for col in range(3):
    if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
      return True

  # Check for a win diagonally
  if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
    return True
  if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
    return True

  # Return False if there is no win
  return False

# Create a function to check if the game is a draw
def check_draw(grid):
  # Check if all the spaces are filled
  for row in grid:
    for space in row:
      if space == ' ':
        return False

  # Return True if the game is a draw
  return True

# Create a function to get the player's input
def get_input(grid):
  # Get the player's mouse input
  mouse_pos = pygame.mouse.get_pos()

  # Calculate the row and column of the mouse click
  row = mouse_pos[1] // 133
  column = mouse_pos[0] // 133

  # Check if the space is empty
  if grid[row][column] != ' ':
    return None  # Return None if the space is already taken

  # Return the player's input
  return row, column

# Create a function to draw the game grid
def draw_grid(screen, grid):
  # Set the line color
  line_color = (0, 0, 0)

  # Draw the horizontal lines
  for i in range(1, 3):
    pygame.draw.line(screen, line_color, (0, i * 133), (400, i * 133), 3)

  # Draw the vertical lines
  for i in range(1, 3):
    pygame.draw.line(screen, line_color, (i * 133, 0), (i * 133, 400), 3)

  # Draw the grid cells
  for row in range(3):
    for column in range(3):
      if grid[row][column] == 'X':
        pygame.draw.line(screen, (255, 0, 0), (column * 133 + 10, row * 133 + 10), (column * 133 + 123, row * 133 + 123), 3)
        pygame.draw.line(screen, (255, 0, 0), (column * 133 + 123, row * 133 + 10), (column * 133 + 10, row * 133 + 123), 3)
      elif grid[row][column] == 'O':
        pygame.draw.circle(screen, (0, 0, 255), (column * 133 + 67, row * 133 + 67), 60, 3)

# Create a function to play the game
def play_game():
  # Loop until the game is over
  while True:
    # Fill the screen with the background color
    screen.fill(bg_color)

    # Draw the game grid
    draw_grid(screen, grid)

    # Check for events
    for event in pygame.event.get():
      # Check if the user has clicked the close button
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      # Check if the user has clicked the mouse
      if event.type == pygame.MOUSEBUTTONDOWN:
        # Get the player's input
        row, column = get_input(grid)

        # Check if the input is valid
        if row is not None and column is not None:
          # Place the player's piece in the grid
          grid[row][column] = current_player

          # Check if the player has won
          if check_win(grid):
            print(f"{current_player} wins!")
            pygame.quit()
            sys.exit()

          # Check if the game is a draw
          if check_draw(grid):
            print("The game is a draw.")
            pygame.quit()
            sys.exit()

          # Switch to the other player
          current_player = players[(players.index(current_player) + 1) % 2]

    # Update the display
    pygame.display.update()

# Play the game
if __name__ == "__main__":
    play_game()
