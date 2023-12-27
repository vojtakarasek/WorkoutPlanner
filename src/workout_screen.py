import tkinter as tk
from tkinter import ttk
from input_screen import selected_font

color = '#DEEAFF'


class WorkoutScreen(tk.Frame):
    def __init__(self, master, parent, controller):
        self.master = master

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(bg=color)

        switch_frame_back_button = ttk.Button(self, text='Zpatky', command=lambda: controller.show_frame('InputScreen'), style='Custom.TButton')
        switch_frame_back_button.grid(row=0, column=0)

        self.style = ttk.Style(self)
        self.style.configure('Custom.TButton', font='Helvetica', background=color)

        self.workout = None

    def set_workout(self, workout):
        self.workout = workout
