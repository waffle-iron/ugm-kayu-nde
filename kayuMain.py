#!/bin/python3
# Required library
# 1. Tkinter
# 2. NumPy
# 3. Matplotlib
# 4. PyAudio
# 5. SciPy
# 6. KayuEngine

# import all the library
from kayuEngine import *

# prepare the root window
root = Tk()
rootTitle = root.title("Kayu: Open Wood NDT")
winCenter(root, 480, 320)

# set the layout

# create the graph
t = arange(-1.0, 1.0, 0.001)
s = t*sin(1/t)

# draw initial graph
f = Figure(figsize=(4.4,2.8), dpi=100)
a = f.add_subplot(111)
lines = a.plot(t, s) #plot(x,y) for initial graph

# create side bar
Button(root, text="A").pack(side=RIGHT, expand=NO, fill=NONE, anchor=NE)


# embedding the graph
canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().pack(side=TOP, expand=YES, anchor=NW)
# creating the toolbar
toolbar = NavigationToolbar2TkAgg(canvas, root).pack(side=LEFT,  expand=NO, anchor=NW)




s = t*sin(1/2*t)
lines = Graph('modify', lines, t, s, f)

Graph('destroy', lines, t, s, f)

t = arange(-2.0, 1.0, 0.001)
s = t*sin(1/t)
lines = Graph('create', lines, t, s, f)

# create side bar


# run the program
root.mainloop()