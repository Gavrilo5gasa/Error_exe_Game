from tkinter import *

from ghost_window import ghost


def black_out():
    black_window = Tk()
    black_window.title("")
    black_window.geometry("800x500")
    black_window.configure(background="black")
    black_window.resizable(False, False)

    button_message = Button(black_window,
                            text="ᳱ",
                            font=("Arial", 16),
                            bg="black",
                            fg="#3B3B3B",
                            activebackground="black",
                            activeforeground="#3B3B3B",
                            command=ghost)
    button_message.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Start the main loop
    black_window.mainloop()