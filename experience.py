from tkinter import Tk, Label, Button, StringVar
from python_hangmen_game.hangmen import HangmenGame
from python_hangmen_game.words import Generator

class HangmenGUI:
    def __init__(self, master):
        self.game = HangmenGame()
        label_tries_done = StringVar()  # tries done label
        self.master = master
        master.title("Hangmen application")
# ------------------------------------------------------------------------------------------
        self.a_button = Button(master, text='A', command=lambda: self.greet('a'), height=2, width=3)
        self.a_button.grid(row=0, column=0)
        self.b_button = Button(master, text='B', command=lambda: self.greet('b'), height=2, width=3)
        self.b_button.grid(row=0, column=1)
        self.c_button = Button(master, text='C', command=lambda: self.greet('c'), height=2, width=3)
        self.c_button.grid(row=0, column=2)
        self.d_button = Button(master, text='D', command=lambda: self.greet('d'), height=2, width=3)
        self.d_button.grid(row=0, column=3)
        self.e_button = Button(master, text='E', command=lambda: self.greet('e'), height=2, width=3)
        self.e_button.grid(row=0, column=4)
        self.f_button = Button(master, text='F', command=lambda: self.greet('f'), height=2, width=3)
        self.f_button.grid(row=1, column=0)
        self.g_button = Button(master, text='G', command=lambda: self.greet('g'), height=2, width=3)
        self.g_button.grid(row=1, column=1)
        self.h_button = Button(master, text='H', command=lambda: self.greet('h'), height=2, width=3)
        self.h_button.grid(row=1, column=2)
        self.i_button = Button(master, text='I', command=lambda: self.greet('i'), height=2, width=3)
        self.i_button.grid(row=1, column=3)
        self.j_button = Button(master, text='J', command=lambda: self.greet('j'), height=2, width=3)
        self.j_button.grid(row=1, column=4)
        self.k_button = Button(master, text='K', command=lambda: self.greet('k'), height=2, width=3)
        self.k_button.grid(row=2, column=0)
        self.l_button = Button(master, text='L', command=lambda: self.greet('l'), height=2, width=3)
        self.l_button.grid(row=2, column=1)
        self.m_button = Button(master, text='M', command=lambda: self.greet('m'), height=2, width=3)
        self.m_button.grid(row=2, column=2)
        self.n_button = Button(master, text='N', command=lambda: self.greet('n'), height=2, width=3)
        self.n_button.grid(row=2, column=3)
        self.o_button = Button(master, text='O', command=lambda: self.greet('o'), height=2, width=3)
        self.o_button.grid(row=2, column=4)
        self.p_button = Button(master, text='P', command=lambda: self.greet('p'), height=2, width=3)
        self.p_button.grid(row=3, column=0)
        self.q_button = Button(master, text='Q', command=lambda: self.greet('q'), height=2, width=3)
        self.q_button.grid(row=3, column=1)
        self.r_button = Button(master, text='R', command=lambda: self.greet('r'), height=2, width=3)
        self.r_button.grid(row=3, column=2)
        self.s_button = Button(master, text='S', command=lambda: self.greet('s'), height=2, width=3)
        self.s_button.grid(row=3, column=3)
        self.t_button = Button(master, text='T', command=lambda: self.greet('t'), height=2, width=3)
        self.t_button.grid(row=3, column=4)
        self.u_button = Button(master, text='U', command=lambda: self.greet('u'), height=2, width=3)
        self.u_button.grid(row=4, column=0)
        self.v_button = Button(master, text='V', command=lambda: self.greet('v'), height=2, width=3)
        self.v_button.grid(row=4, column=1)
        self.w_button = Button(master, text='W', command=lambda: self.greet('w'), height=2, width=3)
        self.w_button.grid(row=4, column=2)
        self.x_button = Button(master, text='X', command=lambda: self.greet('x'), height=2, width=3)
        self.x_button.grid(row=4, column=3)
        self.y_button = Button(master, text='Y', command=lambda: self.greet('y'), height=2, width=3)
        self.y_button.grid(row=4, column=4)
        self.z_button = Button(master, text='Z', command=lambda: self.greet('z'), height=2, width=3)
        self.z_button.grid(row=5, column=0)
# ------------------------------------------------------------------------------------------

        label_tries_done.set(self.game.getTries())
        self.label = Label(master, text=v.get())
        self.label.grid(row=0, column=5)
        label_tries_done.set(self.game.getTries())
        print(self.game.getTries())

    def greet(self, letter):
        self.game.guess(letter)
        label_tries_done.set(self.game.getTries())


root = Tk()
my_gui = HangmenGUI(root)
root.mainloop()
