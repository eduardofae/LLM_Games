import numpy as np

class Game:
    def __init__(self):
        self.grid = np.zeros((10, 10), dtype=int)
        self.player = 1

    def print_grid(self):
        for row in self.grid:
            for cell in row:
                print(cell, end=" ")
            print()

    def check_win(self):
        # Check rows and columns
        for row in self.grid:
            if np.any(np.diff(row) == 0) and row[0] != 0:
                return True
        for col in range(10):
            column = [row[col] for row in self.grid]
            if np.any(np.diff(column) == 0) and column[0] != 0:
                return True

        # Check diagonals
        diagonals = [
            [self.grid[i][i] for i in range(10)],
            [self.grid[i][9-i] for i in range(10)]
        ]
        for diagonal in diagonals:
            if np.any(np.diff(diagonal) == 0) and diagonal[0] != 0:
                return True

        return False

    def check_draw(self):
        return np.all(self.grid != 0)

    def play_turn(self):
        while True:
            try:
                column = int(input(f"Player {self.player}, choose a column (0-9): "))
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 9.")
            else:
                if 0 <= column <= 9:
                    break
                else:
                    print("Invalid input. Please enter a number between 0 and 9.")

        if self.grid[0][column] != 0:
            print("Column is full. Please choose another column.")
            return

        for row in range(9, -1, -1):
            if self.grid[row][column] == 0:
                self.grid[row][column] = self.player
                break

        self.player = (self.player % 2) + 1

def main():
    game = Game()

    while True:
        game.print_grid()

        game.play_turn()

        if game.check_win():
            game.print_grid()
            print(f"Player {game.player} wins!")
            break

        if game.check_draw():
            game.print_grid()
            print("Draw!")
            break

if __name__ == "__main__":
    main()
