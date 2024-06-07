import sys

class Game:
    def __init__(self, board_size=3):
        """
        Initialize a new game of jdv.

        Args:
            board_size (int): The size of the game board.
        """
        self.board_size = board_size
        self.game_board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.players = ['X', 'O']
        self.current_player = 0
        self.num_moves = 0

    def reset_game(self):
        """
        Reset the game to its initial state.
        """
        self.game_board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 0
        self.num_moves = 0

    def get_num_moves(self):
        """
        Get the number of moves that have been made in the game.

        Returns:
            int: The number of moves that have been made.
        """
        return self.num_moves

    def set_board_size(self, board_size):
        """
        Set the size of the game board.

        Args:
            board_size (int): The size of the game board.

        Raises:
            ValueError: If the board size is less than 3 or greater than 10.
        """
        if board_size < 3 or board_size > 10:
            raise ValueError("Invalid board size. Board size must be between 3 and 10.")

        self.board_size = board_size
        self.game_board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

    def print_game_board(self):
        """
        Print the game board to the console.
        """
        for row in self.game_board:
            print(' '.join(row))

    def get_player_move(self):
        """
        Get the player's move.

        Returns:
            tuple: A tuple containing the row and column of the player's move.
        """
        try:
            row = int(input("Enter the row (1-{}): ".format(self.board_size))) - 1
            column = int(input("Enter the column (1-{}): ".format(self.board_size))) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and {}.".format(self.board_size))
            return self.get_player_move()

        return row, column

    def is_valid_move(self, row, column):
        """
        Check if the player's move is valid.

        Args:
            row (int): The row of the player's move.
            column (int): The column of the player's move.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return row >= 0 and row < self.board_size and column >= 0 and column < self.board_size and self.game_board[row][column] == ' '

    def make_move(self, row, column):
        """
        Make the player's move.

        Args:
            row (int): The row of the player's move.
            column (int): The column of the player's move.
        """
        self.game_board[row][column] = self.players[self.current_player]
        self.num_moves += 1

    def check_win(self):
        """
        Check if the current player has won the game.

        Returns:
            bool: True if the current player has won, False otherwise.
        """
        # Check the rows
        for row in self.game_board:
            if all(x == self.players[self.current_player] for x in row):
                return True

        # Check the columns
        for column in range(self.board_size):
            if all(self.game_board[row][column] == self.players[self.current_player] for row in range(self.board_size)):
                return True

        # Check the diagonals
        if self.game_board[0][0] == self.players[self.current_player] and self.game_board[1][1] == self.players[self.current_player] and self.game_board[2][2] == self.players[self.current_player]:
            return True
        if self.game_board[0][2] == self.players[self.current_player] and self.game_board[1][1] == self.players[self.current_player] and self.game_board[2][0] == self.players[self.current_player]:
            return True

        # No win yet
        return False

    def check_draw(self):
        """
        Check if the game is a draw.

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        # Check if there are any empty spaces
        for row in self.game_board:
            for column in row:
                if column == ' ':
                    return False

        # No empty spaces, so the game is a draw
        return True

    def play_game(self):
        """
        Play a game of jdv.
        """
        while True:
            # Print the game board
            self.print_game_board()

            # Get the current player's move
            row, column = self.get_player_move()

            # Check if the move is valid
            if not self.is_valid_move(row, column):
                print("Invalid move. Please try again.")
                continue

            # Make the move
            self.make_move(row, column)

            # Check if the player has won
            if self.check_win():
                print(f"{self.players[self.current_player]} wins!")
                break

            # Check if the game is a draw
            if self.check_draw():
                print("Draw!")
                break

            # Switch to the other player
            self.current_player = (self.current_player + 1) % 2

if __name__ == "__main__":
    game = Game()
    game.play_game()
