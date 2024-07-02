import numpy as np
import pygame
from pygame import mixer

class ConnectFourGame:
    def __init__(self):
        self.game_board = np.zeros((10, 10), dtype=int)
        self.players = [Player(1, "Player 1"), Player(2, "Player 2")]
        self.current_player = self.players[0]

    def play(self):
        while True:
            # Get the player's move
            try:
                column = self.get_player_move()
            except ValueError:
                print("Invalid input. Please enter a valid integer between 1 and 10.")
                continue

            # Check if the column is valid
            if not self.is_valid_move(column):
                print("Invalid column. Please enter a column between 1 and 10.")
                continue

            # Place the player's piece in the column
            self.place_piece(column)

            # Check if the player has won
            if self.check_win():
                print("{} wins!".format(self.current_player.name))
                break

            # Switch to the other player
            self.switch_player()

        # Check if the game is a draw
        if np.all(self.game_board != 0):
            print("The game is a draw.")

    def get_player_move(self):
        while True:
            try:
                column = int(input("{}: Enter a column (1-10): ".format(self.current_player.name))) - 1
                if self.is_valid_move(column):
                    return column
                else:
                    print("Invalid column. Please enter a column between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid integer between 1 and 10.")

    def is_valid_move(self, column):
        return column >= 0 and column < 10 and self.game_board[9, column] == 0

    def place_piece(self, column):
        for i in range(9, -1, -1):
            if self.game_board[i, column] == 0:
                self.game_board[i, column] = self.current_player.symbol
                break

    def check_win(self):
        # Check for a horizontal win
        for i in range(10):
            if np.all(self.game_board[i, :] == self.current_player.symbol):
                return True

        # Check for a vertical win
        for j in range(10):
            if np.all(self.game_board[:, j] == self.current_player.symbol):
                return True

        # Check for a diagonal win
        for i in range(7):
            for j in range(7):
                if np.all(self.game_board[i:i+3, j:j+3] == self.current_player.symbol):
                    return True

        for i in range(2,10):
            for j in range(7):
                if np.all(self.game_board[i:i-3:-1, j:j+3] == self.current_player.symbol):
                    return True

        # No win found
        return False

    def switch_player(self):
        self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]

    def reset_game(self):
        self.game_board = np.zeros((10, 10), dtype=int)
        self.current_player = self.players[0]


class Player:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name


if __name__ == "__main__":
    # Initialize the game
    game = ConnectFourGame()

    # Initialize the sound effects
    mixer.init()
    drop_sound = mixer.Sound("drop.wav")
    win_sound = mixer.Sound("win.wav")

    # Play the game
    while True:
        # Get the player's move
        try:
            column = game.get_player_move()
        except ValueError:
            print("Invalid input. Please enter a valid integer between 1 and 10.")
            continue

        # Check if the column is valid
        if not game.is_valid_move(column):
            print("Invalid column. Please enter a column between 1 and 10.")
            continue

        # Place the player's piece in the column
        game.place_piece(column)

        # Play the drop sound effect
        drop_sound.play()

        # Check if the player has won
        if game.check_win():
            # Play the win sound effect
            win_sound.play()
            print("{} wins!".format(game.current_player.name))
            break

        # Switch to the other player
        game.switch_player()

    # Check if the game is a draw
    if np.all(game.game_board != 0):
        print("The game is a draw.")

    # Ask the player if they want to play again
    while True:
        play_again = input("Play again? (y/n): ")
        if play_again == "y":
            game.reset_game()
            game.play()
        else:
            break
