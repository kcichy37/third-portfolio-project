import random


def minesweeper(board_size, mines):
    """
    Creates the board and all of the
    boards functions
    """
    # Creates the board
    board = [[0 for row in range(board_size)] for col in range(board_size)]

    # Places mines randomly
    for num in range(mines):
        r = random.randint(0, board_size-1)
        c = random.randint(0, board_size-1)
        board[c][r] = "X"

        # Checks neighbouring number = center right
        if (r >= 0 and r <= board_size-2) and (c >= 0 and c <= board_size-1):
            if board[c][r+1] != "X":
                board[c][r+1] += 1

        # Checks neighbouring number = center left
        if (r >= 1 and r <= board_size-1) and (c >= 0 and c <= board_size-1):
            if board[c][r-1] != "X":
                board[c][r-1] += 1

        # Checks neighbouring number = top left
        if (r >= 1 and r <= board_size-1) and (c >= 1 and c <= board_size-1):
            if board[c-1][r-1] != "X":
                board[c-1][r-1] += 1

        # Checks neighbouring number = top right
        if (r >= 0 and r <= board_size-2) and (c >= 1 and c <= board_size-1):
            if board[c-1][r+1] != "X":
                board[c-1][r+1] += 1

        # Checks neighbouring number = top center
        if (r >= 0 and r <= board_size-1) and (c >= 1 and c <= board_size-1):
            if board[c-1][r] != "X":
                board[c-1][r] += 1

        # Checks neighbouring number = bottom right
        if (r >= 0 and r <= board_size-2) and (c >= 0 and c <= board_size-2):
            if board[c+1][r+1] != "X":
                board[c+1][r+1] += 1

        # Checks neighbouring number = bottom left
        if (r >= 1 and r <= board_size-1) and (c >= 0 and c <= board_size-2):
            if board[c+1][r-1] != "X":
                board[c+1][r-1] += 1

        # Checks neighbouring number = bottom left
        if (r >= 0 and r <= board_size-1) and (c >= 0 and c <= board_size-2):
            if board[c+1][r] != "X":
                board[c+1][r] += 1

    max_row_len = len(max(board, key=len))
    print('    ', end='')
    print(*range(max_row_len), sep=' | ')
    print('', "----"*max_row_len)

    for idx, val in enumerate(board):
        print('%2s' % idx, end='| ')
        print(*val, sep=' | ')


def player(board_size,):
    board = [["-" for row in range(board_size)] for col in range(board_size)]
    
    max_row_len = len(max(board, key=len))
    print('    ', end='')
    print(*range(max_row_len), sep=' | ')
    print('', "----"*max_row_len)

    for idx, val in enumerate(board):
        print('%2s' % idx, end='| ')
        print(*val, sep=' | ')
