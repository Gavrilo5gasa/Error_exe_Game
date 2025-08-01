from tkinter import *
from tkinter import messagebox, Button

from application_window import login

def resouces():
    while True:
        if messagebox.askyesno(title="An Error Occurred", message="Error: Could not load the requested resources. \nDo you want to try again?"):
            print ("Trying to load resources again...")
            return resouces()
        else:
            are_you_sure()

def are_you_sure():
    if messagebox.askyesno(title="Are you sure?", message="Do you really want to continue with out resources?"):
        return corroupted()
    else:
        return resouces()

def corroupted():
        corroupted = Tk()
        corroupted.geometry("300x310")
        corroupted.title("E̸̛̛͚͉̟̖͂̿͂̈́̈́̅̈̇́́͐͝r̸̨͔͙͚̘̗̱̱̰͖̓͗̌̆̂̓̋̏̿̚̕͠ṛ̸̹͉̘͇̟̪̣͛ò̴̡͍̫̫͔̙̣̳͚̰͕̗̮̪̩͙̞̖̝̟̙͚͓̤͗́̅̀̔͌̏̉̉͌͂̑͘͝r̵͚͆͗̈́͐.̵̢̢͇͚̟͈͉̟̫̘̦̬̮͕̠̥̳̣͕͓̝̘̉͛̋̀̾̏̀͝͝͠e̶͚͈͑́̓̇̂͌̈́̌̋̄͂͒̈́͂̐̂̄̓͘̚͝x̷̨̨̛͎̫̘̩͉̟̥̳͈̩̺͈̟̯̳͂͊͆̊̈̍͋̆͊̄͊̓͑̌̈̌̒͌́ͅe̷̺͙̲̤̣̳̜͔̜̹̲̱̹̼̭̯͎̖͋̒̈́̑̐̌͜͜")
        corroupted.configure(background="#3B3B3B")

        # texts
        down = Label(corroupted, text="G̷̨̨̩̖̜̹̫̮͔̋͑̀̑̅̍̒̀̀̆͑̊́̀̔̓̈̏̊̑̊̂̈̉͂͑̇͋̚̕͝͠ö̸̧̨͓͖͉̜̰͉̭̯͓̯̪̩͙̪̱̯̦̺̱͛͒͋̀ ̸̨̨̧̨̛̫͚͉̳̼̘͇͓̙̣͚̼̹̖͇͓͕̻͕̤̼̥̮͇̜̦̝͉̯̲͍̭̠̩̱̖̠̖̻̺̲̮̼̝̏͒́̑̍̏̔̑̐̀͘ḓ̸̨̨̢̫̺̼̝̣͉̠̣̖̘̗͓̮̣͖̼̫̱̙͕̱̙̽̃̋̿̈́̇̚͜͠ő̷̡̢̢̩̲͉͚̞̩͇͔̥̠͚̣̞̙̳̝̖̟̮̭͈̟̯̦͈̫̲͖̙͂̓̀̊̒̄͑̄̋͒̊̉̍̄͊́̌͛̈͗̈́̋̍̅̀́͂͘̕͝͝͝ͅw̴̧̛̬̺͍̼͙̣̹̻̤̺̠̗͍͔͈̦̗̱̮̫̳̣͈̥̜̞̐͗͆̈̍͂̽̽͗̑̆͊̽͒̈́̋̒̍̕͘͜͜͜͝͝ͅņ̴̢̧̨̠̼̺̼͈͉̰͙̭͎̦̳͈̟͍̣̮͈̬͔̮̪̼͇̬̣̠̫͓̭̫́̐͛̃̾̂̉̀́͆̄́̀̇̍͊̕͜͜͝ͅͅ", font=("Arial", 16), fg="blue", bg="#3B3B3B")
        down.place(x=2500, y=50)
        right = Label(corroupted, text="Ģ̷̡̧̡̣͔̣̠̤̱̯̻̮̮̮̮̻̱͎͍̽͝ͅơ̵̧̢̨̨̨̛̛̭̪̫͓̦͓͕͕̜͎̣̹̞̜̘͔̝͈̪̟̪̗̰͚̜͚͇̜̘̗̖̥͎̦̙̯̗͕̽̔͒̄̊͗̅̋͆̽̓̾̀͒̉̔̂̌̾̎́̃̇̆̐͒̎̽͊̌͐̔̾̑͋̾̽̈́̅̂̽̍̚͘͝͝͝ ̴̡̧̛̥͈̱̺̞̠̖͙̥̝̼̣̹̝͚̻̭͇̳̥̻̲͕̩̖͖̺̥̻̱̘̮̪̖̜͉̾͛͛̀͜ͅr̴̢̡̡̛̦̤̪̘̳͕̥̯̙̤͇̹̬̝̠̰̥͙̬̭͖̟̤̈́̈́́̄̑͛̌͋̊̅̀̽̉̍̏͆̋̾̊̀̂̍̄̄̕̕̕͝͠ī̷̧̧̫̺͇̞̦͍̠̲͖̱̳̯͍̘̻͕̹̩͎̦͎̝̦͕̩͙̹̫̦̙̩̰̪͉̞̥͚̳̳͇̻͑͒͊̽̍̏̈́͑̏̈́̂̈́̽̌̇̎͑̐̿͂̃͋͆̒̍̇̈͋͒̍̐̚̕̚̕̕̚̚̚̚͜͜͝͠͝ͅͅͅͅģ̵̞͖̙̦͍̮̺̗͍͔̪̜̪͚̺̩̤̝̖͇͖͍͉̼̦̗̮̂̏̓͌̓͋̍̇́̑̽̅̐̒̿́͊̋̍̑͌͐̅̚͜͝ḥ̵͛̍͘̚͠͠t̵̨̧̧̡̛̛̻͈̼̮̰̼̩̬͎͇̹͔͍̦̙̱̠̫̲̹̭̲̟̝̮͓̞̒̈́̂̒́̈̀̈́͆̉̽̀̄̎͗͂̌̀̈̉̏̔͋̓͌́́̓̏̊̔̿̀͑̒̈́̌̚̚͝͝ͅ", font=("Arial", 16), fg="blue", bg="#3B3B3B")
        right.place(x=50, y=50)
        # buttons
        button_application = Button(corroupted, text="Login",
                             command=login,
                             bd=10, bg="#3B3B3B",
                             fg="blue",
                             font=("Arial", 16),
                             relief=RAISED,
                             activebackground="#3B3B3B")
        button_application.place(x=2500, y=500)
        button_exit = Button(corroupted, text="Exit",
                             command=corroupted.destroy,
                             bd=10, bg="#3B3B3B",
                             fg="blue",
                             font=("Arial", 16),
                             relief=SUNKEN,
                             activebackground="#3B3B3B")



def win():
    messagebox.showerror(title="YOU ESCAPED THE WINDOW!!", message="Error: You have won the game!")

