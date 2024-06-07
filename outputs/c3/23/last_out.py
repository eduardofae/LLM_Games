import numpy as np

class Player:
    def __init__(self, piece):
        self.piece = piece
        self.wins = 0

class Board:
    def __init__(self, rows, columns):
        self.board = np.zeros((rows, columns), dtype=int)

    def place_piece(self, player, column):
        for row in range(self.board.shape[0]-1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = player.piece
                return True
        return False

    def check_for_win(self, player):
        # Check for horizontal win
        for row in range(self.board.shape[0]):
            if np.all(self.board[row] == player.piece):
                return True

        # Check for vertical win
        for column in range(self.board.shape[1]):
            if np.all(self.board[:, column] == player.piece):
                return True

        # Check for diagonal win
        for i in range(self.board.shape[0]-2):
            for j in range(self.board.shape[1]-2):
                if np.all(self.board[i:i+3, j:j+3] == player.piece):
                    return True
                if np.all(self.board[i:i+3, self.board.shape[1]-1-j:self.board.shape[1]-1-j+3] == player.piece):
                    return True

        return False

    def is_full(self):
        return np.all(self.board != 0)

class Pong:
    def __init__(self, rows, columns, win_length):
        self.board = Board(rows, columns)
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.current_player = self.player1
        self.winner = None
        self.win_length = win_length

    def play(self):
        while self.winner is None:
            self.print_board()
            self.get_player_input()
            self.check_for_win()

        self.print_board()
        if self.winner == 0:
            print("Draw")
        else:
            print("Player {} wins".format(self.winner))

    def print_board(self):
        for row in self.board.board:
            for cell in row:
                if cell == 0:
                    print("-", end=" ")
                elif cell == 1:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()

    def get_player_input(self):
        try:
            column = int(input("Player {}: Choose a column (1-{}): ".format(self.current_player.piece, self.board.board.shape[1]))) - 1
            if column < 0 or column > self.board.board.shape[1]-1:
                raise ValueError("Invalid column number")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and {}.".format(self.board.board.shape[1]))
            return

        if not self.board.place_piece(self.current_player, column):
            print("Invalid move. Please choose another column.")
            return

        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def check_for_win(self):
        if self.board.check_for_win(self.current_player):
            self.winner = self.current_player.piece
        elif self.board.is_full():
            self.winner = 0

    def reset_game(self):
        self.board = Board(self.board.board.shape[0], self.board.board.shape[1])
        self.player1.wins = 0
        self.player2.wins = 0
        self.current_player = self.player1
        self.winner = None

if __name__ == "__main__":
    while True:
        rows = int(input("Enter the number of rows (minimum 3): "))
        columns = int(input("Enter the number of columns (minimum 3): "))
        win_length = int(input("Enter the length of the winning line (minimum 3): "))
        if rows < 3 or columns < 3 or win_length < 3:
            print("Invalid input. Please enter values greater than or equal to 3.")
            continue

        game = Pong(rows, columns, win_length)
        game.play()
        if input("Play again (y/n)? ") == "n":
            break
        game.reset_game()
