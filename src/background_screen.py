from PIL import Image
import customtkinter as ctk


class BackgroundScreen(ctk.CTkFrame):
    def __init__(self, master, parent, controller):
        self.master = master

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.my_image = ctk.CTkImage(dark_image=Image.open("imgs/background.jpg"), size=(2560, 1440))
        self.image_label = ctk.CTkLabel(self, image=self.my_image, text='')
        self.image_label.place(x=0, y=0)
