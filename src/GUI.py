import tkinter
from tkinter import *
from tkinter import ttk


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Workout planner")

        self.screen_height = self.master.winfo_screenheight()
        self.screen_width = self.master.winfo_screenwidth()
        self.frm1 = ttk.Frame(self.master, padding=10)

    def place_frame_center(self, event):
        frame_width = self.frm1.winfo_reqwidth()
        frame_height = self.frm1.winfo_reqheight()

        x_pos = (self.screen_width - frame_width) // 2
        y_pos = (self.screen_height - frame_height) // 2

        self.frm1.place(x=x_pos, y=y_pos)

    def frame1(self):
        ttk.Button(self.master, text="Exit", command=self.master.destroy).grid(column=0, row=0)
        #tkinter.Button(self.master, bg='red', text= " X ", command=self.master.destroy).grid(column=0, row=0)
        #photo = tkinter.PhotoImage(file='Petr 2.png')
        #ttk.Button(self.master, image=photo, command=self.master.destroy).grid(column=0, row=0)

        ttk.Label(self.frm1, text="Vyberte část těla, kterou chcete posilovat").grid(column=1, row=0)

        current_var = tkinter.StringVar()
        bp_combobox = ttk.Combobox(self.frm1, textvariable=current_var)
        bp_combobox.grid(column=1, row=1)
        bp_combobox['values'] = ('břicho', 'záda', 'paže', 'prsa', 'ramena', 'stehna', 'lýtka')
        bp_combobox['state'] = ('readonly')

        ttk.Label(self.frm1, text="vyberte obtížnost").grid(column=1, row=2)

        current_var2 = tkinter.StringVar()
        lvl_combobox = ttk.Combobox(self.frm1, textvariable=current_var2)
        lvl_combobox.grid(column=1, row=3)
        lvl_combobox['values'] = ('začátečník', 'středně pokročilý', 'pokročilý')
        lvl_combobox['state'] = ('readonly')

        self.frm1.place(x= 0, y=0)
        self.frm1.bind("<Configure>", self.place_frame_center)


def main():
    root = Tk()
    gui = GUI(root)
    gui.frame1()
    root.attributes('-fullscreen', True)
    root.mainloop()


if __name__ == "__main__":
    main()