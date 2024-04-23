class JdvGame:
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]
        self.players = ['X', 'O']
        self.current_player = 0
        self.winner = None

    def print_board(self):
        for row in self.board:
            print('|'.join(row))

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_move_valid(self, row, column):
        return row >= 0 and row < 3 and column >= 0 and column < 3 and self.board[row][column] == ' '

    def play_game(self):
        while self.winner is None:
            self.print_board()

            move = input(f"Player {self.players[self.current_player]}, enter your move (row, column): ")

            try:
                row, column = [int(x) for x in move.split(',')]

                if not self.is_move_valid(row, column):
                    raise ValueError("Invalid move. Please try again.")

            except ValueError:
                print("Invalid input. Please try again.")
                continue

            self.board[row][column] = self.players[self.current_player]

            self.winner = self.check_winner()

            if self.winner is None:
                self.current_player = (self.current_player + 1) % 2

        if self.winner is not None:
            self.print_board()
            print(f"Player {self.winner} wins!")
        else:
            self.print_board()
            print("Draw!")


if __name__ == "__main__":
    game = JdvGame()
    game.play_game()