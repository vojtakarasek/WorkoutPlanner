from tkVideoPlayer import TkinterVideo
import customtkinter as ctk

selected_font = ('Helvetica', 30)


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.video_frame = None
        self.videoplayer = None
        self.values = ()
        self.exercise = None
        self.group_list = ('Název:', 'Partie:', 'Obtížnost:', 'Počet sérii:', 'Počet opakování:')
        self.drawn_labels = []

        # monitor size
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.geometry(f'{int((self.screen_width / 2) + 50)}x{int((self.screen_height / 2) + 95)}')

        self.segmented_button = ctk.CTkSegmentedButton(self, values=['Video', 'Popis'],
                                                       font=('Helvetica', 20),
                                                       command=self.segmented_button_callback, height=30)
        self.segmented_button.pack(side='top', pady=20)

        self.label = ctk.CTkLabel(self, text='Zvolte jednu z možností', font=('Helvetica', 50))
        self.label.place(x=400, y=320)

        self.bind("<Configure>", self.initialize())

    def check_if_the_clicked_exercise_is_open(self, name):
        if name == self.exercise.name:
            pass
        else:
            self.initialize()

    def pass_values(self, exercise):
        self.exercise = exercise
        self.values = (exercise.name, exercise.body_part, exercise.level, exercise.series,
                       exercise.repetitions)

        self.title(self.exercise.name)

    def initialize(self):
        self.destroy()


    def segmented_button_callback(self, value):
        if value == 'Video':
            self.video_player()

        elif value == 'Popis':
            self.details_table()

    def video_player(self):
        if len(self.drawn_labels) > 0:
            for label in self.drawn_labels:
                label.destroy()
        self.label.destroy()

        self.video_frame = ctk.CTkFrame(self, fg_color='green')
        self.video_frame.configure(width=self.screen_width / 2, height=self.screen_height / 2)
        self.video_frame.pack_propagate(False)
        self.video_frame.pack(side='top', pady=10)

        self.videoplayer = TkinterVideo(master=self.video_frame, scaled=True)
        self.videoplayer.load(self.exercise.video)
        self.videoplayer.pack(expand=True, fill='both')
        self.videoplayer.play()
        self.videoplayer.bind("<<Ended>>", self.video_restart)

    def video_restart(self, event):
        self.videoplayer.pause()
        self.videoplayer.seek(0)
        self.videoplayer.play()

    def details_table(self):
        if self.videoplayer is not None:
            self.videoplayer.destroy()
            self.video_frame.destroy()
        self.label.destroy()

        for group in zip(self.group_list, self.values):
            label = ctk.CTkLabel(self, text=f'{group[0]} {group[1]}', font=selected_font)
            label.pack(side='top', anchor='w')
            self.drawn_labels.append(label)

        popis_label = ctk.CTkLabel(self, text=f'Popis:', font=selected_font)
        popis_label.pack(side='top', anchor='w')
        self.drawn_labels.append(popis_label)

        description_sentences = self.exercise.description.split(". ")

        # each split sentence has its own line, so it fits on screen
        for sentence in description_sentences:
            description_label = ctk.CTkLabel(self, text=f'{sentence}', font=selected_font)
            description_label.pack(side='top', anchor='w')
            self.drawn_labels.append(description_label)
