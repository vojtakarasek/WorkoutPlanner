import tkinter as tk
from tkinter import ttk

# lepe umistit
values = ['', 'břicho', 'záda', 'paže', 'prsa', 'ramena', 'stehna', 'lýtka']


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Workout planner")

        ttk.Button(self.master, text="Exit", command=self.master.destroy).grid(column=0, row=0)

        self.screen_height = self.master.winfo_screenheight()
        self.screen_width = self.master.winfo_screenwidth()


class Frame1:
    def __init__(self, master, screen_width, screen_height):
        self.master = master
        self.frm1 = ttk.Frame(self.master, padding=10)

        self.screen_width = screen_width
        self.screen_height = screen_height

        ttk.Label(self.frm1, text="Vyberte obtížnost").grid(column=1, row=0)

        selected_level = tk.StringVar()
        lvl_combobox = ttk.Combobox(self.frm1, textvariable=selected_level)
        lvl_combobox.grid(column=1, row=1)
        lvl_combobox['values'] = ('začátečník', 'středně pokročilý', 'pokročilý')
        lvl_combobox['state'] = 'readonly'

        ttk.Label(self.frm1, text="Vyberte část těla, kterou chcete posilovat").grid(column=1, row=2)

        self.frm1.place(x=0, y=0)
        self.frm1.bind("<Configure>", self.place_frame_center)

    def place_frame_center(self, event):
        frame_width = self.frm1.winfo_reqwidth()
        frame_height = self.frm1.winfo_reqheight()

        x_pos = (self.screen_width - frame_width) // 2
        y_pos = (self.screen_height - frame_height) // 2

        self.frm1.place(x=x_pos, y=y_pos)


def main():
    root = tk.Tk()
    gui = GUI(root)
    frame1 = Frame1(root, gui.screen_width, gui.screen_height)

    root.attributes('-fullscreen', True)
    root.mainloop()


if __name__ == "__main__":
    main()