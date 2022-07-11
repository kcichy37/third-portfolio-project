def minesweeper(board_size):
    """
    Creates the board and all of the
    boards functions
    """
    board = [[[0] for row in range(board_size)] for column in range(board_size)]
    for row in board:
        print(" ".join(str(cell) for cell in row))
