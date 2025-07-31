from time import sleep

from error_game import game

def console_run():
    print("----------Dev Console----------")
    print("1 = Start Game")
    print("0 = Exit")
    a = input("Input: ")

    if a == "1":
        print("Sending you to the Good Boy game...")
        sleep(1)
        print("Success!")
        game()