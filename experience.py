from tkinter import Tk, Label, Button, StringVar
from hangmen import HangmenGame


class HangmenGUI:

    def __init__(self, master):
        self.v = StringVar()                # tries done label
        self.word = StringVar()             # the word of the game
        self.message = StringVar()          # message that helps the use
        self.already_guessed = StringVar()  # all the letters that are already guessed
        self.guess_output = ""

        self.game = HangmenGame()
        self.master = master
        master.title("Hangmen application")
# ------------------------------------------------------------------------------------------
        self.a_button = Button(master, text='A', command=lambda: self.make_guess('a'), height=2, width=3)
        self.a_button.grid(row=0, column=0)
        self.b_button = Button(master, text='B', command=lambda: self.make_guess('b'), height=2, width=3)
        self.b_button.grid(row=0, column=1)
        self.c_button = Button(master, text='C', command=lambda: self.make_guess('c'), height=2, width=3)
        self.c_button.grid(row=0, column=2)
        self.d_button = Button(master, text='D', command=lambda: self.make_guess('d'), height=2, width=3)
        self.d_button.grid(row=0, column=3)
        self.e_button = Button(master, text='E', command=lambda: self.make_guess('e'), height=2, width=3)
        self.e_button.grid(row=0, column=4)
        self.f_button = Button(master, text='F', command=lambda: self.make_guess('f'), height=2, width=3)
        self.f_button.grid(row=1, column=0)
        self.g_button = Button(master, text='G', command=lambda: self.make_guess('g'), height=2, width=3)
        self.g_button.grid(row=1, column=1)
        self.h_button = Button(master, text='H', command=lambda: self.make_guess('h'), height=2, width=3)
        self.h_button.grid(row=1, column=2)
        self.i_button = Button(master, text='I', command=lambda: self.make_guess('i'), height=2, width=3)
        self.i_button.grid(row=1, column=3)
        self.j_button = Button(master, text='J', command=lambda: self.make_guess('j'), height=2, width=3)
        self.j_button.grid(row=1, column=4)
        self.k_button = Button(master, text='K', command=lambda: self.make_guess('k'), height=2, width=3)
        self.k_button.grid(row=2, column=0)
        self.l_button = Button(master, text='L', command=lambda: self.make_guess('l'), height=2, width=3)
        self.l_button.grid(row=2, column=1)
        self.m_button = Button(master, text='M', command=lambda: self.make_guess('m'), height=2, width=3)
        self.m_button.grid(row=2, column=2)
        self.n_button = Button(master, text='N', command=lambda: self.make_guess('n'), height=2, width=3)
        self.n_button.grid(row=2, column=3)
        self.o_button = Button(master, text='O', command=lambda: self.make_guess('o'), height=2, width=3)
        self.o_button.grid(row=2, column=4)
        self.p_button = Button(master, text='P', command=lambda: self.make_guess('p'), height=2, width=3)
        self.p_button.grid(row=3, column=0)
        self.q_button = Button(master, text='Q', command=lambda: self.make_guess('q'), height=2, width=3)
        self.q_button.grid(row=3, column=1)
        self.r_button = Button(master, text='R', command=lambda: self.make_guess('r'), height=2, width=3)
        self.r_button.grid(row=3, column=2)
        self.s_button = Button(master, text='S', command=lambda: self.make_guess('s'), height=2, width=3)
        self.s_button.grid(row=3, column=3)
        self.t_button = Button(master, text='T', command=lambda: self.make_guess('t'), height=2, width=3)
        self.t_button.grid(row=3, column=4)
        self.u_button = Button(master, text='U', command=lambda: self.make_guess('u'), height=2, width=3)
        self.u_button.grid(row=4, column=0)
        self.v_button = Button(master, text='V', command=lambda: self.make_guess('v'), height=2, width=3)
        self.v_button.grid(row=4, column=1)
        self.w_button = Button(master, text='W', command=lambda: self.make_guess('w'), height=2, width=3)
        self.w_button.grid(row=4, column=2)
        self.x_button = Button(master, text='X', command=lambda: self.make_guess('x'), height=2, width=3)
        self.x_button.grid(row=4, column=3)
        self.y_button = Button(master, text='Y', command=lambda: self.make_guess('y'), height=2, width=3)
        self.y_button.grid(row=4, column=4)
        self.z_button = Button(master, text='Z', command=lambda: self.make_guess('z'), height=2, width=3)
        self.z_button.grid(row=5, column=0)
# ------------------------------------------------------------------------------------------
        # label that show the tries that are left (and done)
        self.label = Label(master, textvariable=self.v, font=("Comic Sans MS", 20))
        self.label.grid(row=0, column=5)
        self.v.set(self.game.get_tries() + " / 10")

        # shows the word (dot if letter is not guessed)
        self.label = Label(master, textvariable=self.word, font=("Comic Sans MS", 20))
        self.label.grid(row=1, column=5)
        self.word.set(self.game.hashed_word())

        # shows the letters that are already guessed
        self.label = Label(master, textvariable=self.already_guessed, font=("Comic Sans MS", 17))
        self.label.grid(row=6, column=5)
        self.already_guessed.set("already guessed: ")

        # shows the message for the user (for example: this letter is in the word)
        self.label = Label(master, textvariable=self.message, font=("Comic Sans MS", 10))
        self.label.grid(row=3, column=5)
        self.already_guessed.set(" ")

    def make_guess(self, letter):
        self.guess_output = self.game.guess(letter)
        self.update_values()

    # updates the dynamic values of the interface
    def update_values(self):
        self.v.set(self.game.get_tries() + " / 10")
        self.word.set(self.game.hashed_word())

        words = ""
        for letter in self.game.words_guessed:
            words = words + " " + letter + " "
        self.already_guessed.set("Already guessed: " + words)
        self.message.set(self.guess_output)


root = Tk()
root.geometry("600x300")
my_gui = HangmenGUI(root)
root.mainloop()
