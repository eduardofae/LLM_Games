import numpy as np

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((10, 10))
        self.players = ['X', 'O']
        self.current_player = 0
        self.turns = 0
        self.winner = None

    def check_winner(self):
        # Check the rows
        for row in self.board:
            if np.all(row == self.players[self.current_player]):
                return True

        # Check the columns
        for col in self.board.T:
            if np.all(col == self.players[self.current_player]):
                return True

        # Check the diagonals
        diagonals = [self.board.diagonal(), np.flip(self.board).diagonal()]
        for diagonal in diagonals:
            if np.all(diagonal == self.players[self.current_player]):
                return True

        return False

    def place_piece(self, col):
        # Check if the column is full
        if self.board[9, col] != 0:
            print("Invalid move. Try again.")
            return False

        # Find the lowest free space in the column
        row = 9
        while self.board[row, col] != 0:
            row -= 1

        # Place the piece
        self.board[row, col] = self.players[self.current_player]

        return True

    def switch_player(self):
        self.current_player = (self.current_player + 1) % 2

    def run_game(self):
        while self.winner is None and self.turns < 100:
            # Get the column from the current player
            while True:
                try:
                    col = int(input("Enter a column (0-9): "))
                    if col in range(0, 10):
                        break
                    else:
                        print("Invalid input. Please enter a number between 0 and 9.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Place the piece
            if not self.place_piece(col):
                continue

            # Check if there is a winner
            if self.check_winner():
                self.winner = self.players[self.current_player]
                break

            # Check if the board is full
            if np.all(self.board != 0):
                self.winner = "Draw"
                break

            # Switch the current player
            self.switch_player()

            # Increment the number of turns
            self.turns += 1

        # Print the winner
        if self.winner is not None:
            print(f"{self.winner} wins!")
        else:
            print("Draw!")

        # Ask if the players want to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == 'y':
            self.reset_game()
            self.run_game()

    def reset_game(self):
        self.board = np.zeros((10, 10))
        self.current_player = 0
        self.turns = 0
        self.winner = None

# Create a new instance of the game
game = ConnectFour()

# Run the game
game.run_game()
