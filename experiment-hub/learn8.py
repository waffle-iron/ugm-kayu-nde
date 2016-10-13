from tkinter import *
import time

#create invisible root window
root = Tk()
root.withdraw()

def closewindow():
	top.destroy()
	time.sleep(4)
	create()

def create():
	global top
	feet = 2
	top = Toplevel(root)
	top.overrideredirect(1) #hides max min buttons
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	top.geometry("%dx%d+0+0" % (w, h))
	app = Frame(top)
	app.grid()
	bttnhide = Button(app, text ="destroy window and create a new window in 4 seconds", command=closewindow)
	bttnhide.grid()
	bttnclose = Button(app, text ="exit application", command=root.destroy)
	bttnclose.grid()
	feet_entry = Entry(top, width=7, textvariable=feet)
	feet_entry.grid(column=2, row=1, sticky=(W, E))
	root.bind('<Escape>', lambda e: root.destroy())
	root.bind('<Double-1>', lambda e: root.destroy())
	


create()
root.mainloop()