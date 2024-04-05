from tkVideoPlayer import TkinterVideo
import customtkinter as ctk


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ctk.set_appearance_mode("dark")

        self.video_frame = None
        self.videoplayer = None
        self.values = ()
        self.exercise = None
        self.group_list = ('Název:', 'Partie:', 'Obtížnost:', 'Počet sérii:', 'Počet opakování:')
        self.drawn_labels = []
        # monitor size
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.font = int(self.screen_width * (3 / 256))
        self.selected_font = ('Helvetica', self.font)

        self.geometry(f'{int((self.screen_width / 2) + 50)}x{int((self.screen_height / 2) + 95)}')

        self.segmented_button = ctk.CTkSegmentedButton(self, values=['Video', 'Popis'],
                                                       font=('Helvetica', 20),
                                                       command=self.segmented_button_callback, height=30,
                                                       selected_color='#6600ff', unselected_color='#350085',
                                                       fg_color='#350085', selected_hover_color='#6600ff',
                                                       unselected_hover_color='#6600ff')
        self.segmented_button.pack(side='top', pady=20)
        self.segmented_button.set('Video')

        self.bind("<Configure>", self.focus_window)

    def focus_window(self, event):
        self.focus()

    def check_if_the_clicked_exercise_is_open(self, name):
        if name == self.exercise.name:
            pass
        else:
            self.destroy_existing_exercise()

    def destroy_existing_exercise(self):
        if self.videoplayer is not None:
            self.videoplayer.destroy()
            self.video_frame.destroy()
            self.videoplayer = None

        if len(self.drawn_labels) > 0:
            for label in self.drawn_labels:
                label.destroy()
            self.drawn_labels = []

    def pass_values(self, exercise):
        self.exercise = exercise
        self.values = (exercise.name, exercise.body_part, exercise.level, exercise.series,
                       exercise.repetitions)

        self.initialize_window()

    def initialize_window(self):
        self.title(self.exercise.name)

        value = self.segmented_button.get()
        if self.videoplayer is None and len(self.drawn_labels) == 0:
            if value == 'Video':
                self.play_video()

            elif value == 'Popis':
                self.details_table()

    def segmented_button_callback(self, value):
        if value == 'Video':
            self.play_video()

        elif value == 'Popis':
            self.details_table()

    def play_video(self):
        if len(self.drawn_labels) > 0:
            for label in self.drawn_labels:
                label.destroy()
            self.drawn_labels = []

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
            self.videoplayer = None

        for group in zip(self.group_list, self.values):
            label = ctk.CTkLabel(self, text=f'{group[0]} {group[1]}', font=self.selected_font)
            label.pack(side='top', anchor='w', padx=10)
            self.drawn_labels.append(label)

        popis_label = ctk.CTkLabel(self, text=f'Popis:', font=self.selected_font)
        popis_label.pack(side='top', anchor='w', padx=10)
        self.drawn_labels.append(popis_label)

        split_description = self.split_string(self.exercise.description)

        # each split sentence has its own line, so it fits on screen
        for sentence in split_description:
            description_label = ctk.CTkLabel(self, text=f'{sentence}', font=self.selected_font)
            description_label.pack(side='top', anchor='w', padx=10)
            self.drawn_labels.append(description_label)

    def split_string(self, string, chunk_size=90):
        chunks = []
        while len(string) > chunk_size:
            space_index = string.rfind(' ', 0, chunk_size)
            if space_index == -1:  # If no space found within the chunk size
                space_index = chunk_size
            chunks.append(string[:space_index])
            string = string[space_index + 1:]
        if string:
            chunks.append(string)
        return chunks
