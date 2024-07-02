import numpy as np

class ConnectFour:
    def __init__(self):
        self.grid = np.zeros((10, 10), dtype=int)
        self.players = [player1_symbol, player2_symbol]
        self.current_player = player1_symbol
        self.game_over = False
        self.draw = False
        self.winner = None
        self.player1_wins = 0
        self.player2_wins = 0

    def get_player_input(self):
        while True:
            try:
                column = int(input("Player {}, enter a column (1-10): ".format(self.current_player))) - 1
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 10.")
            else:
                break
        return column

    def place_piece(self, column):
        for i in range(9, -1, -1):
            if self.grid[i, column] == 0:
                self.grid[i, column] = self.current_player
                break

    def check_win(self):
        # Check for horizontal wins
        for row in self.grid:
            if np.all(row == self.current_player):
                return True
    
        # Check for vertical wins
        for col in self.grid.T:
            if np.all(col == self.current_player):
                return True
    
        # Check for diagonal wins
        for i in range(3):
            if np.all(self.grid[i:i+3, i:i+3] == self.current_player):
                return True
    
        for i in range(3):
            if np.all(self.grid[i:i+3, 6-i:9-i] == self.current_player):
                return True
    
        return False

    def check_draw(self):
        return np.all(self.grid != 0)

    def play(self):
        while not self.game_over:
            column = self.get_player_input()

            # Check if the move is valid
            if column < 0 or column > 9 or self.grid[9, column] != 0:
                print("Invalid move. Please try again.")
                continue

            # Place the player's piece in the grid
            self.place_piece(column)

            # Check if the player has won
            if self.check_win():
                self.game_over = True
                self.winner = self.current_player
                if self.winner == player1_symbol:
                    self.player1_wins += 1
                else:
                    self.player2_wins += 1
    
            # Check if the game is a draw
            elif self.check_draw():
                self.game_over = True
                self.draw = True

            # Switch the current player
            self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]

        # Print the game over message
        if self.draw:
            print("The game is a draw.")
        else:
            print("Player {} wins!".format(self.winner))

        # Print the final grid
        print(self.grid)

        # Print the player win counts
        print("Player 1 wins:", self.player1_wins)
        print("Player 2 wins:", self.player2_wins)

        # Ask the players if they want to play again
        while True:
            play_again = input("Do you want to play again? (y/n) ")
            if play_again == "y":
                self.reset_game()
                break
            elif play_again == "n":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def reset_game(self):
        self.grid = np.zeros((10, 10), dtype=int)
        self.current_player = player1_symbol
        self.game_over = False
        self.draw = False
        self.winner = None

# Create a new game object and play the game
game = ConnectFour()
game.play()
