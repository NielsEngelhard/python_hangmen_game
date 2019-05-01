from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.a_button = Button(master, text="a", command=self.dol)
        self.a_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def dol(self):
        print("Greetings!" + "lol")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()