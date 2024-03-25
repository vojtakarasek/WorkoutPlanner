import customtkinter as ctk


text_color = 'white'
frame_color = '#6600ff'
border_color = '#350085'


class WorkoutScreen(ctk.CTkFrame):
    def __init__(self, master, parent, controller):
        self.workout = None
        self.master = master

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.color = '#070f1c'
        self.configure(fg_color=self.color)

        #font
        self.screen_width = self.master.winfo_screenwidth()
        self.font = int(self.screen_width * (3/128))
        self.selected_font = ('Helvetica', self.font)

        switch_frame_back_button = ctk.CTkButton(self, text='Zpátky',
                                                 command=lambda: controller.show_frame('InputScreen'),
                                                 font=('Helvetica', int(self.font/2)), fg_color=frame_color, hover_color=border_color)
        switch_frame_back_button.place(x=0, y=0)

        self.click_bindings = []
        self.enter_bindings = []
        self.leave_bindings = []
        self.drawn_exercises = []
        self.drawn_repetitions = []

        self.is_drawn = False

        self.exercises_frame = None
        self.repetitions_frame = None

    def frames(self):
        self.exercises_frame = ctk.CTkFrame(self, fg_color=frame_color, border_width=10, border_color=border_color)
        self.exercises_frame.pack(side='left', expand=True)
        self.repetitions_frame = ctk.CTkFrame(self, fg_color=frame_color, border_width=10, border_color=border_color)
        self.repetitions_frame.pack(side='right', expand=True)

    def set_workout(self, workout):
        self.workout = workout

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

            self.exercises_frame.destroy()
            self.repetitions_frame.destroy()

        self.frames()

        label_exercises = ctk.CTkLabel(self.exercises_frame, text='CVIKY', text_color=text_color,
                                       font=self.selected_font)
        label_exercises.pack(side="top", expand=True, pady=30)

        label_repetitions = ctk.CTkLabel(self.repetitions_frame, text='OPAKOVÁNÍ', text_color=text_color,
                                         font=self.selected_font)
        label_repetitions.pack(side='top', expand=True, pady=30, padx=30)
        # initializing labels
        for i in range(8):
            exercise = ctk.CTkLabel(self.exercises_frame, text=self.workout[i].name, text_color=text_color,
                                    font=self.selected_font)
            exercise.pack(side='top', expand=True, anchor='w', padx=35, pady=15)
            self.drawn_exercises.append(exercise)

            repetition = ctk.CTkLabel(self.repetitions_frame,
                                      text=f'{self.workout[i].series}x{self.workout[i].repetitions}',
                                      text_color=text_color, font=self.selected_font)
            repetition.pack(side='top', expand=True, anchor='center', padx=35, pady=15)
            self.drawn_repetitions.append(repetition)

        for label, i in zip(self.drawn_exercises, range(8)):
            click_binding = label.bind("<Button-1>", lambda event, value=i: self.on_click(event, value))
            enter_binding = label.bind("<Enter>", lambda event, value=i: self.on_enter(event, value))
            leave_binding = label.bind("<Leave>", lambda event, value=i: self.on_leave(event, value))
            self.click_bindings.append(click_binding)
            self.enter_bindings.append(enter_binding)
            self.leave_bindings.append(leave_binding)

        self.is_drawn = True

    def resize_frames(self):
        exercises_frame_height = self.exercises_frame.winfo_reqheight()
        self.exercises_frame.configure(height=exercises_frame_height + 30)

        reps_frame_height = self.exercises_frame.winfo_reqheight()
        self.repetitions_frame.configure(height=reps_frame_height + 30)

    def on_enter(self, event, value):
        self.exercises_frame.pack_propagate(False)
        self.repetitions_frame.pack_propagate(False)
        self.drawn_exercises[value].configure(font=('Helvetica', self.font - 2, 'bold'), text_color='grey')
        self.drawn_repetitions[value].configure(font=('Helvetica', self.font - 2, 'bold'), text_color='grey')

    def on_leave(self, event, value):
        self.drawn_exercises[value].configure(font=self.selected_font, text_color=text_color)
        self.drawn_repetitions[value].configure(font=self.selected_font, text_color=text_color)

    def on_click(self, event, value):
        self.controller.show_toplevel(self.workout[value])
