"""Game"""
import sys
import time
from os import system
from pyfiglet import Figlet
import pyinputplus as pyip
from termcolor import colored
from board import minesweeper, player, display_board

# Main menu logo
figlet = Figlet(font="slant")


def main_menu():
    """
    Main menu for user to pick whether
    they want the rules or straight to difficulty options
    """

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
    """

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
        system('cls')


def game():
    """
    Game function that loops through
    two board and shows players board
    while uncovering the original board
    with users input.
    """
    game_status = True
    used_coordinates = []
    revealed_cells = 0

    while game_status:

        # Difficulty selection
        print("\n1) Easy, 5x5 grid with 5 mines")
        print("2) Medium, 8x8 grid with 10 mines")
        print("3) Hard, 10x10 grid with 25 mines")
        print("4) Back\n")

        difficulty = pyip.inputInt("""Please enter 1 for Easy, 2 for Medium and 3 for Hard
            Or 4 to go back to main menu:\n""", min=1, max=4)

        if difficulty == 1:
            board_size = 5
            mines = 5
        elif difficulty == 2:
            board_size = 8
            mines = 10
        elif difficulty == 3:
            board_size = 10
            mines = 25
        else:
            main_menu()
        break

    minesweeper_map = minesweeper(board_size, mines)
    player_map = player(board_size)

    # Displays given board
    display_board(player_map)

    while True:
        # Gets users choice
        print("\nSelect position:")
        r = pyip.inputInt("Row:", min=0, max=board_size-1)
        c = pyip.inputInt("Column:", min=0, max=board_size-1)
        coordinates = [r, c]

        # If mine hit game lost
        if minesweeper_map[r][c] == colored("X", "red", attrs=['bold']):
            display_board(minesweeper_map)
            print('\nYou hit a mine!!')
            print('~~~~~~~GAME-OVER~~~~~~~\n')
            restart()

        # Uncovers players board corresponding to users input
        # Checks for used coordinates
        else:
            if coordinates not in used_coordinates:
                # Joins users input together to form coordinates
                used_coordinates.append([r, c])

                # Reveales cells
                player_map[r][c] = minesweeper_map[r][c]
                display_board(player_map)

                # Counts how many cells revealed
                revealed_cells = revealed_cells + 1
            else:
                print('Coordinate already used, try again!')

            # Once all empty cells are revealed user wins
            if revealed_cells == board_size**2 - mines:
                print("\nWell done you didn't hit a mine")
                print("~~~~~~~YOU WON~~~~~~~\n")
                restart()


print(figlet.renderText("WELCOME TO MINESWEEPER"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
main_menu()
