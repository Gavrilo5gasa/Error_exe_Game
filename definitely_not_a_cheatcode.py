from os import WCONTINUED
from time import sleep

from aaa_start_here import main
from Dead_tools import death_window
from error_windows import corroupted
from application_window import login
from error_main import error_exe_app
from error_game import game
from console import console_run
from error_settings import settings
# -_- YOU CHEATER

def dev():
    print("----------Dev Console----------")
    print("1 = Start")
    print("2 = Death Window")
    print("3 = Corrupted Window")
    print("4 = Login Window")
    print("5 = Error.exe")
    print("6 = Good Boy game")
    print("7 = Settings :)")
    print("8 = Console")
    print("0 = Exit")
    a = input("Input: ")

    if a == "1":
        print("Sending you to the main window...")
        sleep(1)
        print("Success!")
        main()

    elif a == "2":
        print("Sending you to the dead window...")
        sleep(1)
        print("Success!")
        death_window()

    elif a == "3":
        print("Sending you to the corrupted window...")
        sleep(1)
        print("Success!")
        corroupted()

    elif a == "4":
        print("Sending you to the error window...")
        sleep(1)
        print("Success!")
        login()

    elif a == "5":
        print("Sending you to the error window...")
        sleep(1)
        print("Success!")
        error_exe_app()

    elif a == "6":
        print("Sending you to the Good Boy game...")
        sleep(1)
        print("Success!")
        game()

    elif a == "7":
        print("Sending you to the settings window...")
        sleep(1)
        print("Success!")
        settings()

    elif a == "0":
        return

    else:
        print("Invalid input, try again.")
        sleep(1)


if __name__ == "__main__":
    dev()