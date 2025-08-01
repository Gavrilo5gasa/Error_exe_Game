from tkinter import *
from tkinter import messagebox

from Dead_tools import death_window
from error_windows import resouces

def main_window():
    main_window = Tk()

    main_window.geometry("300x310")
    main_window.title("Error.exe")
    main_window.configure(background="#3B3B3B")

    # texts
    down = Label(main_window, text="Maybe down", font=("Arial", 16), fg="blue", bg="#3B3B3B")
    down.place(x=1400, y=50)
    left = Label(main_window, text="Maybe left", font=("Arial", 16), fg="blue", bg="#3B3B3B")
    left.place(x=50, y=50)
    nothing = Label(main_window, text="Nothing here", font=("Arial", 16), fg="blue", bg="#3B3B3B")
    nothing.place(x=50, y=700)

    # buttons
    button_down = Button(main_window, text="Click Me :)",
                         command=main_window,
                         bd=10, bg="#3B3B3B",
                         fg="blue",
                         font=("Arial", 16),
                         relief=RAISED,
                         activebackground="#3B3B3B", )
    button_down.place(x=50, y=50)

    button_escape = Button(main_window, text="Exit",
                           command=resouces,
                           bd=10, bg="#3B3B3B",
                           fg="blue",
                           font=("Arial", 16),
                           relief=RAISED,
                           activebackground="#3B3B3B")
    button_escape.place(x=1450, y=750)

    main_window.mainloop()

if messagebox.askokcancel("BEFORE START!!", "This Game has a lot of dead ends and also memory usage it might crash your computer/lead to blue screens/log you out (Depends on what you are using Linux, Windows 10/11), so be careful and don't run it if you don't want to risk it. \n\nIf you want to continue press OK, if not press cancel and close the program."):
    while True:
        main_window()
else:
    print("Well that's sad :( \n\nBut you can always play later :)")
