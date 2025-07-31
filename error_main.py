from tkinter import *
from tkinter import messagebox

from console import console_run
from error_settings import settings

def confirmed():
    if messagebox.askyesno(title="Do you want to continue", message="Are you shure your password is strong"):
        messagebox.showinfo(title="Login Successful", message="You have successfully logged in!")
        return error_exe_app()

def error_exe_app():
    global play_game
    while True:
        error_app = Tk()
        error_app.title("Error.exe")
        error_app.geometry("3000x3000")
        error_app.configure(background="#3B3B3B")

        settings1 = Button(error_app,
                           font=("Arial", 16),
                           text="⌇☌⋏⟟⏁⏁⟒⌇",
                           command=settings)
        settings1.place(x=1450, y=800)

        dev_mode = Button(error_app,
                           font=("Arial", 16),
                           text="Open Console",
                           command=console_run)
        dev_mode.place(relx=0.5, rely=0.5, anchor=CENTER)
        error_app.mainloop()
