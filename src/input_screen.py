import tkinter as tk
import customtkinter as ctk

from src.level_enum import Level
from user_requirements import UserRequirements
from body_part_enum import BodyPart

values = ['', 'břicho', 'záda', 'paže', 'prsa', 'ramena', 'stehna', 'lýtka']

color = '#A6A3E5'
selected_font = ('Helvetica', 30)


class InputScreen(ctk.CTkFrame):
    def __init__(self, master, parent, controller):
        self.master = master

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.pack()
        self.pack_propagate(True)
        switch_frame_button = ctk.CTkButton(self, text='Naplánovat', command=self.on_planning_clicked, font=selected_font)
        switch_frame_button.grid(column=1, row=9, sticky='nsew')

        # variable helping with combo boxes counting
        self.i = 0

        # monitor size
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        # background color
        self.configure(fg_color='dark grey')

        ctk.CTkLabel(self, font=selected_font, text="Vyberte obtížnost", width=666).grid(column=1, row=0)

        # select level combobox
        self.selected_level = tk.StringVar()
        lvl_combobox = ctk.CTkComboBox(self, variable=self.selected_level, values=['začátečník', 'středně pokročilý',
                                                                                   'pokročilý'], state='readonly',
                                       font=selected_font, dropdown_font=selected_font, dropdown_fg_color='white',
                                       dropdown_text_color='black', justify='center')
        lvl_combobox.grid(column=1, row=1, sticky='nsew')

        ctk.CTkLabel(self, font=selected_font, text="Vyberte část těla, kterou chcete posilovat").grid(
            column=1, row=2)

        # select body part combobox
        self.selected_bp_1 = tk.StringVar()
        bp_combobox = ctk.CTkComboBox(self, variable=self.selected_bp_1, values=values, state='readonly',
                                      font=selected_font, dropdown_font=selected_font, dropdown_fg_color='white',
                                      dropdown_text_color='black', justify='center')
        bp_combobox.grid(column=1, row=3, sticky='nsew')
        bp_combobox['values'] = values
        bp_combobox['state'] = 'readonly'

        # Button adding comboboxes
        self.adding_button = ctk.CTkButton(self, text="Přidat více částí těla", command=self.generate_combobox, font=selected_font)
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
        #self.style = ttk.Style(self)
        #self.style.configure('TButton', font='Helvetica', background=color)
        #self.style.configure('CustomTLabel', font=(selected_font, 30), background=color)

    def place_frame_center(self, event):
        frame_width = self.winfo_reqwidth()
        frame_height = self.winfo_reqheight()

        x_pos = (self.screen_width - frame_width) // 2
        y_pos = (self.screen_height - frame_height) // 2

        self.place(x=x_pos, y=y_pos)

    def generate_combobox(self):
        if self.i == 0:
            self.i += 1
            ctk.CTkLabel(self, font=selected_font, text='+').grid(column=1, row=4)

            self.bp_combobox_2 = ctk.CTkComboBox(self, variable=self.selected_bp_2, values=values, state='readonly',
                                                 font=selected_font, dropdown_font=selected_font,
                                                 dropdown_fg_color='white', dropdown_text_color='black', justify='center')
            self.bp_combobox_2.grid(column=1, row=5, sticky='nsew')
            self.bp_combobox_2['values'] = values
            self.bp_combobox_2['state'] = 'readonly'
        elif self.i == 1:
            self.i += 1

            ctk.CTkLabel(self, font=selected_font, text='+').grid(column=1, row=6)

            self.bp_combobox_3 = ctk.CTkComboBox(self, variable=self.selected_bp_3, values=values, state='readonly',
                                                 font=selected_font, dropdown_font=selected_font,
                                                 dropdown_fg_color='white', dropdown_text_color='black', justify='center')
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

    def body_part_reqs(self) -> list[BodyPart]:
        body_parts = []
        selected_bp = self.combobox_variables_bp()
        for i in selected_bp:
            if len(i) == 0:
                pass
            else:
                body_parts.append(BodyPart(i))

        return body_parts

    def level_reqs(self):
        selected_lvl = self.combobox_variables_lvl()
        level = Level(selected_lvl)

        return level

    def create_reqs(self):
        user_reqs = UserRequirements(self.body_part_reqs(), self.level_reqs())
        return user_reqs

    def on_planning_clicked(self):
        self.controller.plan_and_show_workout(self.create_reqs())
