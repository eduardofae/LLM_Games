import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player_turn = 1

    def play(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = self.player_turn
            self.player_turn = -self.player_turn  # Switch player turn
            return True
        else:
            return False

    def check_winner(self):
        # Check rows
        for row in range(3):
            if np.all(self.board[row, :] == self.player_turn):
                return self.player_turn

        # Check columns
        for col in range(3):
            if np.all(self.board[:, col] == self.player_turn):
                return self.player_turn

        # Check diagonals
        if np.all(self.board.diagonal() == self.player_turn):
            return self.player_turn
        if np.all(np.flip(self.board).diagonal() == self.player_turn):
            return self.player_turn

        # Check draw
        if np.all(self.board != 0):
            return 0

        # No winner or draw yet
        return None

    def print_board(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    print('_', end=' ')
                elif col == 1:
                    print('X', end=' ')
                elif col == -1:
                    print('O', end=' ')
            print()

if __name__ == '__main__':
    game = Jdv()

    while True:
        game.print_board()
        print(f"Player {game.player_turn}'s turn (row, col): ")
        row, col = map(int, input().split())

        if game.play(row, col):
            winner = game.check_winner()
            if winner is not None:
                game.print_board()
                if winner == 0:
                    print("Draw")
                else:
                    print(f"Player {winner} wins!")
                break
        else:
            print("Invalid move. Try again.")