from tkinter import *
from tkinter import messagebox
from error_main import confirmed

def login():
    while True:
        login = Tk()
        login.title("Login to Error.exe")
        login.geometry("500x300")
        login.configure(background="#3B3B3B")

        # Text
        username = Label(login, text="Username:", font=("Arial", 16))
        username.place(x=0, y=0)

        password = Label(login, text="Password:", font=("Arial", 16))
        password.place(x=0, y=20)

        confirm_password = Label(login, text="C̸̨̧̡̝̙̦̫̫̣̼̭͓̘̘̥̙̞͙̱̘͚̦̪̼̼̺̞̻̀͜o̶̰͓͎̪͇͓̫̦̜͎̮̓̄̀̈́̈́̅͆̾̑̀́̔̂͐͒͋̄͑̍̕̕͘͝͝͝n̴̛̛͎̅̌͊͐̀̊̽̀̏̾̾̉̓͐̿͋͌͑̍̒̅̾͂̇̐̿͊̿́̆͐̀̑͆̋͒̆́̍͆̕̕͘͘̕͠͠f̷̢̢̨̢̢̛̛̩͎̥̝̻̦̪͈̳̞̥̮̰̰̬̮̞̭̲̮̫̘̠̟̗̮̮͙͉͔̹̹͈͙̖̘̲̼̠͈̖̈́̌̔̐̄͒̎̎̆̀͛̀́͊̉͊̀̂͐͑͆̅͐͊͋̌̓͂́̈́͐̎̾͑̕̚̚̚̕̚͠͝ị̶̢̲͓̫͔̘͓̓̇͑͒̈́̏̍͆̃̏̏̂̅͊̄̃͂̽̀̑̀̅͛̉̊̿̂̐̄̅̃̈́͋͂̆̉̋̾̚͘͘̚͘͝͝ŗ̶̨̡̧̛̠͙͚͍̥̝͈̘̥̬̻͕̹͚̰͕̼̜̻̮͕̟̋̑̏̓̽̓̓̀̽̂́̌̐͊͛̂̐̆̃̔̒̔͌́͒͊̋͊̈́̈́̃̆̏͑̏̃̄̓̇̊̊̿̓͜͝͝͠͝͝͝m̴̨̥̼͔̲̼̤͎̖͓̫̰̳̯̻̖̠̟͙͔̪̩̞̻̋͂̈͑̊̈́͐̉̇͑͊̂̉͋́̽͘̕͘͜͠͝ ̴̧̢͓̙̪̘͚̩͍̺͈̫̞̟̗̩̯̠͍͈̙̙̜͇͎͈͓̼̯͎̩̜͖͚͇́͊̑͋̈́͗̋̄̊̅̅͋̈́̉̔̐̽̽̄̎̾͗̀́͐͗̅̾́̆̈́͌̈́̀́̉̿͆̊͊͊̚̕ṕ̸͔̥̳̞̣̹̇̂͗͊̒̂̍̔͋̍͆͗͌̊̕̚͝a̵̧̢̦̞͎̩̟͙̤͚̪͔̝̗̲͍͎̮̣̮̺͓̠͕̺̣͎̞͎͉͍̙̮̬̞̝̤͔͙͓͎̭̗̟̐̏̀̇̆̾̏̐̓̈́́̍̏̔͐̒̚ş̴̡̡̢̨̯̳̞͈͚͈̲͍̬̰̹̹̟̺̭̭̪̘̱͎̦̳͚̟̥̈́͐̊̄̑̐̆͊͝ͅş̴̧̡̢̡̢̳̼̖̞͔̻͕͉̰̹̣̱̰̰͈̠͎͙̭̘̲̥̩̘̩͙͈̺̤̖̩͉͍̱͈̤̬̻̟̭̞̈́̐̐̓̄̋̌̎̽͆̉̃̈͒̈́̂͒́͛͛́̊̎̅̑̈̋͒̇͆̅̎͘̕̕͘͘͜͝ͅw̴̨̧̛̛̪̰͓̗̭̺͉͙͇̍́̈́̈́̑̀͊̆̀͊̂͒̓͑͂͐̆̿͊͗̅̃̓͒͆͗͂́̈́̑̈̌͂͂̿̓̌̋͊̕͜ͅͅǫ̸̨̨̠͕̦̹̻̬̹͙͚̺̪͎̞̖̹͖̪̰͈͍̻͎̩̠̤̬̩̙͂͑̿͆́̀͌̀̆̀̑̀͑̔̔̾̈́͜͝͝͝ͅr̶̢̡̧̛̛̛̩̟̘͈͍̱̗͔̬͎͔̞͚̫̻͈̲̣̟͉̗͓͖̪͖̺̫̻̭̺͍̩̥̙̹̟̩͌̍̓͗̑̒̑̂̄̀͐̓̌͛̉͒̈́͒̂̎̎͒͐̋̍̈́̄́̆̒̋̌̀͘̚̕͜͝͠͝͝͝ḑ̴̰̫̹͍̟̹̠͍̭͔̱̬̰́͐͋͂͂͛̈̇̂̈́͝͝ͅ:̶̧̢̧̨̡̢̧̧̢̧̪͙̪̜̣̗͓̰̰̝̞̲̫̯̗̯̜̟̳̫̜̹̪͖̗̞̯̻̪̜̱͖̺̺̺̀̾̓̊̿̒̆͒̐͂̀̐͐̐̿͐̏̇̓͗̌̍̇̈̄͑̎̈́̏̒̏̂̕̕̕͜͝͠͝͠ͅ", font=("Arial", 16))
        confirm_password.place(x=0, y=40)

        # User input (WILL NOT SAVE ANY DATA U PUT IN HERE)
        username_entry = Entry(font=("Arial", 16),
                      fg="blue",
                      width=20,)
        username_entry.insert(0, "Error")
        username_entry.place(x=190, y=0)


        password_entry = Entry(font=("Arial", 16),
                               fg="blue",
                                width=20,
                                show="*")
        password_entry.place(x=190, y=20)

        confirm_password_entry = Entry(font=("Arial", 16),
                                       fg="blue",
                                      width=20,
                                      show="*")
        confirm_password_entry.place(x=190, y=40)


        # Buttons
        confirm = Button(login, text="Confirm",
                         font=("Arial", 16),
                         command=confirmed)
        confirm.place(x=-50, y=100)

        login.mainloop()

if __name__ == '__main__':
    login()