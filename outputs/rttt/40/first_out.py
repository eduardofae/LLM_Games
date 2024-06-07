class JdvGame:
    def __init__(self):
        self.grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player_turn = 1

    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))

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
            if row[0] == row[1] == row[2] != ' ':
                return True

        # Check columns
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != ' ':
                return True

        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
            return True

        return False

    def check_draw(self):
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def play(self):
        while True:
            self.print_grid()
            row = int(input("Player {}'s turn. Enter row (0-2): ".format(self.player_turn)))
            col = int(input("Enter column (0-2): "))

            self.place_piece(row, col)

            if self.check_win():
                self.print_grid()
                print("Player {} wins!".format(3 - self.player_turn))
                break
            elif self.check_draw():
                self.print_grid()
                print("Draw!")
                break

if __name__ == "__main__":
    game = JdvGame()
    game.play()
