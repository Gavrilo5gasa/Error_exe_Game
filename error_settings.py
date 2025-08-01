from time import sleep

from tkinter import *
from tkinter import messagebox


def settings():
    while True:
        settings_window = Tk()
        settings_window.title("Settings")
        settings_window.geometry("400x400")
        settings_window.configure(background="#3B3B3B")
        settings_window.resizable(False, False)


        # Random stuff idk what it is
        x = IntVar() # pov: trying to name smth useless
        y = IntVar()
        z = IntVar()

        # Functions
        def background_colour():
            if x.get() == 1:
                settings_window.configure(background="white")
                checkbox.configure(bg="white", fg="black")
                checkbox2.configure(bg="white", fg="black")
            else:
                return None

        def death_loop_nums():
            # Infinite loop to keep the window open
            # This will create a dead window that cannot be closed
            # and will consume resources until the program is terminated.
            num = 0
            while True:
                num += 1
                print(f"{num}")
                continue

        def big_boy():
            big = Tk()
            big.title("Settings 2.0")
            big.geometry("400x400")
            big.minsize(1000000000,
                        1000000000)  # Mess with it if you want :) # in 1000% WILL CRASH YOUR PC

        def back():
            settings_window.destroy

        # Checkboxes
        checkbox = Checkbutton(settings_window, text="white mode :>",
                               bg="white",
                               fg="black",
                               variable=x,
                               onvalue= 1, offvalue=0,
                               command = background_colour)
        checkbox.place(x=0, y=0)

        checkbox2 = Checkbutton(settings_window, text="start counting",
                                bg="#3B3B3B",
                                fg="white",
                                variable=y,
                                onvalue=1, offvalue=0,
                                command = death_loop_nums)
        checkbox2.place(x=0, y=30)

        checkbox3 = Checkbutton(settings_window, text="Settings 2.0",
                                bg="#3B3B3B",
                                fg="white",
                                variable=z,
                                onvalue=1, offvalue=0,
                                command = big_boy)
        checkbox3.place(x=0, y=60)


        back = Button(settings_window, text="Back",
                                command=back,
                                bg="#3B3B3B",
                                fg="blue",
                                font=("Arial", 16),
                                relief=RAISED,
                                activebackground="#3B3B3B")
        back.place(x=0, y=90)

        settings_window.mainloop()

if __name__ == "__main__":
    settings()