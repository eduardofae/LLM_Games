import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3,3),dtype=int)
        self.player = 1

    def play(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = self.player
            self.player *= -1
        else:
            raise ValueError("Invalid move!")

    def check_winner(self):
        # Check rows
        for row in range(3):
            if np.all(self.board[row,:] == self.player):
                return self.player

        # Check columns
        for col in range(3):
            if np.all(self.board[:,col] == self.player):
                return self.player

        # Check diagonals
        if np.all(np.diag(self.board) == self.player):
            return self.player
        if np.all(np.diag(np.flipud(self.board)) == self.player):
            return self.player

        # Check draw
        if np.all(self.board != 0):
            return 0

        # No winner yet
        return None

    def print_board(self):
        print(self.board)

def main():
    game = Jdv()
    game.print_board()

    while True:
        try:
            # Get player input
            row, col = map(int, input("Enter row and column (0-2): ").split())

            # Play the move
            game.play(row, col)

            # Check winner
            winner = game.check_winner()

            # Print board
            game.print_board()

            # Check game over
            if winner != None:
                if winner == 0:
                    print("Draw!")
                else:
                    print("Player", winner, "wins!")
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
