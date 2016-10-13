from tkinter import *
from tkinter import ttk
root = Tk()
I = ttk.Label(root, text="Starting...")
I.grid()
I.bind('<Enter>', lambda e: I.configure(text='Moved mouse inside'))
I.bind('<Leave>', lambda e: I.configure(text='Moved mouse outside'))
I.bind('<1>', lambda e: I.configure(text='Clicked left mouse button'))
I.bind('<Double-1>', lambda e: I.configure(text='Double click'))
I.bind('<B3-Motion>', lambda e: I.configure(text='right drag to %d,%d' % (e.y,e.y)))
root.mainloop()