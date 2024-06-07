import numpy as np

class Jdv:
    def __init__(self):
        """
        Initializes the game state.
        """
        self.grid = np.zeros((3, 3), dtype=int)
        self.player_turn = 1  # 1 for player 1, -1 for player 2
        self.player_names = {}  # dictionary to store player names and their numbers

    def play(self, row, col):
        """
        Places a player's mark on the grid at the specified row and column.

        Args:
            row (int): The row index (0-2).
            col (int): The column index (0-2).
        """
        if self.grid[row, col] == 0:
            self.grid[row, col] = self.player_turn
            self.player_turn *= -1  # switch player turn
        else:
            print("Invalid move. Space already occupied.")

    def is_winner(self):
        """
        Checks if there is a winner in the current grid.

        Returns:
            bool: True if there is a winner, False otherwise.
        """
        # check rows
        for row in range(3):
            if np.sum(self.grid[row, :]) == 3 or np.sum(self.grid[row, :]) == -3:
                return True

        # check columns
        for col in range(3):
            if np.sum(self.grid[:, col]) == 3 or np.sum(self.grid[:, col]) == -3:
                return True

        # check diagonals
        if np.sum(self.grid.diagonal()) == 3 or np.sum(self.grid.diagonal()) == -3:
            return True
        if np.sum(np.flipud(self.grid).diagonal()) == 3 or np.sum(np.flipud(self.grid).diagonal()) == -3:
            return True

        # check for a draw
        if np.all(self.grid != 0):
            return True

        return False

    def print_grid(self):
        """
        Prints the current grid to the console.
        """
        for row in self.grid:
            for col in row:
                if col == 1:
                    print("X", end=" ")
                elif col == -1:
                    print("O", end=" ")
                else:
                    print("-", end=" ")
            print()

    def get_player_name(self):
        """
        Returns the name of the player whose turn it is.

        Returns:
            str: The player's name.
        """
        return self.player_names[self.player_turn]

    def add_player(self, name):
        """
        Adds a player to the game and assigns them a player number.

        Args:
            name (str): The player's name.
        """
        if self.player_turn == 1:
            self.player_names[1] = name
        elif self.player_turn == -1:
            self.player_names[-1] = name
        self.player_turn *= -1  # switch player turn

if __name__ == "__main__":
    jdv = Jdv()

    # get player names
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    # add players to the game
    jdv.add_player(player1)
    jdv.add_player(player2)

    while True:
        jdv.print_grid()

        # get player move
        try:
            row = int(input("{}: Enter row (0-2): ".format(jdv.get_player_name())))
            col = int(input("{}: Enter column (0-2): ".format(jdv.get_player_name())))
        except ValueError:
            print("Invalid input. Please enter integers between 0 and 2.")
            continue

        # play move
        jdv.play(row, col)

        # check for winner or draw
        if jdv.is_winner():
            jdv.print_grid()
            if jdv.player_turn == 1:
                print("{} wins!".format(jdv.player_names[2]))
            else:
                print("{} wins!".format(jdv.player_names[1]))
            break
        elif jdv.is_draw():
            jdv.print_grid()
            print("Draw!")
            break
