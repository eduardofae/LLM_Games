from os import system, name

# Define the game board
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Define the players
players = ['X', 'O']

# Define the current player
current_player = 0

# Define the game state
game_state = 'playing'

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def print_board():
    """Prints the game board."""
    clear()
    print("   |   |   ")
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   ")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   ")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
    print("   |   |   ")

def is_valid_move(row, col):
  """Checks if the given move is valid."""
  return board[row][col] == ' '

def make_move(player, row, col):
    """Makes a move for the given player."""
    board[row][col] = player

def check_winner():
    """Checks if there is a winner."""
    
    # Check for horizontal wins
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            return board[row][0]

    # Check for vertical wins
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check for a draw
    if all(all(row) for row in board):
        return 'draw'

    # No winner yet
    return None

# Print the game board
print_board()

# Start the game loop
while game_state == 'playing':
    # Get the current player's move
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1

    # Check if the move is valid
    if is_valid_move(row, col):
        # Make the move
        make_move(players[current_player], row, col)
        
        # Check if there is a winner
        winner = check_winner()
        
        # Print the game board
        print_board()
        
        # Check if there is a winner
        if winner is not None:
            if winner == 'draw':
                print("The game is a draw.")
            else:
                print(f"{winner} wins!")
            game_state = 'finished'
        
        # Switch to the other player
        current_player = (current_player + 1) % len(players)
    else:
        print("Invalid move. Please try again.")
