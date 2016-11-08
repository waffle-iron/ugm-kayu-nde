#!/bin/python3
# REQUIRED LIBRARY
# 1. Tkinter
# 2. NumPy
# 3. Matplotlib
# 4. PyAudio
# 5. SciPy
# 6. KayuEngine

# IMPORT ALL THE REQUIRED LIBRARY
from kayuEngine import *

# PREPARE THE ROOT WINDOW
root = Tk()
rootTitle = root.title("Kayu: Open Wood NDT")
winCenter(root, 480, 320)

# MEMBUAT BEBERAPA FRAMES
# tedapat dua frame utama yaitu TOP dan BOTTOM
frameTop = Frame(root, width=480, height=280)
frameTop.pack(side=TOP,  expand=NO)
frameBottom = Frame(root, width=480, height=40)
frameBottom.pack(side=BOTTOM,  expand=NO, anchor=SW)
# terdapat satu child frame dari frame TOP
frameToolbar = Frame(frameTop, width=40, height=280)
frameToolbar.pack(side=RIGHT, expand=NO, anchor=NE)

# CREATE THE GRAPHH
t = arange(-1.0, 1.0, 0.001)
s = t*sin(1/t)
# draw initial graph
f = Figure(figsize=(4.4,2.8), dpi=100)
a = f.add_subplot(111)
lines = a.plot(t, s) #plot(x,y) for initial graph

# CREATE THE SIDE BAR
# botton for Input
buttonInput = Button(frameToolbar, text="I", width=1)	#buttonInput
buttonInput.pack(side=TOP,  expand=NO, anchor=NE)
# button for the Record
buttonRecord = Button(frameToolbar, text="R", width=1)	#buttonRecord
buttonRecord.pack(side=TOP,  expand=NO, anchor=NE)
# button for the Stop
buttonStop = Button(frameToolbar, text="S", width=1)	#buttonStop
buttonStop.pack(side=TOP,  expand=NO, anchor=NE)
# button for the Stop
buttonPick = Button(frameToolbar, text="P", width=1)	#buttonPick
buttonPick.pack(side=TOP,  expand=NO, anchor=NE)

# EMBEDDING THE GRAPH
canvas = FigureCanvasTkAgg(f, master=frameTop)
canvas.get_tk_widget().pack(side=LEFT,  expand=NO, anchor=NW)

# creating the toolbar
toolbar = NavigationToolbar2TkAgg(canvas, frameBottom).pack(side=LEFT)




s = t*sin(1/2*t)
lines = Graph('modify', lines, t, s, f)

Graph('destroy', lines, t, s, f)

t = arange(-2.0, 1.0, 0.001)
s = t*sin(1/t)
lines = Graph('create', lines, t, s, f)

# create side bar


# run the program
root.mainloop()