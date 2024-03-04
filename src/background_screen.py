import tkinter as tk
from input_screen import color
import customtkinter as ctk


class BackgroundScreen(ctk.CTkFrame):
    def __init__(self, master, parent, controller):
        self.master = master

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.configure(fg_color='dark grey')
