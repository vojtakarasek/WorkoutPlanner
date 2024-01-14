import tkinter as tk
from tkinter import ttk
from tkVideoPlayer import TkinterVideo


class PopUpScreen(tk.Frame):
    def __init__(self, master, parent, controller):
        self.exercise = None
        self.drawn_labels = []
        self.master = master
        self.group_list = ('Název:', 'Partie:', 'Obtížnost:', 'Počet sérii:', 'Počet opakování:')
        self.values = ()
        self.videoplayer = None

        tk.Frame.__init__(self, parent)
        self.controller = controller

        exit_button = ttk.Button(self, text='Exit', command=self.exit_button)
        exit_button.place(x=0, y=0)
        self.config(bg='black')

        self.font = 30
        self.color = 'black'

        # monitor size
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.style = ttk.Style()
        self.style.configure('Custom1.TLabel', font=('Helvetica', self.font), foreground='white', background=self.color)
        self.style.configure('Custom2.TLabel', font=('Helvetica', self.font), foreground='white', background=self.color)

        self.video_frame = tk.Frame(self, bg='green')
        self.video_frame.config(width=self.screen_width / 2, height=self.screen_height / 2)
        self.video_frame.pack(side='top')
        self.video_frame.pack_propagate(False)

        self.details_frame = tk.Frame(self, bg=self.color)
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
            label = ttk.Label(self.details_frame, text=f'{group[0]} {group[1]}', style='Custom1.TLabel')
            label.pack(side='top', anchor='w')
            self.drawn_labels.append(label)
            n += 1

        popis_label = ttk.Label(self.details_frame, text=f'Popis:', style='Custom2.TLabel')
        popis_label.pack(side='top', anchor='w')
        self.drawn_labels.append(popis_label)
        # list of split description string
        description_sentences = exercise.description.split(". ")

        # each split sentence has its own line, so it fits on screen
        for sentence in description_sentences:
            description_label = ttk.Label(self.details_frame, text=f'{sentence}', style='Custom2.TLabel')
            description_label.pack(side='top', anchor='w', padx=50)
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
