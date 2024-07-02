import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player_turn = 1

    def play(self, row, col):
        # Check if the move is valid
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError("Invalid move: The space is outside the board.")
        if self.board[row, col] != 0:
            raise ValueError("Invalid move: The space is already occupied.")

        # Place the player's piece on the board
        self.board[row, col] = self.player_turn

        # Check if the player has won
        if self._check_win(self.player_turn):
            return self.player_turn

        # Switch to the other player's turn
        self.player_turn *= -1

        # Check if the game is a draw
        if np.all(self.board != 0):
            return 0

        return None

    def _check_win(self, player):
        # Check rows
        for row in range(3):
            if np.all(self.board[row, :] == player):
                return True

        # Check columns
        for col in range(3):
            if np.all(self.board[:, col] == player):
                return True

        # Check diagonals
        if np.all(self.board.diagonal() == player):
            return True
        if np.all(np.flip(self.board).diagonal() == player):
            return True

        return False

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.board])

if __name__ == "__main__":
    game = Jdv()

    while True:
        # Get the player's move
        print(game)
        print(f"Player {game.player_turn}'s turn")
        try:
            row, col = map(int, input("Enter the row and column (e.g. 0 0): ").split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue

        # Play the move
        result = game.play(row, col)

        # Check if the game is over
        if result is not None:
            if result == 0:
                print("Draw")
            else:
                print(f"Player {result} wins!")
            break
