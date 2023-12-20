import tkinter as tk
from starting_screen import color


class Frame3(tk.Frame):
    def __init__(self, master, parent, controller):
        self.master = master

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(bg=color)
