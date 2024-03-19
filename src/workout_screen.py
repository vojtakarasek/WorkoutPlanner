import customtkinter as ctk

selected_font = ('Helvetica', 60)


class WorkoutScreen(ctk.CTkFrame):
    def __init__(self, master, parent, controller):
        self.workout = None
        self.master = master

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.color = '#DEEAFF'
        self.configure(fg_color=self.color)
        self.font = 60

        switch_frame_back_button = ctk.CTkButton(self, text='Zpátky',
                                                 command=lambda: controller.show_frame('InputScreen'),
                                                 font=('Helvetica', 30))
        switch_frame_back_button.place(x=0, y=0)

        self.click_bindings = []
        self.enter_bindings = []
        self.leave_bindings = []
        self.drawn_exercises = []
        self.drawn_repetitions = []

        self.is_drawn = False

        self.exercises_frame = ctk.CTkFrame(self, fg_color=self.color)
        self.exercises_frame.pack(side='left', expand=True)
        self.repetitions_frame = ctk.CTkFrame(self, fg_color=self.color)
        self.repetitions_frame.pack(side='right', expand=True)

        self.Label_exercises = ctk.CTkLabel(self.exercises_frame, text='CVIKY', text_color='black', font=selected_font)
        self.Label_exercises.pack(side="top", expand=True)

        self.Label_repetitions = ctk.CTkLabel(self.repetitions_frame, text='OPAKOVÁNÍ', text_color='black',
                                              font=selected_font)
        self.Label_repetitions.pack(side='top', expand=True)

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

        # initializing labels
        for i in range(8):
            exercise = ctk.CTkLabel(self.exercises_frame, text=self.workout[i].name, text_color='black',
                                    font=selected_font)
            exercise.pack(side='top', expand=True, anchor='w')
            self.drawn_exercises.append(exercise)

            repetition = ctk.CTkLabel(self.repetitions_frame,
                                      text=f'{self.workout[i].series}x{self.workout[i].repetitions}',
                                      text_color='black', font=selected_font)
            repetition.pack(side='top', expand=True, anchor='center')
            self.drawn_repetitions.append(repetition)

        for label, i in zip(self.drawn_exercises, range(8)):
            click_binding = label.bind("<Button-1>", lambda event, value=i: self.on_click(event, value))
            enter_binding = label.bind("<Enter>", lambda event, value=i: self.on_enter(event, value))
            leave_binding = label.bind("<Leave>", lambda event, value=i: self.on_leave(event, value))
            self.click_bindings.append(click_binding)
            self.enter_bindings.append(enter_binding)
            self.leave_bindings.append(leave_binding)

        self.is_drawn = True

    def on_enter(self, event, value):
        self.exercises_frame.pack_propagate(False)
        self.repetitions_frame.pack_propagate(False)
        self.drawn_exercises[value].configure(font=('Helvetica', self.font - 2, 'bold'), text_color='grey')
        self.drawn_repetitions[value].configure(font=('Helvetica', self.font - 2, 'bold'), text_color='grey')

    def on_leave(self, event, value):
        self.drawn_exercises[value].configure(font=selected_font, text_color='black')
        self.drawn_repetitions[value].configure(font=selected_font, text_color='black')

    def on_click(self, event, value):
        self.controller.show_toplevel(self.workout[value])



