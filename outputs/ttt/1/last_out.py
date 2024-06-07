class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.wins = 0

class Game:
    def __init__(self, size=3):
        self.game_grid = np.zeros((size, size))
        self.player_symbols = [Player('X'), Player('O')]
        self.current_player = 0

    def play(self):
        # Allow players to choose their symbols
        self.choose_symbols()

        while True:
            self.print_grid()

            # Get player's move
            while True:
                try:
                    row = int(input(f"Player {self.player_symbols[self.current_player].symbol}, enter the row (0-{self.game_grid.shape[0]-1}): "))
                    col = int(input(f"Player {self.player_symbols[self.current_player].symbol}, enter the column (0-{self.game_grid.shape[1]-1}): "))

                    if row < 0 or row > self.game_grid.shape[0]-1 or col < 0 or col > self.game_grid.shape[1]-1:
                        raise ValueError("Invalid move. Please enter a valid row and column.")
                    elif self.game_grid[row, col] != 0:
                        raise ValueError("That space is already taken. Please enter a valid space.")
                    else:
                        break
                except ValueError as e:
                    print(e)

            # Place player's piece in the grid
            self.game_grid[row, col] = self.player_symbols[self.current_player].symbol

            # Check for winner or draw
            winner = self.check_winner()
            if winner:
                self.print_grid()
                print(f"Player {winner.symbol} wins!")
                winner.wins += 1
                break
            elif self.check_draw():
                self.print_grid()
                print("It's a draw!")
                break

            # Switch to the other player
            self.current_player = (self.current_player + 1) % 2

    def print_grid(self):
        for row in self.game_grid:
            print(' '.join([str(int(cell)) for cell in row]))

    def check_winner(self):
        # Check rows
        for row in self.game_grid:
            if all(row == row[0]) and row[0] != 0:
                return self.player_symbols[int(row[0]) - 1]

        # Check columns
        for col in self.game_grid.T:
            if all(col == col[0]) and col[0] != 0:
                return self.player_symbols[int(col[0]) - 1]

        # Check diagonals
        if all(self.game_grid.diagonal() == self.game_grid.diagonal()[0]) and self.game_grid.diagonal()[0] != 0:
            return self.player_symbols[int(self.game_grid.diagonal()[0]) - 1]
        if all(np.flip(self.game_grid).diagonal() == np.flip(self.game_grid).diagonal()[0]) and np.flip(self.game_grid).diagonal()[0] != 0:
            return self.player_symbols[int(np.flip(self.game_grid).diagonal()[0]) - 1]

        # No winner yet
        return None

    def check_draw(self):
        return all(self.game_grid != 0)

    def reset(self):
        self.game_grid = np.zeros((self.game_grid.shape[0], self.game_grid.shape[1]))
        self.current_player = 0

    def print_wins(self):
        print(f"Player {self.player_symbols[0].symbol}: {self.player_symbols[0].wins} wins")
        print(f"Player {self.player_symbols[1].symbol}: {self.player_symbols[1].wins} wins")

    def choose_symbols(self):
        while True:
            player1_symbol = input("Player 1, choose your symbol: ")
            player2_symbol = input("Player 2, choose your symbol: ")
            if player1_symbol == player2_symbol:
                print("Players cannot choose the same symbol. Please choose different symbols.")
            else:
                self.player_symbols = [Player(player1_symbol), Player(player2_symbol)]
                break

if __name__ == "__main__":
    # Get the desired game board size from the user
    while True:
        try:
            size = int(input("Enter the desired game board size (minimum 3): "))
            if size < 3:
                raise ValueError("Invalid size. The game board size must be at least 3.")
            break
        except ValueError as e:
            print(e)

    # Create a new game object
    game = Game(size)

    # Play the game until a player wins or there is a draw
    while True:
        game.play()

        # Ask the players if they want to play again
        while True:
            play_again = input("Do you want to play again? (y/n): ")
            if play_again not in ['y', 'n']:
                print("Invalid input. Please enter 'y' to play again or 'n' to quit.")
            else:
                break

        # Reset the game if the players want to play again
        if play_again == 'y':
            game.reset()
        # Quit the game if the players do not want to play again
        else:
            break

        # Print the number of wins for each player
        game.print_wins()
