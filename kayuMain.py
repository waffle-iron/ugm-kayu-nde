#!/bin/python3

from tkinter import *
from tkinter import ttk

root = Tk()
rootTitle = root.title("Kayu: Open Wood NDT")

# enable the code below if want to turn full size
# rootWidth = root.winfo_screenwidth()
# rootHeight = root.winfo_screenheight()

rootWidth = 480
rootHeight = 320

root.geometry(("%dx%d")%(rootWidth,rootHeight))

root.mainloop()