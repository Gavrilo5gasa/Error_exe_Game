from tkinter import *
from error_windows import resouces, win



def death_window():

    # This function creates a new window that looks the same as the main window
    death = Toplevel()
    death.geometry("300x310")
    death.title("Error.exe")
    death.configure(background="#3B3B3B")

    # texts
    down = Label(death, text="Maybe down", font=("Arial", 16), fg="blue", bg="#3B3B3B")
    down.place(x=1400, y=50)
    left = Label(death, text="Maybe left", font=("Arial", 16), fg="blue", bg="#3B3B3B")
    left.place(x=50, y=50)
    nothing = Label(death, text="Nothing here", font=("Arial", 16), fg="blue", bg="#3B3B3B")
    nothing.place(x=50, y=700)

    # buttons
    button_down = Button(death, text="Click Me :)",
                         command=death_window,
                         bd= 10, bg="#3B3B3B",
                         fg="blue",
                         font=("Arial", 16),
                         relief=RAISED,
                         activebackground="#3B3B3B",)
    button_down.place(x=50, y=50)

    button_escape = Button(death, text="Exit",
                           command=resouces,
                           bd=10, bg="#3B3B3B",
                           fg="blue",
                           font=("Arial", 16),
                           relief=RAISED,
                           activebackground="#3B3B3B")
    button_escape.place(x=1450, y=750)
    death.mainloop()

