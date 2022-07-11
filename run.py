import pyfiglet


result = pyfiglet.figlet_format("Welcome To Minesweeper", font="slant")
print(result)


def main_menu():
    """
    Main menu for user to pick whether
    he wants the rules if he does not know how to play
    or to go straight to difficulty setting options
    """
    # create a rules section
    # create 3 difficulties:
    # Easy (5x5 = 5 mines),
    # Medium (10x10 = 15 mines),
    # Hard (15x15 = 35 mines)
    # input for user to choose between Rules or Difficulty

class Board:
    """
    Creates the board and all of the
    boards functions
    """
    #__init__ for the boards sizes
    # create board depending on difficulty 
    # keep track of location revealed
    # plant the bombs randomly