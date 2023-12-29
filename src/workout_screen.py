import tkinter as tk
from tkinter import ttk
from pop_up_screen import PopUpScreen
from input_screen import selected_font


class WorkoutScreen(tk.Frame):
    def __init__(self, master, parent, controller):
        self.workout = None
        self.master = master

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.color = '#DEEAFF'
        self.config(bg=self.color)

        switch_frame_back_button = ttk.Button(self, text='Zpatky', command=lambda: controller.show_frame('InputScreen'), style='Custom.TButton')
        switch_frame_back_button.pack(side="bottom", expand=True)

        self.style = ttk.Style(self)
        self.style.configure('Custom.TButton', font='Helvetica', background=self.color)
        self.style.configure('TLabel', font=('Helvetica', 40, 'bold'), background=self.color, anchor="e")

        self.click_bindings = []
        self.enter_bindings = []
        self.leave_bindings = []
        self.drawn_exercises = []
        self.drawn_repetitions = []

        self.is_drawn = False

        self.Label = ttk.Label(self, text='CVIKY', style='Custom.TLabel')
        self.Label.pack(side="top", expand=True)

    def set_workout(self, workout):
        self.workout = workout
        self.style.configure('Custom.TLabel', font=('Helvetica', 40, 'bold'), background='red')

        if self.is_drawn:
            for exercise, click_binding, enter_binding, leave_binding in zip(self.drawn_exercises, self.click_bindings,
                                                                             self.enter_bindings, self.leave_bindings):
                if exercise.winfo_exists():
                    exercise.unbind("<Button-1>", click_binding)
                    exercise.unbind("<Enter>", enter_binding)
                    exercise.unbind("<Leave>", leave_binding)

            self.click_bindings = []
            self.enter_bindings = []
            self.leave_bindings = []

            for i in zip(self.drawn_exercises, self.drawn_repetitions):
                for j in range(2):
                    i[j].destroy()

            self.drawn_exercises = []
            self.drawn_repetitions = []

        self.exercise_1 = ttk.Label(self, text=self.workout[0].name)
        self.exercise_1.pack(side="top", expand=True)
        self.exercise_1_reps = ttk.Label(self, text=f'{self.workout[0].series}x{self.workout[0].repetitions}')
        self.exercise_1_reps.pack(side="top", expand=True)
        self.drawn_exercises.append(self.exercise_1)
        self.drawn_repetitions.append(self.exercise_1_reps)

        self.exercise_2 = ttk.Label(self, text=self.workout[1].name)
        self.exercise_2.pack(side="top", expand=True)
        self.exercise_2_reps = ttk.Label(self, text=f'{self.workout[1].series}x{self.workout[1].repetitions}')
        self.exercise_2_reps.pack(side="top", expand=True)
        self.drawn_exercises.append(self.exercise_2)
        self.drawn_repetitions.append(self.exercise_2_reps)

        self.exercise_3 = ttk.Label(self, text=self.workout[2].name, style='Custom.TLabel')
        self.exercise_3.pack(side="top", expand=True)
        self.exercise_3_reps = ttk.Label(self, text=f'{self.workout[2].series}x{self.workout[2].repetitions}')
        self.exercise_3_reps.pack(side="top", expand=True)
        self.drawn_exercises.append(self.exercise_3)
        self.drawn_repetitions.append(self.exercise_3_reps)

        self.exercise_4 = ttk.Label(self, text=self.workout[3].name)
        self.exercise_4.pack(side="top", expand=True)
        self.exercise_4_reps = ttk.Label(self, text=f'{self.workout[3].series}x{self.workout[3].repetitions}')
        self.exercise_4_reps.pack(side="top", expand=True)
        self.drawn_exercises.append(self.exercise_4)
        self.drawn_repetitions.append(self.exercise_4_reps)

        self.exercise_5 = ttk.Label(self, text=self.workout[4].name)
        self.exercise_5.pack(side="top", expand=True)
        self.exercise_5_reps = ttk.Label(self, text=f'{self.workout[5].series}x{self.workout[5].repetitions}')
        self.exercise_5_reps.pack(side="top", expand=True)
        self.drawn_exercises.append(self.exercise_5)
        self.drawn_repetitions.append(self.exercise_5_reps)

        self.exercise_6 = ttk.Label(self, text=self.workout[5].name)
        self.exercise_6.pack(side="top", expand=True)
        self.exercise_6_reps = ttk.Label(self, text=f'{self.workout[5].series}x{self.workout[5].repetitions}')
        self.exercise_6_reps.pack(side="top", expand=True)
        self.drawn_exercises.append(self.exercise_6)
        self.drawn_repetitions.append(self.exercise_6_reps)

        self.exercise_7 = ttk.Label(self, text=self.workout[6].name)
        self.exercise_7.pack(side="top", expand=True)
        self.exercise_7_reps = ttk.Label(self, text=f'{self.workout[6].series}x{self.workout[6].repetitions}')
        self.exercise_7_reps.pack(side="top", expand=True)
        self.drawn_exercises.append(self.exercise_7)
        self.drawn_repetitions.append(self.exercise_7_reps)

        self.exercise_8 = ttk.Label(self, text=self.workout[7].name)
        self.exercise_8.pack(side="top", expand=True)
        self.exercise_8_reps = ttk.Label(self, text=f'{self.workout[7].series}x{self.workout[7].repetitions}')
        self.exercise_8_reps.pack(side="top", expand=True)
        self.drawn_exercises.append(self.exercise_8)
        self.drawn_repetitions.append(self.exercise_8_reps)

        for label, i in zip(self.drawn_exercises, range(8)):
            click_binding = label.bind("<Button-1>", lambda event, value=i: self.on_click(event, value))
            enter_binding = label.bind("<Enter>", lambda event, value=i: self.on_enter(event, value))
            leave_binding = label.bind("<Leave>", lambda event, value=i: self.on_leave(event, value))
            self.click_bindings.append(click_binding)
            self.enter_bindings.append(enter_binding)
            self.leave_bindings.append(leave_binding)

        self.is_drawn = True

    def on_enter(self, event, value):
        self.drawn_exercises[value].config(font=('Helvetica', 38, 'bold'), foreground='grey')

    def on_leave(self, event, value):
        self.drawn_exercises[value].config(font=('Helvetica', 40, 'bold'), foreground='black')

    def on_click(self, event, value):
        self.controller.show_pop_up(self.workout[value])





