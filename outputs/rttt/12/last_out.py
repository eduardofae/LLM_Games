import numpy as np

# Define constants
GAME_STATUS_ONGOING = 'ongoing'
GAME_STATUS_OVER = 'over'
GAME_STATUS_DRAW = 'draw'

PLAYER1_SYMBOL = 'X'
PLAYER2_SYMBOL = 'O'

# Define the winning combinations
WINNING_COMBINATIONS = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


class JdvGame:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.current_player = PLAYER1_SYMBOL
        self.game_status = GAME_STATUS_ONGOING

    def play(self):
        while self.game_status == GAME_STATUS_ONGOING:
            # Get the player's input
            try:
                row = int(input(f"{self.current_player}'s turn. Enter the row (0-2): "))
                column = int(input(f"{self.current_player}'s turn. Enter the column (0-2): "))
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 2.")
                continue

            # Check if the input is valid
            if not self._is_valid_move(row, column):
                print("Invalid move. Please try again.")
                continue

            # Place the player's piece on the board
            self.board[row, column] = self.current_player

            # Print the game board
            self._print_board()

            # Check if the player has won
            if self._check_for_win(row, column):
                self.game_status = GAME_STATUS_OVER
                self.winner = self.current_player
                break

            # Check if the game is a draw
            if np.all(self.board != 0) and self.game_status == GAME_STATUS_ONGOING:
                self.game_status = GAME_STATUS_DRAW

            # Switch the current player
            self.current_player = PLAYER1_SYMBOL if self.current_player == PLAYER2_SYMBOL else PLAYER2_SYMBOL

        # Print the game status
        if self.game_status == GAME_STATUS_OVER:
            print(f"The winner is {self.winner}")
        elif self.game_status == GAME_STATUS_DRAW:
            print("The game is a draw.")

    def _is_valid_move(self, row, column):
        return 0 <= row < 3 and 0 <= column < 3 and self.board[row, column] == 0

    def _check_for_win(self, row, column):
        for combination in WINNING_COMBINATIONS:
            if all(self.board[r, c] == self.current_player for r, c in combination):
                return True
        return False

    def _print_board(self):
        for row in self.board:
            print(' '.join([str(cell) for cell in row]))
        print()


if __name__ == "__main__":
    game = JdvGame()
    game.play()
