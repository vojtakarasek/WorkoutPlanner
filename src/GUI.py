import tkinter
from tkinter import *
from tkinter import ttk


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Workout planner")

        self.screen_height = self.master.winfo_screenheight()
        self.screen_width = self.master.winfo_screenwidth()

    def frames(self):
        frm1 = ttk.Frame(self.master, padding=10)
        frm1.place(x=self.screen_width / 2, y=self.screen_height / 2)

        ttk.Button(self.master, text="Exit", command=self.master.destroy).grid(column=0, row=0)

        ttk.Label(frm1, text="Vyberte část těla, kterou chcete posilovat").grid(column=1, row=0)

        current_var = tkinter.StringVar()
        bp_combobox = ttk.Combobox(frm1, textvariable=current_var)
        bp_combobox.grid(column=1, row=1)
        bp_combobox['values'] = ('břicho', 'záda', 'paže', 'prsa', 'ramena', 'stehna', 'lýtka')
        bp_combobox['state'] = ('readonly')

        ttk.Label(frm1, text="vyberte obtížnost").grid(column=1, row=2)

        current_var2 = tkinter.StringVar()
        lvl_combobox = ttk.Combobox(frm1, textvariable=current_var2)
        lvl_combobox.grid(column=1, row=3)
        lvl_combobox['values'] = ('začátečník', 'středně pokročilý', 'pokročilý')
        lvl_combobox['state'] = ('readonly')


def main():
    root = Tk()
    gui = GUI(root)
    gui.frames()
    root.attributes('-fullscreen', True)
    root.mainloop()


if __name__ == "__main__":
    main()
