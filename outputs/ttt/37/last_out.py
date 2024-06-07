import copy

def display_board(board):
    """Display the game board."""
    print("Current board:")
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def player_move(board, player):
    """Get and validate player's move."""
    while True:
        move = input(f"Player {player}'s turn. Enter your move (row,col): ")
        row, col = [int(x) for x in move.split(",")]
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = player
            break
        else:
            print("Invalid move. Try again.")

def check_winner(board):
    """Check if there is a winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def main():
    """Run the main game loop."""
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    player = 'X'
    while True:
        display_board(board)
        player_move(board, player)
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break

        if ' ' not in [cell for row in board for cell in row]:
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

    # Ask if players want to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        main()

if __name__ == "__main__":
    main()
