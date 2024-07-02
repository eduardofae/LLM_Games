import numpy as np

class Pong:
    def __init__(self):
        self.board = np.zeros((10, 10), dtype=int)
        self.player_turn = 1
        self.winner = None

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
        for row in self.board:
            for cell in row:
                if cell == 0:
                    print("-", end=" ")
                elif cell == 1:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()

    def get_player_input(self):
        column = int(input("Player {}: Choose a column (1-10): ".format(self.player_turn))) - 1
        if column < 0 or column > 9:
            print("Invalid column. Please choose a column between 1 and 10.")
            return
        
        for row in range(9, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.player_turn
                self.player_turn = 3 - self.player_turn
                break

    def check_for_win(self):
        # Check for horizontal win
        for row in range(10):
            if np.all(self.board[row] == self.player_turn):
                self.winner = self.player_turn

        # Check for vertical win
        for column in range(10):
            if np.all(self.board[:, column] == self.player_turn):
                self.winner = self.player_turn

        # Check for diagonal win
        for i in range(6):
            for j in range(6):
                if np.all(self.board[i:i+3, j:j+3] == self.player_turn):
                    self.winner = self.player_turn
                if np.all(self.board[i:i+3, 9-j:9-j+3] == self.player_turn):
                    self.winner = self.player_turn

        # Check for draw
        if np.all(self.board != 0):
            self.winner = 0

if __name__ == "__main__":
    game = Pong()
    game.play()
