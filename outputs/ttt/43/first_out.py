import numpy as np

class jdv:
    def __init__(self):
        self.board = np.zeros((3,3))
        self.player = 1
        self.winner = 0
        self.draw = False

    def play(self, row, col):
        if self.board[row, col] == 0 and not self.winner and not self.draw:
            self.board[row, col] = self.player
            self.check_winner()
            self.check_draw()
            self.player *= -1

    def check_winner(self):
        for i in range(3):
            if np.all(self.board[i, :] == self.player) or np.all(self.board[:, i] == self.player):
                self.winner = self.player
                return
        if np.all(self.board.diagonal() == self.player) or np.all(np.flip(self.board).diagonal() == self.player):
            self.winner = self.player

    def check_draw(self):
        if np.all(self.board != 0):
            self.draw = True

    def print_board(self):
        print(self.board)

    def get_winner(self):
        return self.winner

    def get_draw(self):
        return self.draw

def main():
    game = jdv()
    while not game.get_winner() and not game.get_draw():
        game.print_board()
        row, col = map(int, input("Enter row and column: ").split())
        game.play(row, col)
    if game.get_winner():
        print("Player", game.get_winner(), "wins!")
    else:
        print("Draw")

if __name__ == "__main__":
    main()
