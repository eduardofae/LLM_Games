import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.current_player = 1
        self.opponent = None
        self.difficulty = None
        self.winner = None
        self.win_loss_record = {1: 0, 2: 0, "Draw": 0}

    def play(self):
        # Get the user's choice of opponent
        self.opponent = input("Do you want to play against the computer or another human? (c/h) ")

        # Get the user's choice of difficulty level
        if self.opponent == "c":
            self.difficulty = input("Choose a difficulty level (easy/medium/hard): ")

        # Get the user's choice of board size
        self.board_size = int(input("Choose a board size (3-5): "))

        # Get the user's choice of starting player
        self.starting_player = int(input("Choose the starting player (1 or 2): "))

        # Set the current player to the starting player
        self.current_player = self.starting_player

        # Loop until the game is over
        while True:
            # Get the player's move
            if self.current_player == 1:
                move = input("Player {}'s turn: ".format(self.current_player))
            elif self.opponent == "c" and self.current_player == 2:
                move = self.get_computer_move()
            else:
                move = input("Player {}'s turn: ".format(self.current_player))

            # Convert the move to a row and column
            try:
                row, col = [int(x) for x in move.split(",")]
            except ValueError:
                print("Invalid move. Please try again.")
                continue

            # Check if the move is valid
            if self.board[row, col] != 0:
                print("Invalid move. Please try again.")
                continue

            # Place the player's piece on the board
            self.board[row, col] = self.current_player

            # Check if the player has won
            if self.check_win(self.current_player):
                self.winner = self.current_player
                print("Player {} wins!".format(self.current_player))
                self.win_loss_record[self.winner] += 1
                break

            # Check if the game is a draw
            if np.all(self.board != 0):
                self.winner = "Draw"
                print("Draw!")
                self.win_loss_record["Draw"] += 1
                break

            # Switch to the other player
            self.current_player = 3 - self.current_player

    def get_computer_move(self):
        """
        Gets the computer's move.

        Returns:
            The computer's move as a row and column.
        """

        # Create a minimax object
        minimax = Minimax(self.board, self.difficulty)

        # Get the computer's move
        move = minimax.get_move()

        # Return the move as a row and column
        return move[0], move[1]

    def check_win(self, player):
        """
        Checks if the given player has won the game.

        Args:
            player: The player to check for a win.

        Returns:
            True if the player has won, False otherwise.
        """

        # Check for a win in each row
        for row in range(self.board_size):
            if np.all(self.board[row, :] == player):
                return True

        # Check for a win in each column
        for col in range(self.board_size):
            if np.all(self.board[:, col] == player):
                return True

        # Check for a win in each diagonal
        if np.all(self.board.diagonal() == player) or np.all(np.flip(self.board).diagonal() == player):
            return True

        # No win found
        return False

    def print_board(self):
        """
        Prints the current state of the game board.
        """

        for row in self.board:
            for col in row:
                if col == 0:
                    print(" ", end=" ")
                elif col == 1:
                    print("X", end=" ")
                elif col == 2:
                    print("O", end=" ")
            print()

    def restart(self):
        """
        Restarts the game.
        """

        self.board = np.zeros((self.board_size, self.board_size))
        self.current_player = self.starting_player
        self.winner = None

    def save(self):
        """
        Saves the game to a file.
        """

        with open("game.dat", "wb") as f:
            np.save(f, self.board)
            np.save(f, self.current_player)
            np.save(f, self.winner)

    def load(self):
        """
        Loads the game from a file.
        """

        with open("game.dat", "rb") as f:
            self.board = np.load(f)
            self.current_player = np.load(f)
            self.winner = np.load(f)

if __name__ == "__main__":
    jdv = Jdv()
    jdv.play()
