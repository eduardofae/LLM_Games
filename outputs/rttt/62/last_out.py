import numpy as np

class Game:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.player1 = 'X'
        self.player2 = 'O'
        self.winning_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        self.num_wins_player1 = 0
        self.num_wins_player2 = 0

    def check_for_win(self):
        for winning_condition in self.winning_conditions:
            if self.board[winning_condition[0]] == self.board[winning_condition[1]] == self.board[winning_condition[2]] != 0:
                return True
        return False

    def check_for_draw(self):
        return np.all(self.board != 0)

    def get_player_input(self, player):
        while True:
            try:
                position = int(input(f"{player}'s turn. Enter a position (1-9): "))
                if position < 1 or position > 9:
                    print("Invalid input. Please enter a number between 1 and 9.")
                    continue
                return position - 1
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def play(self):
        while True:
            # Get the player's input
            position = self.get_player_input(self.player1)

            # Check if the space is free
            if self.board[position] != 0:
                print("That space is already taken. Please choose another space.")
                continue

            # Place the player's piece on the board
            self.board[position] = self.player1

            # Check if the player has won
            if self.check_for_win():
                print(f"{self.player1} wins!")
                self.num_wins_player1 += 1
                break

            # Check if the game is a draw
            if self.check_for_draw():
                print("It's a draw!")
                break

            # Switch to the next player
            self.player1, self.player2 = self.player2, self.player1

        # Print the final board
        print(self.board)

        # Ask the players if they want to play another round
        play_again = input("Do you want to play another round? (y/n): ")
        if play_again == 'y':
            # Reset the game board
            self.board = np.zeros((3, 3))

            # Start a new game
            self.play()
        else:
            # Exit the game
            print("Thanks for playing!")

if __name__ == "__main__":
    game = Game()
    game.play()
