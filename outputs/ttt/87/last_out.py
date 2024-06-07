import numpy as np

class JdvGame:
    GRID_SIZE = 3
    PLAYERS = ["X", "O"]

    def __init__(self):
        self.grid = np.array([[" " for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)])
        self.current_player = self.PLAYERS[0]
        self.winner = None

    def print_grid(self):
        print("\n".join([" ".join(row) for row in self.grid]))

    def check_winner(self):
        # Check rows
        for row in self.grid:
            if len(set(row)) == 1 and row[0] != " ":
                return row[0]

        # Check columns
        for col in range(self.GRID_SIZE):
            column = [row[col] for row in self.grid]
            if len(set(column)) == 1 and column[0] != " ":
                return column[0]

        # Check diagonals
        diagonals = [[self.grid[i][i] for i in range(self.GRID_SIZE)],
                     [self.grid[i][self.GRID_SIZE - i - 1] for i in range(self.GRID_SIZE)]]
        for diagonal in diagonals:
            if len(set(diagonal)) == 1 and diagonal[0] != " ":
                return diagonal[0]

        return None

    def play_move(self, row, col):
        if self.grid[row, col] == " ":
            self.grid[row, col] = self.current_player
            self.winner = self.check_winner()
            if self.winner is not None:
                return True
            else:
                # Switch player
                self.current_player = self.PLAYERS[(self.PLAYERS.index(self.current_player) + 1) % len(self.PLAYERS)]
        return False

    def is_draw(self):
        return np.all(self.grid != " ") and self.winner is None

    def start(self):
        while True:
            try:
                self.print_grid()

                # Get player's move
                while True:
                    row, col = map(int, input(f"Enter your move, {self.current_player} (row, column): ").split())
                    if 0 <= row < self.GRID_SIZE and 0 <= col < self.GRID_SIZE:
                        if self.play_move(row, col):
                            break
                        else:
                            print("Invalid move. Try again.")
                    else:
                        print("Invalid input. Try again.")

                # Check for winner or draw
                if self.winner is not None or self.is_draw():
                    break
            except ValueError:
                print("Invalid input. Try again.")

        self.print_grid()
        if self.winner is not None:
            print(f"{self.winner} wins!")
        else:
            print("Draw!")


if __name__ == "__main__":
    game = JdvGame()
    game.start()
