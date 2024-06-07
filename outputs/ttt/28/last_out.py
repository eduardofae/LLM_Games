import copy
import re

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]

        # Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != ' ':
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]

        # Check draw
        if not any(x == ' ' for row in self.board for x in row):
            return 'Draw'

        return None

    def get_available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves

    def make_move(self, player, row, col):
        self.board[row][col] = player.symbol

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.wins = {self.player1: 0, self.player2: 0}

    def start_game(self):
        # Get player names and symbols
        player1_name = input("Enter player 1's name: ")
        player1_symbol = input("Enter player 1's symbol (X or O): ")
        while player1_symbol not in ['X', 'O']:
            player1_symbol = input("Invalid symbol, please enter X or O: ")

        player2_name = input("Enter player 2's name: ")
        player2_symbol = 'O' if player1_symbol == 'X' else 'X'

        # Create player objects
        self.player1 = Player(player1_name, player1_symbol)
        self.player2 = Player(player2_name, player2_symbol)

        # Determine starting player
        self.current_player = self.player1

    def play(self):
        while True:
            self.board.print_board()
            print(f"{self.current_player.name}'s turn")

            if self.current_player == self.player1:
                # Get player input
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))

                    if 0 <= row <= 2 and 0 <= col <= 2:
                        if self.board.board[row][col] == ' ':
                            self.board.make_move(self.current_player, row, col)
                            self.current_player = self.player2
                        else:
                            print("Invalid move, try again")

                except (ValueError, IndexError):
                    print("Invalid input, please enter integers between 0 and 2")

            else:
                # Computer's turn
                available_moves = self.board.get_available_moves()
                best_move = self.minimax(available_moves, self.player2)
                row, col = best_move
                self.board.make_move(self.current_player, row, col)
                self.current_player = self.player1

            winner = self.board.check_win()
            if winner:
                self.board.print_board()
                print(f"Player {winner} wins!")
                self.wins[winner] += 1
                break

    def minimax(self, available_moves, player):
        # Base case: no more moves available
        if not available_moves:
            return 0

        # Calculate the score for each possible move
        scores = []
        for move in available_moves:
            row, col = move
            self.board.make_move(player, row, col)
            score = self.evaluate_board(player)
            self.board.board[row][col] = ' '  # Undo the move
            scores.append(score)

        # Choose the move with the highest score
        if player == self.player2:
            best_score = max(scores)
            best_move = available_moves[scores.index(best_score)]
        else:
            best_score = min(scores)
            best_move = available_moves[scores.index(best_score)]

        return best_move

    def evaluate_board(self, player):
        # Check if the player has won
        winner = self.board.check_win()
        if winner == player.symbol:
            return 1

        # Check if the opponent has won
        opponent = self.player1 if player == self.player2 else self.player2
        if winner == opponent.symbol:
            return -1

        # Check if the board is full (draw)
        if not self.board.get_available_moves():
            return 0

        # Calculate the number of potential winning lines for each player
        player_lines = self.count_potential_lines(player)
        opponent_lines = self.count_potential_lines(opponent)

        # Return the difference in potential winning lines
        return player_lines - opponent_lines

    def count_potential_lines(self, player):
        count = 0

        for line in self.board.board + [''.join(row) for row in zip(*self.board.board)] + [self.board.board[0][0] + self.board.board[1][1] + self.board.board[2][2], self.board.board[0][2] + self.board.board[1][1] + self.board.board[2][0]]:
            if line.count(player.symbol) == 2 and ' ' in line:
                count += 1

        return count


if __name__ == "__main__":
    game = Game()
    game.start_game()
    game.play()
