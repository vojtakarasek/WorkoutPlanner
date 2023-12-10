import tkinter
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

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Frame1, Frame2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('Frame1')

        def show_frame(self, page_name):
            shown_frame = self.frames[page_name]
            shown_frame.tkraise()




class Frame1():
    def __init__(self, master, screen_width, screen_height):
        self.master = master
        self.frm1 = ttk.Frame(self.master, padding=10)

        # variable helping with comboboxes counting
        self.i = 0

        # monitor size
        self.screen_width = screen_width
        self.screen_height = screen_height

        ttk.Label(self.frm1, text="Vyberte obtížnost").grid(column=1, row=0)

        # select level combobox
        selected_level = tk.StringVar()
        lvl_combobox = ttk.Combobox(self.frm1, textvariable=selected_level)
        lvl_combobox.grid(column=1, row=1)
        lvl_combobox['values'] = ('začátečník', 'středně pokročilý', 'pokročilý')
        lvl_combobox['state'] = 'readonly'

        ttk.Label(self.frm1, text="Vyberte část těla, kterou chcete posilovat").grid(column=1, row=2)

        # select body part combobox
        selected_bp_1 = tkinter.StringVar()
        bp_combobox = ttk.Combobox(self.frm1, textvariable=selected_bp_1)
        bp_combobox.grid(column=1, row=3)
        bp_combobox['values'] = values
        bp_combobox['state'] = 'readonly'

        # Button adding comboboxes
        self.adding_button = ttk.Button(self.frm1, text="Přidat více částí těla", command=self.generate_combobox)
        self.adding_button.grid(column=1, row=8)

        # Button switching to another frame
        self.switch_frame_button = ttk.Button(self.frm1, text='Použít')

        # initializing second and third bodypart combobox
        self.bp_combobox_2 = None
        self.selected_bp_2 = tkinter.StringVar()
        self.bp_combobox_3 = None
        self.selected_bp_3 = tkinter.StringVar()

        self.frm1.place(x=0, y=0)
        self.frm1.bind("<Configure>", self.place_frame_center)

    def place_frame_center(self, event):
        frame_width = self.frm1.winfo_reqwidth()
        frame_height = self.frm1.winfo_reqheight()

        x_pos = (self.screen_width - frame_width) // 2
        y_pos = (self.screen_height - frame_height) // 2

        self.frm1.place(x=x_pos, y=y_pos)

    def generate_combobox(self):
        if self.i == 0:
            self.i += 1
            ttk.Label(self.frm1, text='+', padding=5).grid(column=1, row=4)

            self.bp_combobox_2 = ttk.Combobox(self.frm1, textvariable=self.selected_bp_2)
            self.bp_combobox_2.grid(column=1, row=5)
            self.bp_combobox_2['values'] = values
            self.bp_combobox_2['state'] = 'readonly'
        elif self.i == 1:
            self.i += 1

            ttk.Label(self.frm1, text='+', padding=5).grid(column=1, row=6)

            self.bp_combobox_3 = ttk.Combobox(self.frm1, textvariable=self.selected_bp_3)
            self.bp_combobox_3.grid(column=1, row=7)
            self.bp_combobox_3['values'] = values
            self.bp_combobox_3['state'] = 'readonly'
            self.adding_button.destroy()


class Frame2:
    pass


def main():
    root = tk.Tk()
    gui = GUI(root)
    frame1 = Frame1(root, gui.screen_width, gui.screen_height)

    root.attributes('-fullscreen', True)
    root.mainloop()


if __name__ == "__main__":
    main()
