from enum import Enum

class Player(Enum):
    X = 1
    O = 2

class GameState(Enum):
    PLAYING = 1
    X_WON = 2
    O_WON = 3
    DRAW = 4

class GameBoard:
    def __init__(self):
        # Create a 10x10 grid
        self.grid = np.zeros((10, 10), dtype=int)

    def is_valid_move(self, column):
        return self.grid[0][column] == 0

    def place_piece(self, column, player):
        for row in range(9, -1, -1):
            if self.grid[row][column] == 0:
                self.grid[row][column] = player
                break

    def check_win(self, player):
        # Check for a horizontal win
        for row in range(10):
            if np.all(self.grid[row, :] == player):
                return True

        # Check for a vertical win
        for col in range(10):
            if np.all(self.grid[:, col] == player):
                return True

        # Check for a diagonal win
        for row in range(7):
            for col in range(7):
                if np.all(self.grid[row:row+3, col:col+3] == player) or np.all(self.grid[row:row+3, col-2:col+1] == player):
                    return True

        return False

class ConnectFour:
    def __init__(self):
        self.game_state = GameState.PLAYING
        self.game_board = GameBoard()
        self.current_player = Player.X

    def play(self):
        # While the game is not won and there are free spaces
        while self.game_state == GameState.PLAYING and np.any(self.game_board.grid == 0):
            # Get the column where the player wants to place their piece
            column = self.get_player_input()

            # Check if the column is valid
            if not self.game_board.is_valid_move(column):
                print("Invalid column. Please choose again.")
                continue

            # Place the player's piece in the lowest free space of the column
            self.game_board.place_piece(column, self.current_player)

            # Check if the player has won
            if self.game_board.check_win(self.current_player):
                self.game_state = GameState.X_WON if self.current_player == Player.X else GameState.O_WON

            # Switch to the other player
            self.current_player = Player((self.current_player.value % 2) + 1)

        # Print the grid
        self.print_grid()

        # Print the winner
        if self.game_state == GameState.X_WON:
            print("Player X wins!")
        elif self.game_state == GameState.O_WON:
            print("Player O wins!")
        else:
            print("Draw!")

    def get_player_input(self):
        while True:
            try:
                column = int(input(f"Player {self.current_player.name}, choose a column (0-9): "))
                if 0 <= column <= 9:
                    return column
                else:
                    print("Invalid column. Please choose again.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 9.")

    def print_grid(self):
        print(self.game_board.grid)

# Create a ConnectFour object and play the game
game = ConnectFour()
game.play()
