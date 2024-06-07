import curses

class JdvGame:
    def __init__(self, grid_size=3, difficulty='easy'):
        self.grid_size = grid_size
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.player_turn = 1
        self.player_wins = {1: 0, 2: 0}
        self.draws = 0
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        self.difficulty = difficulty

    def print_grid(self):
        self.screen.clear()
        for row in self.grid:
            self.screen.addstr(' '.join(row) + '\n')

    def place_piece(self, row, col):
        if self.grid[row][col] == ' ':
            if self.player_turn == 1:
                self.grid[row][col] = 'X'
            else:
                self.grid[row][col] = 'O'
            self.player_turn = 3 - self.player_turn

    def check_win(self):
        # Check rows
        for row in self.grid:
            if all(cell == row[0] and cell != ' ' for cell in row):
                return True

        # Check columns
        for col in range(self.grid_size):
            if all(self.grid[row][col] == self.grid[0][col] and self.grid[0][col] != ' ' for row in range(self.grid_size)):
                return True

        # Check diagonals
        if all(self.grid[i][i] == self.grid[0][0] and self.grid[0][0] != ' ' for i in range(self.grid_size)):
            return True
        if all(self.grid[i][self.grid_size - 1 - i] == self.grid[0][self.grid_size - 1] and self.grid[0][self.grid_size - 1] != ' ' for i in range(self.grid_size)):
            return True

        return False

    def check_draw(self):
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def ai_move(self):
        if self.difficulty == 'easy':
            # Randomly place a piece in an empty cell
            while True:
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)
                if self.grid[row][col] == ' ':
                    self.place_piece(row, col)
                    break
        elif self.difficulty == 'hard':
            # Implement a more sophisticated AI algorithm, such as minimax or alpha-beta pruning

    def play(self):
        self.screen.addstr("Welcome to Jdv!\n")
        self.screen.addstr("Use the arrow keys to move and press space to place a piece.\n")
        self.screen.addstr("Press 'q' to quit.\n")
        self.screen.getch()

        while True:
            self.print_grid()
            key = self.screen.getch()

            if key == curses.KEY_UP:
                row = max(0, self.row - 1)
            elif key == curses.KEY_DOWN:
                row = min(self.grid_size - 1, self.row + 1)
            elif key == curses.KEY_LEFT:
                col = max(0, self.col - 1)
            elif key == curses.KEY_RIGHT:
                col = min(self.grid_size - 1, self.col + 1)
            elif key == ord(' '):
                if self.grid[row][col] != ' ':
                    continue
                self.place_piece(row, col)

                if self.check_win():
                    self.print_grid()
                    self.screen.addstr("Player {} wins!".format(3 - self.player_turn))
                    self.player_wins[3 - self.player_turn] += 1
                    self.screen.getch()
                    break
                elif self.check_draw():
                    self.print_grid()
                    self.screen.addstr("Draw!")
                    self.draws += 1
                    self.screen.getch()
                    break
            elif key == ord('q'):
                break
            elif self.player_turn == 2:
                self.ai_move()

                if self.check_win():
                    self.print_grid()
                    self.screen.addstr("AI wins!")
                    self.player_wins[2] += 1
                    self.screen.getch()
                    break
                elif self.check_draw():
                    self.print_grid()
                    self.screen.addstr("Draw!")
                    self.draws += 1
                    self.screen.getch()
                    break

        self.screen.addstr("\nGame Statistics:\n")
        for player, wins in self.player_wins.items():
            self.screen.addstr("Player {}: {} wins\n".format(player, wins))
        self.screen.addstr("Draws: {}\n".format(self.draws))
        self.screen.getch()

        curses.endwin()

if __name__ == "__main__":
    game = JdvGame()
    game.play()
