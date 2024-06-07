import sys

def jdv(board_size: int = 3, winning_combinations: List[List[Tuple[int, int]]] = None, player_symbols: List[str] = ['X', 'O']) -> None:
    """
    This function implements the "jdv" game, where two players take turns placing their pieces in a free space of a square grid,
    until one of them makes a line with a specified number of (horizontally, vertically, or diagonally) adjacent pieces, in which case the person
    that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw.

    Args:
        board_size: The size of the game board (default: 3).
        winning_combinations: A list of lists of tuples representing the winning combinations (default: 3-in-a-row).
        player_symbols: A list of symbols representing the players' pieces (default: ['X', 'O']).
    """

    # Create the game board
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

    # Set the default winning combinations if none provided
    if not winning_combinations:
        winning_combinations = []
        for i in range(board_size):
            # Horizontal combinations
            winning_combinations.append([(i, j) for j in range(board_size)])
            # Vertical combinations
            winning_combinations.append([(j, i) for j in range(board_size)])
        # Diagonal combinations
        winning_combinations.append([(i, i) for i in range(board_size)])
        winning_combinations.append([(i, board_size - 1 - i) for i in range(board_size)])

    # Create a variable to keep track of the current player
    current_player = 0

    # Create a variable to keep track of the number of moves made
    num_moves = 0

    # Main game loop
    while True:

        # Print the game board
        print_board(board)

        # Get the player's move
        move = get_move(current_player, board_size, player_symbols)

        # Place the player's piece on the board
        board[move[0]][move[1]] = player_symbols[current_player]

        # Increment the number of moves made
        num_moves += 1

        # Check if the player has won
        if check_win(board, current_player, winning_combinations):
            print(f"{player_symbols[current_player]} wins!")
            break

        # Check if the game is a draw
        if num_moves == board_size ** 2:
            print("Draw!")
            break

        # Switch to the other player
        current_player = (current_player + 1) % len(player_symbols)


def print_board(board: List[List[str]]) -> None:
    """
    This function prints the current state of the game board.
    """

    for row in board:
        print(' '.join(row))


def get_move(player: int, board_size: int, player_symbols: List[str]) -> Tuple[int, int]:
    """
    This function gets the player's move.

    Args:
        player: The current player (index).
        board_size: The size of the game board.
        player_symbols: A list of symbols representing the players' pieces.

    Returns:
        A tuple representing the row and column of the player's move.
    """

    while True:
        try:
            move = input(f"{player_symbols[player]}'s turn. Enter your move (row, column): ")
            move = [int(x) for x in move.split(',')]
            if not (0 <= move[0] < board_size and 0 <= move[1] < board_size):
                raise ValueError("Invalid move: Coordinates out of bounds.")
            if board[move[0]][move[1]] != ' ':
                raise ValueError("Invalid move: Space already occupied.")
            return move
        except ValueError as e:
            print(e)


def check_win(board: List[List[str]], player: int, winning_combinations: List[List[Tuple[int, int]]]) -> bool:
    """
    This function checks if the player has won.

    Args:
        board: The game board.
        player: The current player (index).
        winning_combinations: A list of lists of tuples representing the winning combinations.

    Returns:
        True if the player has won, False otherwise.
    """

    for combination in winning_combinations:
        if all([board[x[0]][x[1]] == player_symbols[player] for x in combination]):
            return True

    return False


if __name__ == "__main__":
    # Get the board size from the user
    try:
        board_size = int(input("Enter the board size (default: 3): ") or "3")
    except ValueError:
        print("Invalid board size. Using default size 3.")
        board_size = 3

    # Get the winning combinations from the user
    try:
        num_winning_combinations = int(input("Enter the number of winning combinations (default: 3): ") or "3")
    except ValueError:
        print("Invalid number of winning combinations. Using default value 3.")
        num_winning_combinations = 3

    winning_combinations = []
    for i in range(num_winning_combinations):
        try:
            winning_combination = input(f"Enter winning combination {i + 1} (e.g. 0,0;0,1;0,2): ").split(';')
            winning_combination = [tuple(int(x) for x in wc.split(',')) for wc in winning_combination]
            winning_combinations.append(winning_combination)
        except ValueError:
            print(f"Invalid winning combination {i + 1}. Skipping.")

    # Get the player symbols from the user
    try:
        player_symbols = input("Enter the player symbols (default: ['X', 'O']): ").split(',')
    except ValueError:
        print("Invalid player symbols. Using default symbols ['X', 'O'].")
        player_symbols = ['X', 'O']

    # Start the game
    jdv(board_size, winning_combinations, player_symbols)
