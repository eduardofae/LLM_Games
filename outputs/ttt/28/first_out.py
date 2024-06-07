class Jdv:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player = 1

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]

        # Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != ' ':
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]

        # Check draw
        if all(all(row) for row in self.board):
            return 'Draw'

        return None

    def play(self):
        while True:
            self.print_board()
            print(f"Player {self.player}'s turn")

            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if self.board[row][col] == ' ':
                if self.player == 1:
                    self.board[row][col] = 'X'
                else:
                    self.board[row][col] = 'O'
                self.player = 3 - self.player

            else:
                print("Invalid move, try again")

            winner = self.check_win()
            if winner:
                self.print_board()
                print(f"Player {winner} wins!")
                break


if __name__ == "__main__":
    game = Jdv()
    game.play()
