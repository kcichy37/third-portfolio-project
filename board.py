import random


def minesweeper(board_size, mines):
    """
    Creates the board and all of the
    boards functions
    """
    board = [[[0] for row in range(board_size)] for col in range(board_size)]

    for num in range(mines):
        x = random.randint(0, board_size-1)
        y = random.randint(0, board_size-1)
        board[x][y] = "[X]"

    max_row_len = len(max(board, key=len))
    print('    ', end='')
    print(*range(max_row_len), sep='   ')

    for idx, val in enumerate(board):
        print('%2s' % idx, end=' ')
        print(*val, sep=' ')
