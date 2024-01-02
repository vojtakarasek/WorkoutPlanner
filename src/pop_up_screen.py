import tkinter as tk
from tkinter import ttk
from tkVideoPlayer import TkinterVideo


class PopUpScreen(tk.Frame):
    def __init__(self, master, parent, controller):
        self.exercise = None
        self.drawn_labels = []
        self.master = master
        self.group_list = ('Název:','Popis:','Partie:','Obtížnost:','Počet sérii:','Počet opakování:')
        self.values = ()
        self.videoplayer = None

        tk.Frame.__init__(self, parent)
        self.controller = controller

        exit_button = ttk.Button(self, text='Exit', command=self.exit_button)
        #exit_button.grid(row=0, column=1, sticky='n')
        exit_button.pack(side='right')
        self.config(bg='black')

        # monitor size
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.place(x=0, y=0)
        self.bind("<Configure>", self.place_frame_center)

        self.style = ttk.Style()
        self.style.configure('Custom1.TLabel', font=('Helvetica', 40),foreground='white', background='black')

        self.video_frame = tk.Frame(self, bg='green')
        self.video_frame.config(width=1000, height=500)
        self.video_frame.pack(side='top', expand=True)
        self.video_frame.pack_propagate(False)

    def place_frame_center(self, event):
        frame_width = self.winfo_reqwidth()
        frame_height = self.winfo_reqheight()

        x_pos = (self.screen_width - frame_width) // 2
        y_pos = (self.screen_height - frame_height) // 2

        self.place(x=x_pos, y=y_pos)

    def set_exercise(self, exercise):
        self.exercise = exercise
        self.values = (exercise.name, exercise.description, exercise.body_part, exercise.level, exercise.series,
                       exercise.repetitions)
        n = 1

        self.videoplayer = TkinterVideo(master=self.video_frame, scaled=True)
        self.videoplayer.load(exercise.video)
        self.videoplayer.pack(expand=True, fill='both')
        self.videoplayer.play()

        for group in zip(self.group_list, self.values):
            label = ttk.Label(self, text=f'{group[0]} {group[1]}', style='Custom1.TLabel')
            label.pack(side='top')
            self.drawn_labels.append(label)
            n += 1

    def exit_button(self):
        for label in self.drawn_labels:
            label.destroy()

        self.videoplayer.destroy()

        self.controller.show_frame('WorkoutScreen')






