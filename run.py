import sys
import time
import pyfiglet
import pyinputplus as pyip
from board import minesweeper


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

    choice = pyip.inputInt("Please enter 1 for Rules or 2 for Difficulty selection:\n", min=1, max=2)

    if choice == 1:
        game_rules()

        while True:
            back_to_main = str(input("\nEnter 'BACK' for main menu:\n")).upper()

            if back_to_main == "BACK":
                main_menu()
                break
            else:
                print(f"\n'{back_to_main}' is the wrong input.")
    elif choice == 2:
        print("\n1) Easy, 5x5 grid with 5 mines")
        print("2) Medium, 10x10 grid with 15 mines")
        print("3) Hard, 15x15 grid with 35 mines")
        print("4) Back\n")

        difficulty = pyip.inputInt("""Please enter 1 for Easy, 2 for Medium and 3 for Hard 
        Or 4 to go back to main menu:\n""", min=1, max=4)

        if difficulty == 1:
            minesweeper(5, 3)
        elif difficulty == 2:
            minesweeper(10, 10)
        elif difficulty == 3:
            minesweeper(15, 35)
        else:
            main_menu()


def game_rules():

    """
    Explains the game rules to the user
    """

    rules = """\n Rules
    Minesweeper is a game where mines are hidden in a grid.
    Safe squares have numbers telling you how many mines touch the square.
    You can use the number clues to solve the game, 
    by opening all of the safe squares.
    If you click on a mine you lose the game!

    When you open a square that does not touch any mines,
    it will be empty and the adjacent squares will automatically open
    in all directions until reaching squares that contain numbers.
    A common strategy for starting games is to randomly mark a spot
    until you get a big opening with lots of number clues."""

    def typewriter(rules):
        for char in rules:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)

    print(typewriter(rules))


main_menu()
