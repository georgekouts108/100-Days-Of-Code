GAME_BOARD = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def print_game_board():
    print("    1   2   3  ")
    print("  +" + ("-" * 11)+"+")
    for r in range(3):
        row = GAME_BOARD[r]
        print(f"{r+1} | {row[0]} | {row[1]} | {row[2]} |")
        print("  +" + ("-" * 11) + "+")
    print()


def mark_spot(row, col, symbol):
    GAME_BOARD[row][col] = symbol


def did_player_win():
    for row in GAME_BOARD:
        if ('-' not in row) and (row == [row[0]] * 3):
            return row[0]

    diagonals = [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]
    for diag in diagonals:
        state = [GAME_BOARD[spot[0]][spot[1]] for spot in diag]
        if ('-' not in state) and (state == [state[0]] * 3):
            return state[0]

    for col in range(3):
        state = [row[col] for row in GAME_BOARD]
        if ('-' not in state) and (state == [state[0]] * 3):
            return state[0]

    return -1

def board_is_full():
    for row in GAME_BOARD:
        if '-' in row:
            return False
    return True

def game():
    turn = 2
    while (did_player_win() == -1) and (not board_is_full()):
        turn = 1 if turn == 2 else 2
        symbol = 'Ⅹ' if turn == 1 else 'O'
        print(f"\nPLAYER {turn}'S TURN\n")
        print_game_board()

        while True:
            spot = input(f"Enter the row (1-3) and column (1-3) (e.g. \"1,2\" "
                     f"where you want to put an \'{symbol}\' : ")

            row, col = (int(spot[0])-1, int(spot[2])-1)
            if GAME_BOARD[row][col] == '-':
                mark_spot(row, col, symbol)
                break
            else:
                print("That spot is occupied.")

game()
print("\n" + ("="*50))
print_game_board()
winner = did_player_win()
if winner != -1:
    print(f"🏆🏆 Player {1 if winner == 'X' else 2} wins! 🏆🏆")
elif board_is_full():
    print("It's a draw.")
