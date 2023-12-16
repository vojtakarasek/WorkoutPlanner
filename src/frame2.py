import tkinter as tk
from tkinter import ttk
from frame1 import selected_font

color = '#722525'


class Frame2(tk.Frame):
    def __init__(self, master, parent, controller):
        self.master = master

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(bg=color)

        switch_frame_back_button = ttk.Button(self, text='Zpatky', style='Custom.TButton', command=lambda: controller.show_frame('Frame1'))
        switch_frame_back_button.grid(row=0, column=0)

        self.style = ttk.Style(self)
        self.style.configure('Custom.TButton', font='Helvetica', background=color)
