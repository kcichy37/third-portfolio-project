import pyfiglet
import pyinputplus as pyip


result = pyfiglet.figlet_format("Welcome To Minesweeper", font="slant")
print(result)


def main_menu():
    """
    Main menu for user to pick whether
    he wants the rules if he does not know how to play
    or to go straight to difficulty setting options
    """
    print("""Please choose one of the options:\n
    1) Rules
    2) Difficulty\n""")

    choice = pyip.inputInt("""Please enter 1 for Rules or 2 for Difficulty selection:\n""", min=1, max=2)

    if choice == 1:
        game_rules()

        while True:
            back_to_main = str(input("Enter 'BACK' for main menu:\n")).upper()

            if back_to_main == "BACK":
                main_menu()
            else:
                print("\nWrong input.")


def game_rules():

    """
    Explains the game rules to the user
    """

    print("""\n Rules
        Minesweeper is a game where
        mines are hidden in a grid of squares.
        Safe squares have numbers telling you
        how many mines touch the square.
        You can use the number clues to solve the
        game by opening all of the safe squares.
        If you click on a mine you lose the game!

        When you open a square
        that does not touch any mines,
        it will be empty and the adjacent
        squares will automatically open
        in all directions until reaching
        squares that contain numbers.
        A common strategy for starting
        games is to randomly mark a spot
        until you get a big opening with lots of numbers.\n""")


main_menu()


class Board:
    """
    Creates the board and all of the
    boards functions
    """
    # __init__ for the boards sizes
    # create board depending on difficulty
    # keep track of location revealed
    # plant the bombs randomly
