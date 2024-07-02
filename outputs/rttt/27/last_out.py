import numpy as np
import winsound

def jdv():
    """
    This function implements the jdv game, where 2 players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw.
    """

    # Create the game board
    board = np.zeros((3, 3))

    # Create a list of the players
    players = ['X', 'O']

    # Set the current player to the first player
    current_player = players[0]

    # Define the winning lines
    winning_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    # Create a dictionary of sound effects
    sound_effects = {
        'move': 'move.wav',
        'win': 'win.wav',
        'draw': 'draw.wav'
    }

    # Play the game until someone wins or there are no more free spaces
    while True:
        # Get the player's move
        if current_player == 'X':
            move = int(input("Player " + current_player + ", enter your move (1-9): ")) - 1
        else:
            move = minimax(board, current_player)

        # Check if the move is valid
        if board[move // 3, move % 3] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[move // 3, move % 3] = current_player

        # Play the move sound effect
        winsound.PlaySound(sound_effects['move'], winsound.SND_ASYNC)

        # Check if the player has won
        for winning_line in winning_lines:
            if board[winning_line[0] // 3, winning_line[0] % 3] == board[winning_line[1] // 3, winning_line[1] % 3] == board[winning_line[2] // 3, winning_line[2] % 3] != 0:
                # Play the win sound effect
                winsound.PlaySound(sound_effects['win'], winsound.SND_ASYNC)

                print("Player " + current_player + " has won!")
                return

        # Check if there are no more free spaces
        if np.all(board != 0):
            # Play the draw sound effect
            winsound.PlaySound(sound_effects['draw'], winsound.SND_ASYNC)

            print("Draw!")
            return

        # Switch to the other player
        current_player = players[(players.index(current_player) + 1) % 2]

# Minimax algorithm
def minimax(board, player):
    """
    This function implements the minimax algorithm to find the best move for the computer opponent.
    """

    # Get all possible moves for the current player
    possible_moves = []
    for i in range(9):
        if board[i // 3, i % 3] == 0:
            possible_moves.append(i)

    # Evaluate the possible moves
    scores = []
    for move in possible_moves:
        # Make the move
        board[move // 3, move % 3] = player

        # Get the score of the move
        score = evaluate(board, player)

        # Undo the move
        board[move // 3, move % 3] = 0

        # Add the score to the list of scores
        scores.append(score)

    # Get the best move
    best_move = possible_moves[np.argmax(scores)]

    return best_move

# Evaluate the board
def evaluate(board, player):
    """
    This function evaluates the board and returns a score for the current player.
    """

    # Check if the player has won
    for winning_line in winning_lines:
        if board[winning_line[0] // 3, winning_line[0] % 3] == board[winning_line[1] // 3, winning_line[1] % 3] == board[winning_line[2] // 3, winning_line[2] % 3] != 0:
            if player == board[winning_line[0] // 3, winning_line[0] % 3]:
                return 1
            else:
                return -1

    # Check if there are no more free spaces
    if np.all(board != 0):
        return 0

    # Return the score of the board
    return 0

# Play the game
while True:
    jdv()
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == 'n':
        break
