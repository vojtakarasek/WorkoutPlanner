import tkinter as tk
from tkinter import ttk
from tkVideoPlayer import TkinterVideo
import customtkinter as ctk

selected_font = ('Helvetica', 30)


class PopUpScreen(ctk.CTkFrame):
    def __init__(self, master, parent, controller):
        self.exercise = None
        self.drawn_labels = []
        self.master = master
        self.group_list = ('Název:', 'Partie:', 'Obtížnost:', 'Počet sérii:', 'Počet opakování:')
        self.values = ()
        self.videoplayer = None

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        exit_button = ctk.CTkButton(self, text='Exit', command=self.exit_button, font=selected_font)
        exit_button.place(x=0, y=0)
        self.configure(fg_color='black')

        self.font = 30
        self.color = 'black'

        # monitor size
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.video_frame = ctk.CTkFrame(self, fg_color='green')
        self.video_frame.configure(width=self.screen_width / 2, height=self.screen_height / 2)
        self.video_frame.pack(side='top')
        self.video_frame.pack_propagate(False)

        self.details_frame = ctk.CTkFrame(self, fg_color='grey')#, border_color='green', corner_radius=10000)
        self.details_frame.pack(side='top')

    def set_exercise(self, exercise):
        self.exercise = exercise
        self.values = (exercise.name, exercise.body_part, exercise.level, exercise.series,
                       exercise.repetitions)
        n = 1

        self.videoplayer = TkinterVideo(master=self.video_frame, scaled=True)
        self.videoplayer.load(exercise.video)
        self.videoplayer.pack(expand=True, fill='both')
        self.videoplayer.play()
        self.videoplayer.bind("<<Ended>>", self.video_restart)

        for group in zip(self.group_list, self.values):
            label = ctk.CTkLabel(self.details_frame, text=f'{group[0]} {group[1]}', font=selected_font)
            label.pack(side='top', anchor='w')
            self.drawn_labels.append(label)
            n += 1

        popis_label = ctk.CTkLabel(self.details_frame, text=f'Popis:', font=selected_font)
        popis_label.pack(side='top', anchor='w')
        self.drawn_labels.append(popis_label)

        # list of split description string
        description_sentences = exercise.description.split(". ")

        # each split sentence has its own line, so it fits on screen
        for sentence in description_sentences:
            description_label = ctk.CTkLabel(self.details_frame, text=f'{sentence}', font=selected_font)
            description_label.pack(side='top', anchor='w')
            self.drawn_labels.append(description_label)

    def exit_button(self):
        for label in self.drawn_labels:
            label.destroy()

        self.videoplayer.destroy()

        self.controller.show_frame('WorkoutScreen')

    def video_restart(self, event):
        self.videoplayer.pause()
        self.videoplayer.seek(0)
        self.videoplayer.play()
