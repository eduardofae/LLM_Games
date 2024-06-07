import numpy as np

class ConnectFour:
    def __init__(self):
        # Create a 10x10 grid
        self.grid = np.zeros((10, 10), dtype=int)

        # Define the players' symbols
        self.player1_symbol = 'X'
        self.player2_symbol = 'O'

        # Define the current player
        self.current_player = 1

        # Define the winning combinations
        self.winning_combinations = [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15), (0, 5, 10, 15), (3, 6, 9, 12)]

    def play(self):
        while True:
            # Print the grid
            print(self.grid)

            # Get the player's input
            try:
                column = int(input("Player {}'s turn. Choose a column (1-10): ".format(self.current_player))) - 1
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")
                continue

            # Check if the column is valid
            if column < 0 or column > 9:
                print("Invalid column. Please choose a column between 1 and 10.")
                continue

            # Check if the column is full
            if self.grid[:, column].sum() == 10:
                print("Column is full. Please choose another column.")
                continue

            # Place the player's piece in the lowest free space of the column
            row = 9 - self.grid[:, column].sum()
            self.grid[row, column] = self.current_player

            # Check if the player has won
            if self.check_win(row, column):
                print("Player {} wins!".format(self.current_player))
                break

            # Check if there are no more free spaces
            if np.all(self.grid.sum(axis=0) == 10):
                print("Draw!")
                break

            # Switch to the other player
            self.current_player = 3 - self.current_player

    def check_win(self, row, column):
        # Get the coordinates of the player's piece
        coordinates = [(row, column)]

        # Check for a horizontal win
        for i in range(1, 4):
            if column - i >= 0 and self.grid[row, column - i] == self.current_player:
                coordinates.append((row, column - i))
            if column + i < 10 and self.grid[row, column + i] == self.current_player:
                coordinates.append((row, column + i))

        # Check for a vertical win
        for i in range(1, 4):
            if row - i >= 0 and self.grid[row - i, column] == self.current_player:
                coordinates.append((row - i, column))
            if row + i < 10 and self.grid[row + i, column] == self.current_player:
                coordinates.append((row + i, column))

        # Check for a diagonal win
        for i in range(1, 4):
            if row - i >= 0 and column - i >= 0 and self.grid[row - i, column - i] == self.current_player:
                coordinates.append((row - i, column - i))
            if row + i < 10 and column + i < 10 and self.grid[row + i, column + i] == self.current_player:
                coordinates.append((row + i, column + i))
            if row - i >= 0 and column + i < 10 and self.grid[row - i, column + i] == self.current_player:
                coordinates.append((row - i, column + i))
            if row + i < 10 and column - i >= 0 and self.grid[row + i, column - i] == self.current_player:
                coordinates.append((row + i, column - i))

        # Check if there are four consecutive pieces of the current player
        if len(coordinates) >= 4:
            return True

        return False

if __name__ == "__main__":
    game = ConnectFour()
    game.play()
