import sys

class Jdv:
    def __init__(self):
        """
        Initializes the game board and player information.
        """
        self.board = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]
        self.player1 = 'X'
        self.player2 = 'O'
        self.current_player = self.player1

    def play(self):
        """
        Runs the main game loop.
        """
        while True:
            # Get the current player's move.
            try:
                move = input("%s, enter your move (row, column): " % self.current_player)
                row, column = map(int, move.split(','))
                row -= 1
                column -= 1
            except ValueError:
                print("Invalid move. Please try again.")
                continue

            # Check if the move is valid.
            if not (0 <= row < 3 and 0 <= column < 3):
                print("Invalid move. Please try again.")
                continue

            # Check if the space is already occupied.
            if self.board[row][column] != ' ':
                print("Space already occupied. Please try again.")
                continue

            # Place the player's piece in the grid.
            self.board[row][column] = self.current_player

            # Check if the player has won.
            if self.check_win():
                print("%s wins!" % self.current_player)
                return

            # Check if the game is a draw.
            if self.check_draw():
                print("The game is a draw.")
                return

            # Switch turns.
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def check_win(self):
        """
        Checks if the current player has won.

        Returns:
            True if the current player has won, False otherwise.
        """

        # Check for horizontal wins.
        for row in self.board:
            if row[0] != ' ' and row[0] == row[1] == row[2]:
                return True

        # Check for vertical wins.
        for column in range(3):
            if self.board[0][column] != ' ' and self.board[0][column] == self.board[1][column] == self.board[2][column]:
                return True

        # Check for diagonal wins.
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True

        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True

        # No winner yet.
        return False

    def check_draw(self):
        """
        Checks if the game is a draw.

        Returns:
            True if the game is a draw, False otherwise.
        """

        # Check if there are any empty spaces.
        for row in self.board:
            for space in row:
                if space == ' ':
                    return False

        # No empty spaces, so the game is a draw.
        return True


if __name__ == "__main__":
    jdv = Jdv()
    jdv.play()
