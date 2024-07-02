import tkinter as tk
import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.player = 1
        self.size = 3

    def move(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = self.player
            self.player *= -1  # Switch player

    def check_winner(self):
        # Check rows
        for i in range(self.size):
            if np.all(self.board[i, :] == self.player):
                return self.player

        # Check columns
        for i in range(self.size):
            if np.all(self.board[:, i] == self.player):
                return self.player

        # Check diagonals
        if np.all(self.board.diagonal() == self.player) or np.all(np.flip(self.board).diagonal() == self.player):
            return self.player

        # Check for draw
        if np.all(self.board != 0):
            return 0

        return None

    def play(self):
        while True:
            # Get player move
            row, col = self.get_player_move()

            # Check if move is valid
            if row < 0 or row > self.size-1 or col < 0 or col > self.size-1:
                print("Invalid move. Please enter a valid row and column.")
                continue

            # Make move
            self.move(row, col)

            # Check for winner or draw
            winner = self.check_winner()
            if winner is not None:
                if winner == 0:
                    print("Draw")
                else:
                    print(f"Player {winner} wins")
                break

            # Print board
            self.print_board()

    def get_player_move(self):
        # Get row and column from the player
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        # Return the row and column
        return row, col

    def print_board(self):
        # Print the board
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row, col] == 0:
                    print(" ", end=" ")
                elif self.board[row, col] == 1:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()


# Create a Jdv object
jdv = Jdv()

# Play the game
jdv.play()
