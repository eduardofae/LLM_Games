import numpy as np

class Jdv:
    def __init__(self):
        self.grid = np.zeros((3, 3), dtype=int)
        self.turn = 1  # 1 for player 1, 2 for player 2
        self.player_names = ["Player 1", "Player 2"]
        self.player_wins = [0, 0]  # Keep track of player wins

    def play(self, row, col):
        if self.grid[row, col] == 0:
            self.grid[row, col] = self.turn
            self.check_win()
            self.turn = 3 - self.turn

    def check_win(self):
        # Check rows
        for i in range(3):
            if np.all(self.grid[i, :] == self.turn):
                self.declare_winner(self.turn, f"row {i+1}")
                return

        # Check columns
        for j in range(3):
            if np.all(self.grid[:, j] == self.turn):
                self.declare_winner(self.turn, f"column {j+1}")
                return

        # Check diagonals
        if np.all(self.grid.diagonal() == self.turn):
            self.declare_winner(self.turn, "the main diagonal")
            return
        if np.all(np.flipud(self.grid).diagonal() == self.turn):
            self.declare_winner(self.turn, "the anti-diagonal")
            return

        # Check for draw
        if np.all(self.grid != 0):
            self.declare_draw()

    def declare_winner(self, winner, winning_combination):
        self.player_wins[winner-1] += 1
        print(f"{self.player_names[winner-1]} wins with a {winning_combination}!")

    def declare_draw(self):
        print("Draw!")

    def print_grid(self):
        grid_str = '''
        -------------
        | {} | {} | {} |
        -------------
        | {} | {} | {} |
        -------------
        | {} | {} | {} |
        -------------
        '''.format(*self.grid.flatten())
        print(grid_str)

    def get_player_input(self):
        while True:
            try:
                row = int(input(f"{self.player_names[self.turn-1]}'s turn. Enter row (0-2): "))
                col = int(input(f"{self.player_names[self.turn-1]}'s turn. Enter column (0-2): "))
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input. Please enter a valid row and column.")
                    continue
                if self.grid[row, col] != 0:
                    print("That space is already taken. Please choose another.")
                    continue
                return row, col
            except ValueError:
                print("Invalid input. Please enter integers for row and column.")

    def start_game(self):
        print("Welcome to Jdv!")
        for i in range(2):
            self.player_names[i] = input(f"Enter the name for player {i+1}: ")

        while True:
            self.print_grid()
            row, col = self.get_player_input()
            self.play(row, col)
            if self.turn == 1:
                print(f"{self.player_names[0]}'s turn")
            else:
                print(f"{self.player_names[1]}'s turn")

    def quit_game(self):
        print("Thank you for playing Jdv!")
        print(f"{self.player_names[0]}: {self.player_wins[0]} wins")
        print(f"{self.player_names[1]}: {self.player_wins[1]} wins")
        exit()

if __name__ == "__main__":
    try:
        game = Jdv()
        game.start_game()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
