import tkinter as tk
from tkinter import ttk
from input_screen import selected_font


class WorkoutScreen(tk.Frame):
    def __init__(self, master, parent, controller):
        self.master = master

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.color = '#DEEAFF'
        self.config(bg=self.color)

        switch_frame_back_button = ttk.Button(self, text='Zpatky', command=lambda: controller.show_frame('InputScreen'), style='Custom.TButton')
        switch_frame_back_button.pack(side="bottom", expand=True)

        self.style = ttk.Style(self)
        self.style.configure('Custom.TButton', font='Helvetica', background=self.color)
        self.style.configure('TLabel', font=('Helvetica', 50, 'bold'), background=self.color)

        self.workout = None

    def set_workout(self, workout):
        self.workout = workout
        self.style.configure('Custom.TLabel', font=('Helvetica', 50, 'bold'), background='red')

        first_exercise = ttk.Label(self, text=self.workout[0].name)
        first_exercise.pack(side="top", expand=True)

        second_exercise = ttk.Label(self, text=self.workout[1].name)
        second_exercise.pack(side="top", expand=True)

        third_exercise = ttk.Label(self, text=self.workout[2].name, style='Custom.TLabel')
        third_exercise.pack(side="top", expand=True)

        fourth_exercise = ttk.Label(self, text=self.workout[3].name)
        fourth_exercise.pack(side="top", expand=True)

        fifth_exercise = ttk.Label(self, text=self.workout[4].name)
        fifth_exercise.pack(side="top", expand=True)

        sixth_exercise = ttk.Label(self, text=self.workout[5].name)
        sixth_exercise.pack(side="top", expand=True)

        seventh_exercise = ttk.Label(self, text=self.workout[6].name)
        seventh_exercise.pack(side="top", expand=True)

        eight_exercise = ttk.Label(self, text=self.workout[7].name)
        eight_exercise.pack(side="top", expand=True)
