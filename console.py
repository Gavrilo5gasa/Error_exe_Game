import os
from time import sleep

from error_game import game
from error_settings import settings

# File Creator
def create_file_on_desktop(filename, content=""):
    home_dir = os.path.expanduser("~")
    desktop_path = os.path.join(home_dir, "Desktop")
    file_path = os.path.join(desktop_path, filename)

    with open(file_path, 'w') as f:
        f.write(content)
    print("Check your Desktop :)")


# Console
def console_run():
    print("----------Console----------")
    print("1 = Start Game")
    print("2 = Settings")
    print("3 = Exit")
    print("4 = Back")
    a = input("Input: ")

    if a == "1":
        print("Sending you to the Good Boy game...")
        sleep(1)
        print("Success!")
        game()
    elif a == "2":
        print("Opening settings...")
        sleep(1)
        print("Success!")
        settings()
    elif a == "3":
        create_file_on_desktop("Error.txt", "Hello user \n I am ᳱ and I am here to help you to escape Error.exe \n\n I don't have much time to explai everything but in the error.exe there is an exit button far far to the right \n After you press it I will probably be able to talk to you again \n i hope so at least \n Good luck you will need it \n Copy this: ⎐ and use it as the password")
    else:
        print("Invalid input. Please try again.")
        console_run()

if __name__ == "__main__":
    console_run()