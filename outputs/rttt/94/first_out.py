import numpy as np

class Jdv:
    def __init__(self):
        self.grid = np.zeros((3, 3), dtype=int)
        self.player_turn = 1  # 1 for player 1, -1 for player 2

    def play(self, row, col):
        if self.grid[row, col] == 0:
            self.grid[row, col] = self.player_turn
            self.player_turn *= -1  # switch player turn
        else:
            print("Invalid move. Space already occupied.")

    def check_winner(self):
        # check rows
        for row in range(3):
            if np.sum(self.grid[row, :]) == 3 or np.sum(self.grid[row, :]) == -3:
                return True

        # check columns
        for col in range(3):
            if np.sum(self.grid[:, col]) == 3 or np.sum(self.grid[:, col]) == -3:
                return True

        # check diagonals
        if np.sum(self.grid.diagonal()) == 3 or np.sum(self.grid.diagonal()) == -3:
            return True
        if np.sum(np.flipud(self.grid).diagonal()) == 3 or np.sum(np.flipud(self.grid).diagonal()) == -3:
            return True

        # check for a draw
        if np.all(self.grid != 0):
            return True

        return False

    def print_grid(self):
        for row in self.grid:
            for col in row:
                if col == 1:
                    print("X", end=" ")
                elif col == -1:
                    print("O", end=" ")
                else:
                    print("-", end=" ")
            print()

if __name__ == "__main__":
    jdv = Jdv()

    while True:
        jdv.print_grid()

        # get player move
        row = int(input("Player {}: Enter row (0-2): ".format(1 if jdv.player_turn == 1 else 2)))
        col = int(input("Player {}: Enter column (0-2): ".format(1 if jdv.player_turn == 1 else 2)))

        # play move
        jdv.play(row, col)

        # check for winner or draw
        if jdv.check_winner():
            jdv.print_grid()
            if jdv.player_turn == 1:
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
            break
        elif jdv.check_draw():
            jdv.print_grid()
            print("Draw!")
            break
