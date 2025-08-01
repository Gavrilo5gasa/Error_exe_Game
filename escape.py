from tkinter import *
from tkinter.messagebox import *
from black_window import black_out


def exit_1():
    if askokcancel(title="Error 202", message="YOU ARE NOT GOING TO EXIT YOU ARE NOT ALLOWED TO EXIT"):
        return None
    else:
        if askyesno(title="", message="Y-0u ₾aℕℸ ⎄⏺ tHat \n Please press yes if you want to exit \n Press no if you want to continue"):
            return black_out()



