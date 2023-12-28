import tkinter as tk
from tkinter import ttk
from user_requirements import UserRequirements

values = ['', 'břicho', 'záda', 'paže', 'prsa', 'ramena', 'stehna', 'lýtka']

color = '#A6A3E5'
selected_font = 'Helvetica'


class InputScreen(tk.Frame):
    def __init__(self, master, parent, controller):
        self.master = master

        tk.Frame.__init__(self, parent)
        self.controller = controller
        switch_frame_button = ttk.Button(self, text='Naplánovat', command=self.on_planning_clicked)
        switch_frame_button.grid(column=1, row=9, sticky='nsew')

        # variable helping with combo boxes counting
        self.i = 0

        # monitor size
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        # background color
        self.config(bg=color)

        ttk.Label(self, background=color, font=selected_font, text="Vyberte obtížnost").grid(column=1, row=0)

        # select level combobox
        self.selected_level = tk.StringVar()
        lvl_combobox = ttk.Combobox(self, textvariable=self.selected_level)
        lvl_combobox.grid(column=1, row=1, sticky='nsew')
        lvl_combobox['values'] = ('začátečník', 'středně pokročilý', 'pokročilý')
        lvl_combobox['state'] = 'readonly'

        ttk.Label(self, background=color, font=selected_font, text="Vyberte část těla, kterou chcete posilovat").grid(
            column=1, row=2)

        # select body part combobox
        self.selected_bp_1 = tk.StringVar()
        bp_combobox = ttk.Combobox(self, textvariable=self.selected_bp_1)
        bp_combobox.grid(column=1, row=3, sticky='nsew')
        bp_combobox['values'] = values
        bp_combobox['state'] = 'readonly'

        # Button adding comboboxes
        self.adding_button = ttk.Button(self, text="Přidat více částí těla", command=self.generate_combobox)
        self.adding_button.grid(column=1, row=8, sticky='nsew')

        # Button switching to another frame
        # self.switch_frame_button = ttk.Button(self.frm1, text='Použít')

        # initializing second and third bodypart combobox
        self.bp_combobox_2 = None
        self.selected_bp_2 = tk.StringVar()
        self.bp_combobox_3 = None
        self.selected_bp_3 = tk.StringVar()

        self.place(x=0, y=0)
        self.bind("<Configure>", self.place_frame_center)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TButton', font='Helvetica', background=color)
        self.style.configure('CustomTLabel', font=(selected_font, 30), background=color)

        self.user_requirements = UserRequirements(self)

    def place_frame_center(self, event):
        frame_width = self.winfo_reqwidth()
        frame_height = self.winfo_reqheight()

        x_pos = (self.screen_width - frame_width) // 2
        y_pos = (self.screen_height - frame_height) // 2

        self.place(x=x_pos, y=y_pos)

    def generate_combobox(self):
        if self.i == 0:
            self.i += 1
            ttk.Label(self, background=color, font=selected_font, text='+', padding=5).grid(column=1, row=4)

            self.bp_combobox_2 = ttk.Combobox(self, textvariable=self.selected_bp_2)
            self.bp_combobox_2.grid(column=1, row=5, sticky='nsew')
            self.bp_combobox_2['values'] = values
            self.bp_combobox_2['state'] = 'readonly'
        elif self.i == 1:
            self.i += 1

            ttk.Label(self, background=color, font=selected_font, text='+', padding=5).grid(column=1, row=6)

            self.bp_combobox_3 = ttk.Combobox(self, textvariable=self.selected_bp_3)
            self.bp_combobox_3.grid(column=1, row=7, sticky='nsew')
            self.bp_combobox_3['values'] = values
            self.bp_combobox_3['state'] = 'readonly'
            self.adding_button.destroy()

    def combobox_variables_bp(self):
        selected_variable_1 = self.selected_bp_1.get()
        selected_variable_2 = self.selected_bp_2.get()
        selected_variable_3 = self.selected_bp_3.get()
        selected_variables_bp = [selected_variable_1, selected_variable_2, selected_variable_3]
        return selected_variables_bp

    def combobox_variables_lvl(self):
        selected_variables_lvl = self.selected_level.get()
        return selected_variables_lvl

    def on_planning_clicked(self):
        reqs = self.user_requirements.body_part_reqs()
        self.controller.plan_and_show_workout(reqs)
