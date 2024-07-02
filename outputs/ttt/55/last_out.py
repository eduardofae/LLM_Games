import numpy as np

class JdvGame:

    def __init__(self):
        self.game_board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 for X, 2 for O
        self.winner = 0  # 0 for no winner, 1 for X, 2 for O
        self.num_moves = 0

    def check_win(self):
        # Check for rows
        for i in range(3):
            if np.all(self.game_board[i] == self.game_board[i][0]) and self.game_board[i][0] != 0:
                return True

        # Check for columns
        for j in range(3):
            if np.all(self.game_board[:, j] == self.game_board[0, j]) and self.game_board[0, j] != 0:
                return True

        # Check for diagonals
        if np.all(np.diag(self.game_board) == self.game_board[0, 0]) and self.game_board[0, 0] != 0:
            return True

        if np.all(np.diag(np.flipud(self.game_board)) == self.game_board[0, 2]) and self.game_board[0, 2] != 0:
            return True

        return False

    def print_board(self):
        for i in range(3):
            for j in range(3):
                if self.game_board[i, j] == 0:
                    print(" ", end=" ")
                elif self.game_board[i, j] == 1:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()

    def get_move(self):
        while True:
            print("Player", self.current_player, "turn:")
            move = input("Enter row and column (e.g. 1 2): ")
            try:
                row, col = map(int, move.split())
                if row < 1 or row > 3 or col < 1 or col > 3:
                    print("Invalid move. Please enter a valid row and column.")
                    continue
                if self.game_board[row - 1, col - 1] != 0:
                    print("That space is already taken. Please enter a valid move.")
                    continue
                return row - 1, col - 1
            except ValueError:
                print("Invalid move. Please enter a valid row and column.")

    def play(self):
        while self.winner == 0 and self.num_moves < 9:
            # Get the player's move
            row, col = self.get_move()

            # Place the player's piece on the board
            self.game_board[row, col] = self.current_player

            # Check if the player has won
            if self.check_win():
                print("Player", self.current_player, "wins!")
                break

            # Increment the number of moves
            self.num_moves += 1

            # Switch players
            self.current_player = 3 - self.current_player

            # Print the game board
            self.print_board()

        # Check if the game is a draw
        if self.num_moves == 9 and self.winner == 0:
            print("Draw!")

    def play_against_computer(self):
        while self.winner == 0 and self.num_moves < 9:
            # Get the player's move
            row, col = self.get_move()

            # Place the player's piece on the board
            self.game_board[row, col] = self.current_player

            # Check if the player has won
            if self.check_win():
                print("Player", self.current_player, "wins!")
                break

            # Increment the number of moves
            self.num_moves += 1

            # Get the computer's move
            row, col = self.get_computer_move()

            # Place the computer's piece on the board
            self.game_board[row, col] = 3 - self.current_player

            # Check if the computer has won
            if self.check_win():
                print("Computer wins!")
                break

            # Increment the number of moves
            self.num_moves += 1

            # Print the game board
            self.print_board()

        # Check if the game is a draw
        if self.num_moves == 9 and self.winner == 0:
            print("Draw!")

    def get_computer_move(self):
        # Implement a simple AI algorithm to choose the computer's move.
        # For example, the computer could choose the first available space in a row, column, or diagonal that would result in a win.
        pass

if __name__ == "__main__":
    game = JdvGame()
    game.play()
