import numpy as np

class TicTacToeGame:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.turn = 0
        self.game_over = False
        self.winner = None

    def play(self):
        while not self.game_over:
            self.print_board()

            # Get the player's move
            player = self.turn % 2 + 1
            move = self.get_player_move(player)

            # Check if the move is valid
            if not self.is_valid_move(move):
                print("Invalid move. Try again.")
                continue

            # Place the player's piece on the board
            self.board[move // 3, move % 3] = player

            # Check if the player has won
            if self.check_win(player):
                self.winner = player
                self.game_over = True
                self.print_winning_message()
                break

            # Check if the game is a draw
            if np.all(self.board != 0):
                self.game_over = True
                print("Draw!")
                break

            # Increment the turn counter
            self.turn += 1

    def print_board(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    print(" ", end=" ")
                elif cell == 1:
                    print("X", end=" ")
                elif cell == 2:
                    print("O", end=" ")
            print()

    def get_player_move(self, player):
        while True:
            try:
                move = int(input(f"Player {player}, enter your move (1-9): "))
                if move < 1 or move > 9:
                    raise ValueError("Move must be between 1 and 9.")
                return move - 1
            except ValueError as e:
                print(e)

    def is_valid_move(self, move):
        row, col = move // 3, move % 3
        return self.board[row, col] == 0

    def check_win(self, player):
        # Check the rows
        for row in self.board:
            if np.all(row == player):
                return True

        # Check the columns
        for col in range(3):
            if np.all(self.board[:, col] == player):
                return True

        # Check the diagonals
        if np.all(self.board.diagonal() == player):
            return True
        if np.all(np.flip(self.board).diagonal() == player):
            return True

        # No win
        return False

    def print_winning_message(self):
        if self.winner == 1:
            print("Player 1 wins with a horizontal line on row {row}.")
        elif self.winner == 2:
            print("Player 2 wins with a vertical line on column {col}.")
        elif self.winner == 3:
            print("Player 3 wins with a diagonal line from top left to bottom right.")
        elif self.winner == 4:
            print("Player 4 wins with a diagonal line from bottom left to top right.")

    def reset_game(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.turn = 0
        self.game_over = False
        self.winner = None


if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()
    while True:
        choice = input("Do you want to play again? (y/n): ")
        if choice == "y":
            game.reset_game()
            game.play()
        else:
            break
