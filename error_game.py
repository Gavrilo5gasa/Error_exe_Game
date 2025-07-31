from tkinter import *



def game():
    while True:
        def move_up(event):
            goodboy_label.place(x=goodboy_label.winfo_x(), y=goodboy_label.winfo_y()-10)
        def move_down(event):
            goodboy_label.place(x=goodboy_label.winfo_x(), y=goodboy_label.winfo_y()+10)
        def move_left(event):
            goodboy_label.place(x=goodboy_label.winfo_x()-10, y=goodboy_label.winfo_y())
        def move_right(event):
            goodboy_label.place(x=goodboy_label.winfo_x()+10, y=goodboy_label.winfo_y())

        room = Tk()
        room.title("Good Boy.exe")
        room.configure(background="#3B3B3B")
        room.geometry("800x500")
        room.resizable(False, False)

        binary = Label(room, text="01000101 01110010 01110010 01101111 01110010 00101110 01100101 01111000 01100101 00111010 \n01111000 00100000 00111101 00100000 00110010 00110000 00110000 00110000 \n 01111001 00100000 00111101 00100000 00110101 00110000 ", bg="#3B3B3B", fg="#404040")
        binary.place(relx=0.5, rely=0.5, anchor="center")

        start = Label(room, text="Press WASD to move", font=("Arial", 16), fg="white", bg="#3B3B3B")
        start.place(x= 10, y=50)

        goodboy = PhotoImage(file="textures/good_boy.png")
        goodboy_label = Label(room, image=goodboy, bg="#3B3B3B")
        goodboy_label.place(x = 230, y = 35)

        wall = PhotoImage(file="textures/long_wall_x.png")
        wall_label = Label(room, image=wall, bg="#3B3B3B")
        wall_label.place(x = 0, y = 0)

        wall_label2 = Label(room, image=wall, bg="#3B3B3B")
        wall_label2.place(x = 0, y = 470)

        room.bind("<w>", move_up)
        room.bind("<s>", move_down)
        room.bind("<a>", move_left)
        room.bind("<d>", move_right)
        room.mainloop()
