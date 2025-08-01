from tkinter import *
from the_end import meeting

def ghost():

    password = input("Please enter the password: ")
    if password == "⎐":
        meeting()
    else:
        ghost_window1 = Tk()
        ghost_window1.title("")
        ghost_window1.geometry("800x0")
        ghost_window1.configure(background="white")
        ghost_window1.resizable(False, False)

        ghost_window1.mainloop()