import tkinter as tk
from tkinter import ttk
from starting_screen import Frame1
from main_screen import Frame2
from filler_screen import Frame3


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


def main():
    # root = tk.Tk()
    app = GUI()
    #root.attributes('-fullscreen', True)
    app.mainloop()


if __name__ == "__main__":
    main()
