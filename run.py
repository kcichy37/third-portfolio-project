import sys
import time
import pyfiglet
import pyinputplus as pyip
from board import minesweeper, player, display_board

result = pyfiglet.figlet_format("Welcome To Minesweeper", font="slant")
print(result)


def main_menu():
    """
    Main menu for user to pick whether
    he wants the rules or straight to difficulty setting options
    """
    print("""Please choose one of the options:\n
    1) Rules
    2) Difficulty\n""")

    choice = pyip.inputInt("Please enter 1 for Rules or 2 for Difficulty selection:\n", min=1, max=2)

    if choice == 1:
        game_rules()

        while True:
            back_to_main = input("\nEnter 'BACK' for main menu:\n").upper()

            if back_to_main == "BACK":
                main_menu()
                break
            else:
                print(f"\n'{back_to_main}' is the wrong input.")
    elif choice == 2:
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


def check_board(map):
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True


def game():
    game_status = True
    while game_status:

        print("\n1) Easy, 5x5 grid with 5 mines")
        print("2) Medium, 10x10 grid with 15 mines")
        print("3) Hard, 15x15 grid with 35 mines")
        print("4) Back\n")

        difficulty = pyip.inputInt("""Please enter 1 for Easy, 2 for Medium and 3 for Hard
            Or 4 to go back to main menu:\n""", min=1, max=4)

        if difficulty == 1:
            board_size = 5
            mines = 3
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

    display_board(player_map)

    while True:

        if check_board(player_map) is False:

            print("\nSelect position:")
            r = input("Row:")
            c = input("Column:")
            r = int(r)
            c = int(c)

            if minesweeper_map[r][c] == "X":
                display_board(minesweeper_map)
                print('game over')
                break
            else:
                player_map[r][c] = minesweeper_map[r][c]
                display_board(player_map)
        else:
            display_board(player_map)
            print("won")
            game_status = False
            break


main_menu()