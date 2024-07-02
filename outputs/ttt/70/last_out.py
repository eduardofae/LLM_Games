import numpy as np

# Constants for game parameters
BOARD_SIZE = 3
PLAYER1 = 1
PLAYER2 = 2

class Jdv:
    def __init__(self):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        self.current_player = PLAYER1
        self.winner = 0

    def play(self, row, column):
        """
        Handle a move by the current player at the specified row and column.

        Args:
            row (int): The row index of the move.
            column (int): The column index of the move.
        """

        # Check if the game is over
        if self.winner != 0:
            print("Game over!")
            return

        # Validate the input
        if not (0 <= row < BOARD_SIZE and 0 <= column < BOARD_SIZE):
            print("Invalid move. Please enter a valid row and column.")
            return
        if self.board[row, column] != 0:
            print("Space already occupied. Please choose an empty space.")
            return

        # Place the player's piece on the board
        self.board[row, column] = self.current_player

        # Display the updated game board
        print(self.board)

        # Check if the move results in a win
        if self._check_winner():
            self.winner = self.current_player
            print(f"Player {self.current_player} wins!")
        else:
            # Switch to the other player's turn
            self.current_player = 3 - self.current_player

    def _check_winner(self):
        """
        Check if the current player has won the game.

        Returns:
            True if the current player has won, False otherwise.
        """

        # Check rows
        for row in range(BOARD_SIZE):
            if np.all(self.board[row, :] == self.current_player):
                return True

        # Check columns
        for column in range(BOARD_SIZE):
            if np.all(self.board[:, column] == self.current_player):
                return True

        # Check diagonals
        if np.all(self.board.diagonal() == self.current_player):
            return True
        if np.all(np.flip(self.board).diagonal() == self.current_player):
            return True

        # Check for a draw
        if np.all(self.board != 0):
            print("Draw!")
            return True

        return False


if __name__ == "__main__":
    # Create a new game
    jdv = Jdv()

    # Welcome message
    print("Welcome to Jdv!")

    # Game loop
    while jdv.winner == 0:
        # Get the current player's move
        if jdv.current_player == PLAYER1:
            row = int(input("Player 1, enter the row: "))
            column = int(input("Player 1, enter the column: "))
        else:
            row = int(input("Player 2, enter the row: "))
            column = int(input("Player 2, enter the column: "))

        # Handle the move
        jdv.play(row, column)

    # Game over
    print("Game over!")
