import numpy as np

class Player:
    def __init__(self, player_number):
        self.player_number = player_number

class Board:
    def __init__(self):
        self.board = np.zeros((10, 10), dtype=int)

    def print_board(self):
        print(self.board.tostring().decode("utf-8"))

    def get_valid_column_number(self):
        while True:
            try:
                column = int(input("Player {}: Enter a column number (0-9): ".format(current_player.player_number)))
                if column < 0 or column > 9:
                    print("Invalid column number. Please enter a number between 0 and 9.")
                    continue
                return column
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_winner(self, player):
        # Check for a horizontal win
        for row in range(10):
            for col in range(7):
                if self.board[row, col] == player.player_number and self.board[row, col+1] == player.player_number and self.board[row, col+2] == player.player_number:
                    return True

        # Check for a vertical win
        for row in range(7):
            for col in range(10):
                if self.board[row, col] == player.player_number and self.board[row+1, col] == player.player_number and self.board[row+2, col] == player.player_number:
                    return True

        # Check for a diagonal win
        for row in range(7):
            for col in range(7):
                if self.board[row, col] == player.player_number and self.board[row+1, col+1] == player.player_number and self.board[row+2, col+2] == player.player_number:
                    return True

        # Check for a reverse diagonal win
        for row in range(7):
            for col in range(2, 10):
                if self.board[row, col] == player.player_number and self.board[row+1, col-1] == player.player_number and self.board[row+2, col-2] == player.player_number:
                    return True

        # If no winner, return False
        return False

    def place_piece(self, player, column):
        # Check if the column is full
        if self.board[0, column] != 0:
            print("Column is full. Please choose another column.")
            return

        # Place the current player's piece in the lowest free space of the column
        for row in range(9, -1, -1):
            if self.board[row, column] == 0:
                self.board[row, column] = player.player_number
                break


class AI:
    def __init__(self, player_number):
        self.player_number = player_number

    def get_best_move(self, board):
        # Get all possible moves
        moves = []
        for column in range(10):
            if board.board[0, column] == 0:
                moves.append(column)

        # Evaluate each move and choose the best one
        best_move = None
        best_score = -np.inf
        for move in moves:
            # Make the move on a copy of the board
            board_copy = board.copy()
            board_copy.place_piece(self, move)

            # Check if the move results in a win
            if board_copy.check_winner(self):
                return move

            # If not, evaluate the move based on the number of pieces in a row, column, and diagonal
            score = self.evaluate_move(board_copy)

            # Keep track of the best move and score
            if score > best_score:
                best_move = move
                best_score = score

        # Return the best move
        return best_move

    def evaluate_move(self, board):
        # Count the number of pieces in a row, column, and diagonal for both players
        my_row_count = np.count_nonzero(board.board == self.player_number, axis=1)
        my_col_count = np.count_nonzero(board.board == self.player_number, axis=0)
        my_diag_count = np.count_nonzero(np.diagonal(board.board) == self.player_number) + np.count_nonzero(np.diagonal(np.flip(board.board)) == self.player_number)

        opponent_row_count = np.count_nonzero(board.board == 3 - self.player_number, axis=1)
        opponent_col_count = np.count_nonzero(board.board == 3 - self.player_number, axis=0)
        opponent_diag_count = np.count_nonzero(np.diagonal(board.board) == 3 - self.player_number) + np.count_nonzero(np.diagonal(np.flip(board.board)) == 3 - self.player_number)

        # Calculate the score based on the number of pieces in a row, column, and diagonal
        score = 0
        for count in my_row_count:
            if count == 2:
                score += 1
            elif count == 3:
                score += 10
        for count in my_col_count:
            if count == 2:
                score += 1
            elif count == 3:
                score += 10
        for count in my_diag_count:
            if count == 2:
                score += 1
            elif count == 3:
                score += 10

        for count in opponent_row_count:
            if count == 2:
                score -= 1
            elif count == 3:
                score -= 10
        for count in opponent_col_count:
            if count == 2:
                score -= 1
            elif count == 3:
                score -= 10
        for count in opponent_diag_count:
            if count == 2:
                score -= 1
            elif count == 3:
                score -= 10

        return score


# Create the players
player1 = Player(1)
player2 = Player(2)
ai = AI(2)

# Create the game board
board = Board()

# Define the game over flag
game_over = False

# Define the winner flag
winner = 0

# Define the current player
current_player = player1

# Define the number of moves
num_moves = 0

# Main game loop
while not game_over:
    # Print the game board
    board.print_board()

    # Get a valid column number from the player
    if current_player == player1:
        column = board.get_valid_column_number()
    else:
        column = ai.get_best_move(board)

    # Place the current player's piece in the lowest free space of the column
    board.place_piece(current_player, column)

    # Check if the current player has won
    winner = board.check_winner(current_player)

    # If the current player has won, set the game over flag to True
    if winner:
        game_over = True

    # Increment the number of moves
    num_moves += 1

    # Switch the current player
    current_player = 3 - current_player

# Print the final game board
board.print_board()

# If there is a winner, print the winner
if winner:
    print("Player {} wins!".format(winner))
else:
    print("Draw")

# Ask the user if they want to play again
while True:
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
        # Reset the game
        board = Board()
        game_over = False
        winner = 0
        current_player = player1
        num_moves = 0
    else:
        break
