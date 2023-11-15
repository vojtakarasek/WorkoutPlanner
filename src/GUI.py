import tkinter
from tkinter import *
from tkinter import ttk

main = Tk()

screen_height = main.winfo_screenheight()
screen_width = main.winfo_screenwidth()

frm1 = ttk.Frame(main, padding=10)
frm1.place(x=screen_width/2, y=screen_height/2)

ttk.Button(main, text="Exit", command=main.destroy).grid(column=0, row=0)

ttk.Label(frm1, text="Vyberte část těla, kterou chcete posilovat").grid(column=1,row=0)

current_var = tkinter.StringVar()
Bp_combobox = ttk.Combobox(frm1, textvariable=current_var)
Bp_combobox.grid(column=1, row=1)
Bp_combobox['values'] = ('břicho', 'záda', 'paže', 'prsa', 'ramena', 'stehna', 'lýtka')
Bp_combobox['state'] = ('readonly')

ttk.Label(frm1, text="vyberte obtížnost").grid(column=1, row=2)

current_var2 = tkinter.StringVar()
Lvl_combobox = ttk.Combobox(frm1, textvariable=current_var2)
Lvl_combobox.grid(column=1, row=3)
Lvl_combobox['values'] = ('začátečník', 'středně pokročilý', 'pokročilý')
Lvl_combobox['state'] = ('readonly')

frame_width = frm1.winfo_reqwidth()
frame_height = frm1.winfo_reqheight()



main.attributes('-fullscreen', True)

main.mainloop()
