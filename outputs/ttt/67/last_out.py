import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 for player 1, -1 for player 2
        self.winner = None

    def play(self, row, col):
        """
        Place a piece on the board at the specified row and column.

        Args:
            row: The row index (0-based).
            col: The column index (0-based).
        """

        if self.winner is not None:
            print(f"Game over. Player {self.winner} wins!")
            return

        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid move. Please enter a valid row and column.")
            return

        if self.board[row, col] != 0:
            print("Invalid move. The cell is already occupied.")
            return

        self.board[row, col] = self.current_player
        self.check_winner(row, col)
        self.current_player *= -1

    def check_winner(self, row, col):
        """
        Check if there is a winner.

        Args:
            row: The row index of the last played move.
            col: The column index of the last played move.
        """

        # Check row
        if np.all(self.board[row, :] == self.current_player):
            self.winner = self.current_player
            return

        # Check column
        if np.all(self.board[:, col] == self.current_player):
            self.winner = self.current_player
            return

        # Check diagonals
        if row == col and np.all(self.board.diagonal() == self.current_player):
            self.winner = self.current_player
            return

        if row + col == 2 and np.all(np.flip(self.board).diagonal() == self.current_player):
            self.winner = self.current_player
            return

    def check_draw(self):
        """
        Check if the game is a draw.

        Returns:
            True if the game is a draw, otherwise False.
        """

        return np.all(self.board != 0)

    def print_board(self):
        """
        Print the game board.
        """

        for row in self.board:
            print(' '.join(['X' if x == 1 else 'O' if x == -1 else ' ' for x in row]))


def main():
    game = Jdv()

    while True:
        game.print_board()

        if game.winner is not None:
            print(f"Game over. Player {game.winner} wins!")
            break

        if game.check_draw():
            print("Draw!")
            break

        current_player = "Player 1" if game.current_player == 1 else "Player 2"
        row, col = map(int, input(f"{current_player}'s turn. Enter row and column (0-2): ").split())
        game.play(row, col)


if __name__ == "__main__":
    main()
