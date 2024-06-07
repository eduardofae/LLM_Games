import numpy as np

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((6, 7), dtype=int)
        self.current_player = 1
        self.game_over = False
        self.draw = False

    def play(self):
        while not self.game_over:
            # Get the player's move
            try:
                column = int(input("Player {}'s turn. Choose a column (1-7): ".format(self.current_player))) - 1
            except ValueError:
                print("Invalid input. Please choose a column between 1 and 7.")
                continue

            # Check if the column is valid
            if column < 0 or column > 6:
                print("Invalid column. Please choose a column between 1 and 7.")
                continue

            # Check if the column is full
            if self.is_column_full(column):
                print("Column is full. Please choose another column.")
                continue

            # Drop the piece into the column
            row = self.get_next_open_row(column)
            self.board[row, column] = self.current_player

            # Check if the player has won
            if self.check_win(self.current_player):
                self.game_over = True
                print("Player {} wins!".format(self.current_player))
                break

            # Check if the game is a draw
            if self.is_draw():
                self.game_over = True
                self.draw = True
                print("Draw!")
                break

            # Switch the current player
            self.current_player *= -1

        # Print the final board
        self.print_board()

    def check_win(self, player):
        # Check for horizontal wins
        for row in range(6):
            for col in range(4):
                if self.board[row, col] == player and self.board[row, col + 1] == player and self.board[row, col + 2] == player and self.board[row, col + 3] == player:
                    return True

        # Check for vertical wins
        for row in range(3):
            for col in range(7):
                if self.board[row, col] == player and self.board[row + 1, col] == player and self.board[row + 2, col] == player and self.board[row + 3, col] == player:
                    return True

        # Check for diagonal wins
        for row in range(3):
            for col in range(4):
                if self.board[row, col] == player and self.board[row + 1, col + 1] == player and self.board[row + 2, col + 2] == player and self.board[row + 3, col + 3] == player:
                    return True
                if self.board[row + 3, col] == player and self.board[row + 2, col + 1] == player and self.board[row + 1, col + 2] == player and self.board[row, col + 3] == player:
                    return True

        # No win found
        return False

    def is_column_full(self, column):
        return self.board[0, column] != 0

    def get_next_open_row(self, column):
        for row in range(5, -1, -1):
            if self.board[row, column] == 0:
                return row

    def is_draw(self):
        return np.all(self.board != 0)

    def print_board(self):
        print(self.board)

if __name__ == "__main__":
    game = ConnectFour()
    game.play()
