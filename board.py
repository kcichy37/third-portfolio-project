import random


def minesweeper(board_size, mines):
    """
    Creates the board and all of the
    boards functions
    """
    board = [[[0] for row in range(board_size)] for column in range(board_size)]

    for num in range(mines):
        board[(random.randint(0, board_size-1 ))][random.randint(0, board_size-1)] = '[x]'

    for row in board:
        print(" ".join(str(cell) for cell in row))


    def mines_near(row, column):
        """
        Once the player chooses a spot 
        to uncover, the game needs to show
        a number that will represent 
        how many mines are around that area
        """
