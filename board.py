"""Board"""
import random
from termcolor import colored


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
        board[c][r] = colored("X", "red", attrs=['bold'])

        # Checks neighbouring number = center right
        if (r >= 0 and r <= board_size-2) and (c >= 0 and c <= board_size-1):
            if board[c][r+1] != colored("X", "red", attrs=['bold']):
                board[c][r+1] += 1

        # Checks neighbouring number = center left
        if (r >= 1 and r <= board_size-1) and (c >= 0 and c <= board_size-1):
            if board[c][r-1] != colored("X", "red", attrs=['bold']):
                board[c][r-1] += 1

        # Checks neighbouring number = top left
        if (r >= 1 and r <= board_size-1) and (c >= 1 and c <= board_size-1):
            if board[c-1][r-1] != colored("X", "red", attrs=['bold']):
                board[c-1][r-1] += 1

        # Checks neighbouring number = top right
        if (r >= 0 and r <= board_size-2) and (c >= 1 and c <= board_size-1):
            if board[c-1][r+1] != colored("X", "red", attrs=['bold']):
                board[c-1][r+1] += 1

        # Checks neighbouring number = top center
        if (r >= 0 and r <= board_size-1) and (c >= 1 and c <= board_size-1):
            if board[c-1][r] != colored("X", "red", attrs=['bold']):
                board[c-1][r] += 1

        # Checks neighbouring number = bottom right
        if (r >= 0 and r <= board_size-2) and (c >= 0 and c <= board_size-2):
            if board[c+1][r+1] != colored("X", "red", attrs=['bold']):
                board[c+1][r+1] += 1

        # Checks neighbouring number = bottom left
        if (r >= 1 and r <= board_size-1) and (c >= 0 and c <= board_size-2):
            if board[c+1][r-1] != colored("X", "red", attrs=['bold']):
                board[c+1][r-1] += 1

        # Checks neighbouring number = bottom left
        if (r >= 0 and r <= board_size-1) and (c >= 0 and c <= board_size-2):
            if board[c+1][r] != colored("X", "red", attrs=['bold']):
                board[c+1][r] += 1
    return board


def player(board_size):
    """
    This the board the user will see
    with the mines and numbers hidden for "-"
    """
    board = [["-" for row in range(board_size)] for col in range(board_size)]
    return board


def display_board(map):
    """
    This function prints out selected
    board to the command line terminal
    with row and column numbers
    """
    max_row_len = len(max(map, key=len))
    print('    ', end='')
    print(*range(max_row_len), sep=' | ')
    print('', "----"*max_row_len)

    for idx, val in enumerate(map):
        print('%2s' % idx, end='| ')
        print(*val, sep=' | ')
