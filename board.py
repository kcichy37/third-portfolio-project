import random


def minesweeper(board_size, mines):
    """
    Creates the board and all of the
    boards functions
    """
    board = [[0 for row in range(board_size)] for col in range(board_size)]

    for num in range(mines):
        row = random.randint(0, board_size-1)
        col = random.randint(0, board_size-1)
        board[col][row] = "X"

        if (row >= 0 and row <= board_size-2) and (col >= 0 and col <= board_size-1):
            if board[col][row+1] != "X":
                board[col][row+1] += 1

        if (row >= 1 and row <= board_size-1) and (col >= 1 and col <= board_size-1):
            if board[col][row-1] != "X":
                board[col][row-1] += 1

        if (row >= 1 and row <= board_size-1) and (col >= 1 and col <= board_size-1):
            if board[col-1][row-1] != "X":
                board[col-1][row-1] += 1

        if (row >= 0 and row <= board_size-2) and (col >= 1 and col <= board_size-1):
            if board[col-1][row+1] != "X":
                board[col-1][row+1] += 1

        if (row >= 0 and row <= board_size-1) and (col >= 1 and col <= board_size-1):
            if board[col-1][row] != "X":
                board[col-1][row] += 1

        if (row >= 0 and row <= board_size-2) and (col >= 1 and col <= board_size-2):
            if board[col+1][row+1] != "X":
                board[col+1][row+1] += 1

        if (row >= 1 and row <= board_size-1) and (col >= 0 and col <= board_size-2):
            if board[col+1][row-1] != "X":
                board[col+1][row-1] += 1

        if (row >= 0 and row <= board_size-1) and (col >= 0 and col <= board_size-2):
            if board[col+1][row] != "X":
                board[col+1][row] += 1

    max_row_len = len(max(board, key=len))
    print('    ', end='')
    print(*range(max_row_len), sep=' | ')
    print('', "----"*max_row_len)

    for idx, val in enumerate(board):
        print('%2s' % idx, end='| ')
        print(*val, sep=' | ')
