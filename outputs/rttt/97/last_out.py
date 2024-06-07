import numpy as np

class JdvGame:
    def __init__(self):
        self.grid = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 for player 1, 2 for player 2
        self.winner = None
        self.draw = False
        self.game_stats = {"wins": {"player_1": 0, "player_2": 0, "ai": 0}, "draws": 0, "moves": 0}

    def play(self):
        while not self.winner and not self.draw:
            self.display_grid()
            try:
                move = self.get_player_move()
                self.place_piece(move)
                self.check_win()
                self.check_draw()
                self.switch_player()
            except ValueError as e:
                print(e)

        if self.winner:
            self.update_game_stats(self.winner)
            print(f"{self.winner} wins!")
        elif self.draw:
            self.update_game_stats("draw")
            print("Draw!")

    def display_grid(self):
        for row in self.grid:
            print("|".join(["X" if cell == 1 else "O" if cell == 2 else " " for cell in row]))
            print("-----")

    def get_player_move(self):
        while True:
            try:
                move = input(f"Player {self.current_player}, enter your move (row, column): ")
                row, column = map(int, move.split(","))
                if self.grid[row, column] == 0:
                    return row, column
                else:
                    print("Invalid move. That space is already taken.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")

    def place_piece(self, move):
        row, column = move
        self.grid[row, column] = self.current_player
        self.game_stats["moves"] += 1

    def check_win(self):
        # Check rows
        for row in self.grid:
            if np.all(row == self.current_player):
                self.winner = self.current_player
                return

        # Check columns
        for column in self.grid.T:
            if np.all(column == self.current_player):
                self.winner = self.current_player
                return

        # Check diagonals
        if np.all(self.grid.diagonal() == self.current_player) or np.all(np.flip(self.grid).diagonal() == self.current_player):
            self.winner = self.current_player
            return

    def check_draw(self):
        if np.all(self.grid != 0):
            self.draw = True

    def switch_player(self):
        self.current_player = 3 - self.current_player  # Switch between 1 and 2

    def update_game_stats(self, winner):
        if winner == "player_1":
            self.game_stats["wins"]["player_1"] += 1
        elif winner == "player_2":
            self.game_stats["wins"]["player_2"] += 1
        elif winner == "ai":
            self.game_stats["wins"]["ai"] += 1
        else:
            self.game_stats["draws"] += 1

    def display_game_stats(self):
        print("Game Statistics:")
        for player, wins in self.game_stats["wins"].items():
            print(f"{player}: {wins} wins")
        print(f"Draws: {self.game_stats['draws']}")
        print(f"Total moves: {self.game_stats['moves']}")


if __name__ == "__main__":
    game = JdvGame()
    game.play()
    game.display_game_stats()
