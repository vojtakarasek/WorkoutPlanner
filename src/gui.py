import tkinter as tk

from src.user_requirements import UserRequirements
from src.workout_planner import WorkoutPlanner
from input_screen import InputScreen
from workout_screen import WorkoutScreen
from background_screen import BackgroundScreen
from pop_up_screen import PopUpScreen


class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.exercises_count = 8

        window = self
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # fulfilling the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window.geometry(f'{screen_width}x{screen_height}')

        self.frames = {}
        for F in (InputScreen, WorkoutScreen, BackgroundScreen, PopUpScreen):
            page_name = F.__name__
            frame = F(master=self, parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='wsen')

        self.show_frame('InputScreen')
        self.planner = None

    def use_planner(self, planner: WorkoutPlanner):
        self.planner = planner

    def show_frame(self, page_name):
        frm3 = self.frames['BackgroundScreen']
        frm3.tkraise()
        shown_frame = self.frames[page_name]
        shown_frame.tkraise()

    def plan_and_show_workout(self, user_req: UserRequirements):
        # zavola planner
        workout = self.planner.create_plan(user_req, self.exercises_count)
        # Frame2 preda vysledek z planneru
        workout_screen = self.frames['WorkoutScreen']
        workout_screen.set_workout(workout)
        self.show_frame('WorkoutScreen')

    def show_pop_up(self, exercise):
        pop_up = self.frames['PopUpScreen']
        pop_up.set_exercise(exercise)
        self.show_frame('PopUpScreen')
