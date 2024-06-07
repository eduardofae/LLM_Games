import numpy as np
import pygame

class Pong:
  def __init__(self, grid_size=10):
    self.grid_size = grid_size
    self.players = [player1_symbol, player2_symbol]
    self.grid = np.zeros((self.grid_size, self.grid_size))
    self.current_player = self.players[0]
    self.game_status = 'ongoing'
    self.sound_effects = {
      'place_piece': pygame.mixer.Sound('place_piece.wav'),
      'win': pygame.mixer.Sound('win.wav'),
      'draw': pygame.mixer.Sound('draw.wav')
    }

  def run(self):
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Set the screen size
    screen_width = self.grid_size * 100
    screen_height = self.grid_size * 100
    self.screen = pygame.display.set_mode((screen_width, screen_height))

    # Set the game title
    pygame.display.set_caption('Pong')

    # Main game loop
    while self.game_status == 'ongoing':
      # Handle events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

        # Handle player input
        if event.type == pygame.MOUSEBUTTONDOWN:
          # Get the mouse position
          mouse_x, mouse_y = pygame.mouse.get_pos()

          # Convert the mouse position to a grid coordinate
          column = mouse_x // 100

          # Check if the column is valid
          if column < 0 or column >= self.grid_size:
            continue

          # Check if the column is full
          if self.grid[9, column] != 0:
            continue

          # Place the player's piece in the lowest free space of the column
          for row in range(9, -1, -1):
            if self.grid[row, column] == 0:
              self.grid[row, column] = self.current_player
              self.sound_effects['place_piece'].play()
              break

          # Check if the player has won
          if self.check_win(self.current_player):
            self.game_status = 'win'
            self.sound_effects['win'].play()
            print(f'{self.current_player} wins!')
          # Check if the game is a draw
          elif np.all(self.grid != 0):
            self.game_status = 'draw'
            self.sound_effects['draw'].play()
            print('Draw!')

          # Switch the current player
          self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

      # Draw the game grid
      self.screen.fill(black)
      for row in range(self.grid_size):
        for column in range(self.grid_size):
          if self.grid[row, column] == player1_symbol:
            color = red
          elif self.grid[row, column] == player2_symbol:
            color = blue
          else:
            color = white
          pygame.draw.rect(self.screen, color, (column * 100, row * 100, 100, 100))

      # Update the display
      pygame.display.update()

  def check_win(self, player):
    # Check for horizontal wins
    for row in range(self.grid_size):
      if all(self.grid[row, i] == player for i in range(3)):
        return True

    # Check for vertical wins
    for column in range(self.grid_size):
      if all(self.grid[i, column] == player for i in range(3)):
        return True

    # Check for diagonal wins
    for row in range(self.grid_size - 2):
      for column in range(self.grid_size - 2):
        if all(self.grid[row + i, column + i] == player for i in range(3)):
          return True

    # Check for anti-diagonal wins
    for row in range(self.grid_size - 2):
      for column in range(2, self.grid_size):
        if all(self.grid[row + i, column - i] == player for i in range(3)):
          return True

    # No win found
    return False

if __name__ == '__main__':
  # Create a new game
  game = Pong()

  # Run the game
  game.run()
