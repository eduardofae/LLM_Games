import numpy as np
import unittest

class Game:
    def __init__(self, grid_size=10):
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.players = ['X', 'O']
        self.current_player = 0
        self.game_state = 'in progress'

    def play(self):
        print('Welcome to Pong!')
        print(f'Grid size: {self.grid.shape[0]}x{self.grid.shape[1]}')

        while self.game_state == 'in progress':
            column = self.get_player_input()
            if column is None:
                continue
            self.place_piece(column)
            self.check_win()
            self.switch_player()
            self.display_grid()

            if self.game_state == 'won':
                print(f'Player {self.players[self.current_player]} wins!')
            elif self.game_state == 'draw':
                print('Draw!')

    def get_player_input(self):
        while True:
            try:
                column = int(input(f'Player {self.players[self.current_player]}, choose a column (0-{self.grid.shape[1]-1}) or "q" to quit: '))
                if column < 0 or column >= self.grid.shape[1]:
                    print('Invalid column')
                    continue
                elif column == 'q':
                    print('Exiting game...')
                    exit()
                break
            except ValueError:
                print('Invalid input')

        return column

    def place_piece(self, column):
        try:
            for i in range(self.grid.shape[0]-1, -1, -1):
                if self.grid[i, column] == 0:
                    self.grid[i, column] = self.players[self.current_player]
                    break
        except IndexError:
            print('Invalid column')

    def check_win(self):
        # Horizontal checks
        for i in range(self.grid.shape[0]):
            if np.all(self.grid[i, :] == self.players[self.current_player]):
                self.game_state = 'won'
                return

        # Vertical checks
        for j in range(self.grid.shape[1]):
            if np.all(self.grid[:, j] == self.players[self.current_player]):
                self.game_state = 'won'
                return

        # Diagonal checks
        for i in range(self.grid.shape[0]-2):
            for j in range(self.grid.shape[1]-2):
                if np.all(self.grid[i+k, j+k] == self.players[self.current_player] for k in range(3)):
                    self.game_state = 'won'
                    return

        for i in range(2, self.grid.shape[0]):
            for j in range(self.grid.shape[1]-2):
                if np.all(self.grid[i-k, j+k] == self.players[self.current_player] for k in range(3)):
                    self.game_state = 'won'
                    return

        # Draw check
        if np.all(self.grid != 0):
            self.game_state = 'draw'

    def switch_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def display_grid(self):
        print(self.grid)

class GameTest(unittest.TestCase):

    def test_place_piece(self):
        game = Game()
        game.place_piece(0)
        self.assertEqual(game.grid[9, 0], 'X')

if __name__ == '__main__':
    grid_size = int(input('Enter the grid size (e.g., 10): '))
    game = Game(grid_size)
    game.play()
