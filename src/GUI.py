import tkinter
from tkinter import *
from tkinter import ttk


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Workout planner")

        ttk.Button(self.master, text="Exit", command=self.master.destroy).grid(column=0, row=0)

        self.screen_height = self.master.winfo_screenheight()
        self.screen_width = self.master.winfo_screenwidth()

        self.frm1 = ttk.Frame(self.master, padding=10)

        self.values = ['','břicho', 'záda', 'paže', 'prsa', 'ramena', 'stehna', 'lýtka']

        self.selected_bp_1 = tkinter.StringVar()
        self.bp_combobox = ttk.Combobox(self.frm1, textvariable=self.selected_bp_1)

        self.selected_bp_2 = tkinter.StringVar()
        self.bp_combobox2 = ttk.Combobox(self.frm1, textvariable=self.selected_bp_2)

        style = ttk.Style()
        style.configure("BW.TLabel", background="red")
        self.frm2 = ttk.Frame(self.master, padding=10, height=self.screen_height, width=self.screen_width, style="BW.TLabel" )
        self.frm2.pack_propagate(0)

    def place_frame_center(self, event):
        frame_width = self.frm1.winfo_reqwidth()
        frame_height = self.frm1.winfo_reqheight()

        x_pos = (self.screen_width - frame_width) // 2
        y_pos = (self.screen_height - frame_height) // 2

        self.frm1.place(x=x_pos, y=y_pos)

    def place_frame_center2(self, event):
        frame_width = self.frm2.winfo_reqwidth()
        frame_height = self.frm2.winfo_reqheight()

        x_pos = (self.screen_width - frame_width) // 2
        y_pos = (self.screen_height - frame_height) // 2

        self.frm2.place(x=x_pos, y=y_pos)
    def generate_combobox(self):
        ttk.Label(self.frm1, text="+").grid(column=1, row=4)

        self.bp_combobox2.grid(column=1, row=5)
        self.bp_combobox2['values'] = self.values
        self.bp_combobox2['state'] = 'readonly'

    def frame1(self):
        # tkinter.Button(self.master, bg='red', text= " X ", command=self.master.destroy).grid(column=0, row=0)

        ttk.Label(self.frm1, text="Vyberte obtížnost").grid(column=1, row=0)

        selected_level = tkinter.StringVar()
        lvl_combobox = ttk.Combobox(self.frm1, textvariable=selected_level)
        lvl_combobox.grid(column=1, row=1)
        lvl_combobox['values'] = ('začátečník', 'středně pokročilý', 'pokročilý')
        lvl_combobox['state'] = 'readonly'

        ttk.Label(self.frm1, text="Vyberte část těla, kterou chcete posilovat").grid(column=1, row=2)

        self.bp_combobox.grid(column=1, row=3)
        self.bp_combobox['values'] = self.values
        self.bp_combobox['state'] = 'readonly'

        ttk.Button(self.frm1, text="+", command=self.generate_combobox, padding=5).grid(column=1, row=6)

        ttk.Button(self.frm1, text="Použít", padding=5).grid(column=1,row=7)

        self.frm1.place(x=0, y=0)
        self.frm1.bind("<Configure>", self.place_frame_center)

    def frame2(self):
        ttk.Label(self.frm2, text="jsi tady!!!").grid(column=0, row=0)
        ttk.Label(self.frm2, text="jsi tady!!!").grid(column=1, row=0)
        ttk.Label(self.frm2, text="jsi tady!!!").grid(column=2, row=0)
        ttk.Label(self.frm2, text="jsi tady!!!").grid(column=3, row=0)
        ttk.Label(self.frm2, text="jsi tady!!!").grid(column=4, row=0)
        ttk.Label(self.frm2, text="jsi tady!!!").grid(column=0, row=1)
        ttk.Label(self.frm2, text="jsi tady!!!").grid(column=0, row=2)
        ttk.Label(self.frm2, text="jsi tady!!!").grid(column=0, row=3)
        ttk.Label(self.frm2, text="jsi tady!!!").grid(column=0, row=4)
        ttk.Label(self.frm2, text="jsi tady!!!").grid(column=0, row=5)

        self.frm2.place(x=0, y=0)
        self.frm2.bind("<Configure>", self.place_frame_center2)




def main():
    root = Tk()
    gui = GUI(root)
    #gui.frame1()
    gui.frame2()
    root.attributes('-fullscreen', True)
    root.mainloop()


if __name__ == "__main__":
    main()
