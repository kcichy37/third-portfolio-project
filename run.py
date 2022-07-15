"""Game"""
import sys
import time
import pyfiglet
import pyinputplus as pyip
from termcolor import colored
from board import minesweeper, player, display_board


def main_menu():
    """
    Main menu for user to pick whether
    they want the rules or straight to difficulty options
    """

    # Main menu logo
    result = pyfiglet.figlet_format("Welcome To Minesweeper", font="slant")
    print(result)

    # Rules or Difficulty selection choice
    print("""Please choose one of the options:\n
    1) Rules
    2) Difficulty\n""")

    choice = pyip.inputInt("""Enter 1 for Rules or
2 for Difficulty: """, min=1, max=2)

    if choice == 1:
        # Rules
        game_rules()
        while True:
            back_to_main = input("\nEnter 'BACK' for main menu:\n").upper()
            if back_to_main == "BACK":
                main_menu()
                break
            else:
                print(f"\n'{back_to_main}' is the wrong input.")
    elif choice == 2:
        # Difficulty
        game()


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

    # Gives the rules a typing animation
    def typewriter(rules):
        for char in rules:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)

    print(typewriter(rules))


def restart():
    """
    Asks user if they want to quit the game
    or go back to main menu
    """

    print("""1) Main Menu
2) Quit\n""")
    choice = pyip.inputInt("""Enter 1 for Main Menu
or 2 to Quit: """, min=1, max=2)

    if choice == 1:
        main_menu()
    else:
        quit()


def game():
    """
    Game function that loops through
    two board and shows players board
    while uncovering the original board
    with users input.
    """
    game_status = True
    while game_status:

        # Difficulty selection
        print("\n1) Easy, 5x5 grid with 5 mines")
        print("2) Medium, 10x10 grid with 15 mines")
        print("3) Hard, 15x15 grid with 35 mines")
        print("4) Back\n")

        difficulty = pyip.inputInt("""Please enter 1 for Easy, 2 for Medium and 3 for Hard
            Or 4 to go back to main menu:\n""", min=1, max=4)

        if difficulty == 1:
            board_size = 2
            mines = 1
        elif difficulty == 2:
            board_size = 10
            mines = 10
        elif difficulty == 3:
            board_size = 15
            mines = 35
        else:
            main_menu()
        break

    minesweeper_map = minesweeper(board_size, mines)
    player_map = player(board_size)

    display_board(minesweeper_map)

    while True:

        print("\nSelect position:")
        r = pyip.inputInt("Row:", min=0, max=board_size-1)
        c = pyip.inputInt("Column:", min=0, max=board_size-1)
        r = int(r)
        c = int(c)

        # If mine hit game lost
        if minesweeper_map[r][c] == colored("X", "red", attrs=['bold']):
            display_board(minesweeper_map)
            print('\nYou hit a mine!!')
            print('~~~~~~~GAME-OVER~~~~~~~\n')
            restart()
        # Uncovers players board corresponding to users input
        else:
            player_map[r][c] = minesweeper_map[r][c]
            display_board(player_map)


main_menu()
