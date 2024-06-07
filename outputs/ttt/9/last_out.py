import numpy as np

class TicTacToe:
    """
    A simple implementation of the game TicTacToe in Python.

    Attributes:
        grid: A 3x3 numpy array representing the game board.
        player: The current player's turn (1 or 2).
        moves: The number of moves made so far.

    Methods:
        play(): Starts the game.
        get_move(): Gets the player's move.
        place_piece(): Places the player's piece on the board.
        check_win(): Checks if the player has won.
        check_draw(): Checks if the game is a draw.
        reset(): Resets the game.
        display_board(): Displays the game board to the user.
    """

    def __init__(self):
        """
        Initializes the game.
        """

        self.grid = np.zeros((3, 3), dtype=int)
        self.player = 1
        self.moves = 0

    def play(self):
        """
        Starts the game.
        """

        while True:
            # Display the game board
            self.display_board()

            # Get the player's move
            row, col = self.get_move()

            # Check if the move is valid
            if self.grid[row, col] != 0:
                print("Invalid move. Please try again.")
                continue

            # Place the player's piece on the board
            self.place_piece(row, col)

            # Increment the number of moves made
            self.moves += 1

            # Check if the player has won
            if self.check_win():
                print(f"Player {self.player} wins!")
                break

            # Check if the game is a draw
            if self.check_draw():
                print("Draw!")
                break

            # Switch to the other player
            self.player = 3 - self.player

    def get_move(self):
        """
        Gets the player's move.

        Returns:
            A tuple of the row and column of the player's move.
        """

        while True:
            try:
                row, col = map(int, input("Enter your move (row, column): ").split())

                # Check if the row and column are within the bounds of the board
                if 0 <= row < 3 and 0 <= col < 3:
                    return row, col

                else:
                    print("Invalid move. Please try again.")

            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

    def place_piece(self, row, col):
        """
        Places the player's piece on the board.

        Args:
            row: The row of the player's move.
            col: The column of the player's move.
        """

        self.grid[row, col] = self.player

    def check_win(self):
        """
        Checks if the player has won.

        Returns:
            True if the player has won, False otherwise.
        """

        # Check rows
        for row in range(3):
            if np.all(self.grid[row, :] == self.player):
                return True

        # Check columns
        for col in range(3):
            if np.all(self.grid[:, col] == self.player):
                return True

        # Check diagonals
        if np.all(np.diag(self.grid) == self.player):
            return True

        if np.all(np.diag(np.flip(self.grid)) == self.player):
            return True

        # No win yet
        return False

    def check_draw(self):
        """
        Checks if the game is a draw.

        Returns:
            True if the game is a draw, False otherwise.
        """

        return self.moves == 9

    def reset(self):
        """
        Resets the game.
        """

        self.grid = np.zeros((3, 3), dtype=int)
        self.player = 1
        self.moves = 0

    def display_board(self):
        """
        Displays the game board to the user.
        """

        for row in range(3):
            for col in range(3):
                if self.grid[row, col] == 0:
                    print(" ", end=" ")
                elif self.grid[row, col] == 1:
                    print("X", end=" ")
                else:
                    print("O", end=" ")

            print()


# Start the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
