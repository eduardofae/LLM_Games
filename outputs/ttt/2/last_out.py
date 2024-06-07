import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player_turn = 1

    def play(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row, col] == 0:
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

    def restart_game(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player_turn = 1

    def get_score(self):
        player1_score = 0
        player2_score = 0

        # Check rows
        for row in range(3):
            if np.all(self.board[row, :] == 1):
                player1_score += 1
            elif np.all(self.board[row, :] == -1):
                player2_score += 1

        # Check columns
        for col in range(3):
            if np.all(self.board[:, col] == 1):
                player1_score += 1
            elif np.all(self.board[:, col] == -1):
                player2_score += 1

        # Check diagonals
        if np.all(self.board.diagonal() == 1):
            player1_score += 1
        elif np.all(self.board.diagonal() == -1):
            player2_score += 1
        if np.all(np.flip(self.board).diagonal() == 1):
            player1_score += 1
        elif np.all(np.flip(self.board).diagonal() == -1):
            player2_score += 1

        return player1_score, player2_score


class UserInterface:
    def __init__(self, game):
        self.game = game

    def start(self):
        while True:
            self.game.print_board()
            print(f"Player {self.game.player_turn}'s turn (row, col): ")
            try:
                row, col = map(int, input().split())
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
                continue

            if self.game.play(row, col):
                winner = self.game.check_winner()
                if winner is not None:
                    self.game.print_board()
                    if winner == 0:
                        print("Draw")
                    else:
                        print(f"Player {winner} wins!")
                    player1_score, player2_score = self.game.get_score()
                    print(f"Player 1 score: {player1_score}")
                    print(f"Player 2 score: {player2_score}")
                    play_again = input("Play again? (y/n): ")
                    if play_again == 'y':
                        self.game.restart_game()
                    else:
                        break
            else:
                print("Invalid move. Try again.")


if __name__ == '__main__':
    game = Jdv()
    ui = UserInterface(game)
    ui.start()