import tkinter
import tkinter as tk
from tkinter import ttk

# lepe umistit
values = ['', 'břicho', 'záda', 'paže', 'prsa', 'ramena', 'stehna', 'lýtka']

color = '#1D9A6C'
selected_font = 'Helvetica'

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = self
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # fulfilling the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window.geometry(f'{screen_width}x{screen_height}')

        # drasticky reseni
        #window.overrideredirect(1)

        self.frames = {}
        for F in (Frame1, Frame2, Frame3):
            page_name = F.__name__
            frame = F(master=self, parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='wsen')

        self.show_frame('Frame1')

    def show_frame(self, page_name):
        frm3 = self.frames['Frame3']
        frm3.tkraise()
        shown_frame = self.frames[page_name]
        shown_frame.tkraise()


class Frame1(tk.Frame):
    def __init__(self, master, parent, controller):
        self.master = master

        tk.Frame.__init__(self, parent)
        self.controller = controller
        switch_frame_button = ttk.Button(self, text='Použít', command=lambda: controller.show_frame('Frame2'))
        switch_frame_button.grid(column=1, row=9)

        # variable helping with combo boxes counting
        self.i = 0

        # monitor size
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        # background color
        self.config(bg=color)

        ttk.Label(self, background=color, font=selected_font, text="Vyberte obtížnost").grid(column=1, row=0)

        # select level combobox
        selected_level = tk.StringVar()
        lvl_combobox = ttk.Combobox(self, textvariable=selected_level)
        lvl_combobox.grid(column=1, row=1)
        lvl_combobox['values'] = ('začátečník', 'středně pokročilý', 'pokročilý')
        lvl_combobox['state'] = 'readonly'

        ttk.Label(self, background=color, font=selected_font, text="Vyberte část těla, kterou chcete posilovat").grid(column=1, row=2)

        # select body part combobox
        selected_bp_1 = tkinter.StringVar()
        bp_combobox = ttk.Combobox(self, textvariable=selected_bp_1,  style='Custom.TCombobox')
        bp_combobox.grid(column=1, row=3)
        bp_combobox['values'] = values
        bp_combobox['state'] = 'readonly'

        # Button adding comboboxes
        self.adding_button = ttk.Button(self, text="Přidat více částí těla", command=self.generate_combobox)
        self.adding_button.grid(column=1, row=8)

        # Button switching to another frame
        # self.switch_frame_button = ttk.Button(self.frm1, text='Použít')

        # initializing second and third bodypart combobox
        self.bp_combobox_2 = None
        self.selected_bp_2 = tkinter.StringVar()
        self.bp_combobox_3 = None
        self.selected_bp_3 = tkinter.StringVar()

        self.place(x=0, y=0)
        self.bind("<Configure>", self.place_frame_center)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TButton', font='Helvetica', background='grey')
        self.style.configure('Custom.TCombobox', foreground='red', background='green', font='MS comic sans')

    def place_frame_center(self, event):
        frame_width = self.winfo_reqwidth()
        frame_height = self.winfo_reqheight()

        x_pos = (self.screen_width - frame_width) // 2
        y_pos = (self.screen_height - frame_height) // 2

        self.place(x=x_pos, y=y_pos)

    def generate_combobox(self):
        if self.i == 0:
            self.i += 1
            ttk.Label(self, background=color, font=selected_font, text='+', padding=5).grid(column=1, row=4)

            self.bp_combobox_2 = ttk.Combobox(self, textvariable=self.selected_bp_2)
            self.bp_combobox_2.grid(column=1, row=5)
            self.bp_combobox_2['values'] = values
            self.bp_combobox_2['state'] = 'readonly'
        elif self.i == 1:
            self.i += 1

            ttk.Label(self, background=color, font=selected_font, text='+', padding=5).grid(column=1, row=6)

            self.bp_combobox_3 = ttk.Combobox(self, textvariable=self.selected_bp_3)
            self.bp_combobox_3.grid(column=1, row=7)
            self.bp_combobox_3['values'] = values
            self.bp_combobox_3['state'] = 'readonly'
            self.adding_button.destroy()


class Frame2(tk.Frame):
    def __init__(self, master, parent, controller):
        self.master = master

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(bg='#722525')

        switch_frame_back_button = ttk.Button(self, text='Zpatky', command=lambda: controller.show_frame('Frame1'))
        switch_frame_back_button.grid(row=0, column=0)


class Frame3(tk.Frame):
    def __init__(self, master, parent, controller):
        self.master = master

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(bg=color)


def main():
    # root = tk.Tk()
    app = GUI()
    #root.attributes('-fullscreen', True)
    app.mainloop()


if __name__ == "__main__":
    main()
