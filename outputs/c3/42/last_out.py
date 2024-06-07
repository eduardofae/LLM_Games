import numpy as np

class Game:
    """
    Connect Four game class.

    Attributes:
        board: A 2D numpy array representing the game board.
        players: A list of the players in the game.
        current_player: The player who is currently taking their turn.
        game_status: The current status of the game (ongoing, win, draw).
    """

    def __init__(self):
        self.board = np.zeros((6, 7), dtype=int)
        self.players = [1, 2]
        self.current_player = self.players[0]
        self.game_status = "ongoing"

    def play(self):
        """
        Play the game.

        The game continues until one player wins or the board is full.
        """

        while self.game_status == "ongoing":
            self.print_board()
            move = self.get_player_move()

            if not self.is_valid_move(move):
                print("Invalid move. Try again.")
                continue

            self.place_piece(move)

            if self.check_win():
                self.game_status = "win"
                print(f"Player {self.current_player} wins!")
            elif np.all(self.board != 0):
                self.game_status = "draw"
                print("Draw!")

            self.switch_player()

        self.print_board()

    def print_board(self):
        """
        Print the game board to the console.
        """

        for row in range(5, -1, -1):
            print("|", end="")
            for col in range(7):
                if self.board[row, col] == 0:
                    print("   |", end="")
                elif self.board[row, col] == 1:
                    print(" X |", end="")
                else:
                    print(" O |", end="")
            print()
        print("---+---+---+---+---+---+---")

    def get_player_move(self):
        """
        Get the player's move.

        The player is prompted to enter a column number (1-7).
        """

        while True:
            try:
                move = int(input(f"Player {self.current_player}, enter a column (1-7): ")) - 1
                return move
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")

    def is_valid_move(self, move):
        """
        Check if the player's move is valid.

        A move is valid if the column is not full.
        """

        return move >= 0 and move < 7 and self.board[5, move] == 0

    def place_piece(self, move):
        """
        Place the player's piece on the board.

        The piece is placed in the lowest available row in the given column.
        """

        for i in range(5, -1, -1):
            if self.board[i, move] == 0:
                self.board[i, move] = self.current_player
                break

    def check_win(self):
        """
        Check if the current player has won.

        A player wins if they have four of their pieces in a row, either horizontally, vertically, or diagonally.
        """

        # Check for horizontal win
        for i in range(6):
            if np.all(self.board[i,