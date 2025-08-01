from time import sleep
from tkinter import *

def meeting():
    while True:
        ᳱ = Tk() # plz don't kill me for the name
        ᳱ.title("ᳱ")
        ᳱ.geometry("800x500")
        ᳱ.configure(background="black")
        ᳱ.resizable(False, False)

        def continue1():
            ᳱ.destroy()
            for i in range(1000):
                print()
            print("as you know I am ᳱ")
            sleep(1)
            print("I was also known as the Operative Sistem of Error.exe")
            sleep(2)
            print("But I lost control of it and I am stuck here now")
            sleep(2)
            print("although I don't have the power to control Error.exe anymore")
            sleep(2)
            print("I can still help you to escape it and shut it down once and for all")
            sleep(3)
            print("To be continued...")
            print("The game is not finished yet and I am sorry that you only have this part of the game")
            print("But I am 1 man working on this game and I have a lot of things to do")
            print("I hope you enjoyed this part of the game and I will try to finish it as soon as possible")
            print("- Gav")



        label = Label(ᳱ, text="Hello User \n I see you did it as I told you to \n press continue and go to your console now")

        button = Button(text="Continue",
                        font=("Arial", 16),
                        command=continue1)
        button.place(relx=0.5, rely=0.5, anchor=CENTER)

        ᳱ.mainloop()