from tkinter import *
from tkinter import ttk
from numpy import arange, sin, pi #need to be customized
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

def winCenter(Tk, x, y):
	# get screen width and height
	ws = Tk.winfo_screenwidth() # width of the screen
	hs = Tk.winfo_screenheight() # height of the screen

	# enable the code below if want to turn full size
	# rootWidth = root.winfo_screenwidth()
	# rootHeight = root.winfo_screenheight()
	rootWidth = x
	rootHeight = y

	# calculate x and y coordinates for the Tk root window
	x = (ws/2) - (rootWidth/2)
	y = (hs/2) - (rootHeight/2)

	Tk.geometry('%dx%d+%d+%d' % (rootWidth, rootHeight, x, y))

def Graph(command, lines, x, y, figure):
	if command == 'create':
		a = figure.add_subplot(111)
		return a.plot(x,y)
	if command == 'modify':
		l = lines.pop(0)	
		l.remove()
		a = figure.add_subplot(111)
		return a.plot(x,y)
	if command == 'destroy':
		l = lines.pop(0)
		l.remove()
		return lines

	