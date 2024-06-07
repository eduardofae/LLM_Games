
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def is_column_full(grid, column):
    return all(row[column] for row in grid)

def is_game_over(grid):
    return check_winner(grid) is not None

grid = [[] for _ in range(10)]

player1_symbol = 'X'
player2_symbol = 'O'

current_player = player1_symbol

def check_winner(grid):
    for i in range(10):
        for j in range(7):
            if grid[i][j] == grid[i][j + 1] == grid[i][j + 2] != 0:
                return grid[i][j]
    for j in range(10):
        for i in range(7):
            if grid[i][j] == grid[i + 1][j] == grid[i + 2][j] != 0:
                return grid[i][j]
    for i in range(7):
        for j in range(7):
            if grid[i][j] == grid[i + 1][j + 1] == grid[i + 2][j + 2] != 0:
                return grid[i][j]
            if grid[i][j] == grid[i + 1][j - 1] == grid[i + 2][j - 2] != 0:
                return grid[i][j]
    if all(all(row) for row in grid):
        return 'draw'
    return None

def place_piece(grid, player_symbol, column):
    if is_column_full(grid, column):
        raise ValueError('Invalid column number')
    for i in range(9, -1, -1):
        if not grid[i][column]:
            grid[i][column] = player_symbol
            break

def restart_game():
    global grid
    global current_player
    grid = [[] for _ in range(10)]
    current_player = player1_symbol

while True:
    print_grid(grid)
    column = int(input(f"{current_player}'s turn. Enter a column number (0-9): "))
    try:
        place_piece(grid, current_player, column)
    except ValueError:
        print('Invalid column number')
        continue
    winner = check_winner(grid)
    if winner is not None:
        if winner == 'draw':
            print("Draw!")
        else:
            print(f"{winner} wins!")
        break
    current_player = player2_symbol if current_player == player1_symbol else player1_symbol

    # Add the following line to allow the player to restart the game
    if input('Press "r" to restart the game or any other key to continue: ') == 'r':
        restart_game()
