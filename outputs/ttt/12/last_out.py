import numpy as np

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        """Gets the player's input for the next move."""
        while True:
            try:
                selected_row, selected_column = map(int, input(f"Player {self.symbol}, enter row and column (e.g. 1 2): ").split())
                if selected_row < 1 or selected_row > board.size or selected_column < 1 or selected_column > board.size:
                    print("Invalid input. Row and column must be between 1 and 3.")
                elif board.get_cell(selected_row-1, selected_column-1) != '':
                    print("That space is already occupied.")
                else:
                    return selected_row-1, selected_column-1
            except (ValueError, IndexError):
                print("Invalid input. Please enter two integers separated by a space.")

class Board:
    def __init__(self, size):
        self.size = size
        self.board = np.empty((size, size), dtype=str)
        self.board[:] = ''

    def print_board(self):
        """Prints the board to the console."""
        for row in self.board:
            for cell in row:
                print(cell, end=' ')
            print()

    def get_cell(self, row, column):
        """Gets the value of the cell at the given row and column."""
        return self.board[row][column]

    def set_cell(self, row, column, value):
        """Sets the value of the cell at the given row and column."""
        self.board[row][column] = value

    def check_winner(self):
        """Checks if there is a winner."""
        # Check rows
        for row in self.board:
            if len(set(row)) == 1 and row[0] != '':
                return row[0]

        # Check columns
        for col in range(self.size):
            if len(set(self.board[:, col])) == 1 and self.board[0][col] != '':
                return self.board[0][col]

        # Check diagonals
        if len(set([self.board[i][i] for i in range(self.size)])) == 1 and self.board[0][0] != '':
            return self.board[0][0]
        if len(set([self.board[i][self.size-i-1] for i in range(self.size)])) == 1 and self.board[0][self.size-1] != '':
            return self.board[0][self.size-1]

        # Check draw
        if np.all(self.board != ''):
            return 'draw'

        # No winner yet
        return None

class GameState:
    def __init__(self):
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.board = Board(3)
        self.current_player = self.player1
        self.game_over = False

    def play_game(self):
        """Plays the jdv game."""
        while not self.game_over:
            self.board.print_board()
            try:
                selected_row, selected_column = self.current_player.get_move(self.board)
                self.board.set_cell(selected_row, selected_column, self.current_player.symbol)
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")
                continue

            winner = self.board.check_winner()
            if winner:
                if winner == 'draw':
                    print("It's a draw!")
                else:
                    print(f"Player {winner} wins!")
                self.game_over = True
            else:
                self.current_player = self.player2 if self.current_player == self.player1 else self.player1

# Play the game
game = GameState()
game.play_game()
