from tkinter import *
from tkinter import ttk
from numpy import arange, sin, pi #need to be customized
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import pyaudio
import wave
import sys
import numpy as np
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import datetime as dt


class Wood:
	def __init__(self, weight, length, crossSectionLength, crossSectionWidth, recordDuration, name):
		self.length = float(length)
		self.weight = float(weight)
		self.crossSectionWidth = float(crossSectionWidth)
		self.crossSectionLength = float(crossSectionLength)
		self.density = float(weight)/(float(length)*float(crossSectionLength)*float(crossSectionWidth))
		self.recordDuration = int(recordDuration)
		self.name = name
def timeNow():
	return dt.datetime.now().strftime("%Y-%m-%d %H:%M")
# GLOBAL VARIABLES START
kayu = Wood(1.2, 1.3, 1.4, 1.5, 3, ".123") #initial instance of Wood
recordStatus = 0
setPosition = 0
# varibel global figure
t = arange(-1.0, 1.0, 0.001)
s = t*sin(1/t)
# draw initial graph
f = Figure(figsize=(4.4,2.8), dpi=100)
a = f.add_subplot(111)
lines = a.plot(t, s) #plot(x,y) for initial graph
data = []
# variable global recording
CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
WAVE_OUTPUT_FILENAME = timeNow() + "name" + kayu.name + ".wav"
if sys.platform == 'darwin':
    CHANNELS = 1
# variable global toggle
toggleState = 0;
# GLOBAL VARIABLE END

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
		return a.plot(x,y, 'b')
	if command == 'modify':
		l = lines.pop(0)	
		l.remove()
		a = figure.add_subplot(111)
		return a.plot(x,y, 'b')
	if command == 'destroy':
		l = lines.pop(0)
		l.remove()
		return lines




# USERDEFINED METHOD START
def newWindow(root, title):
	
	t = Toplevel(root)
	t.attributes('-fullscreen', True)
	t.wm_title(title)	
	winCenter(t, 480, 320)
	t.lift(aboveThis=root)

	frameInput = Frame(t)
	frameInput.grid(column=0, row=0, sticky=(N))
	frameKeys = Frame(t)
	frameKeys.grid(column=0, row=1, sticky=(S))



	labelWeight = Label(frameInput, text="Weight (kg) ") 
	labelWeight.grid(column=0, row=0, sticky=(W))
	labelLength = Label(frameInput, text="Length (m): ")
	labelLength.grid(column=0, row=1, sticky=(W))
	labelCrossSectionLength = Label(frameInput, text="CS Length (m): ")
	labelCrossSectionLength.grid(column=0, row=2, sticky=(W))
	labelCrossSectionWidth = Label(frameInput, text="CS Width (m): ")
	labelCrossSectionWidth.grid(column=0, row=3, sticky=(W))
	labelDuration = Label(frameInput, text="Duration (s): ")
	labelDuration.grid(column=0, row=4, sticky=(W))
	labelWoodName = Label(frameInput, text="Wood Name: ")
	labelWoodName.grid(column=0, row=5, sticky=(W))

	weightStr = StringVar()
	entryWeight = Entry(frameInput, textvariable=weightStr)
	entryWeight.grid(column=1, row=0, )
	weightStr.set(kayu.weight)

	lengthStr = StringVar()
	entryLength = Entry(frameInput, textvariable=lengthStr)
	entryLength.grid(column=1, row=1)
	lengthStr.set(kayu.length)

	crossSectionLengthStr = StringVar()
	entryCrossSectionLength = Entry(frameInput, textvariable=crossSectionLengthStr)
	entryCrossSectionLength.grid(column=1, row=2)
	crossSectionLengthStr.set(kayu.crossSectionLength)
	
	crossSectionWidthStr = StringVar()
	entryCrossSectionWidth = Entry(frameInput, textvariable=crossSectionWidthStr)
	entryCrossSectionWidth.grid(column=1, row=3)
	crossSectionWidthStr.set(kayu.crossSectionWidth)

	durationStr = StringVar()
	entryDuration = Entry(frameInput, textvariable=durationStr)
	entryDuration.grid(column=1, row=4)
	durationStr.set(kayu.recordDuration)		

	woodNameStr = StringVar()
	entryWoodName = Entry(frameInput, textvariable=woodNameStr)
	entryWoodName.grid(column=1, row=5)
	woodNameStr.set(kayu.name)

	def setWeight():
		kayu.weight = weightStr.get()
		buttonWeight.config(state="disabled")
		buttonLength.config(state="normal")
		global setPosition 
		setPosition+=1
		# print("succes")
	def setLength():
		kayu.length = lengthStr.get()
		buttonLength.config(state="disabled")
		buttonCrossSectionLength.config(state="normal")
		global setPosition 
		setPosition+=1
		# print("succes")
	def setCrossSectionLength():
		kayu.crossSectionLength = crossSectionLengthStr.get()
		buttonCrossSectionLength.config(state="disabled")
		buttonCrossSectionWidth.config(state="normal")
		global setPosition 
		setPosition+=1
		# print("succes")		
	def setCrossSectionWidth():
		kayu.crossSectionWidth = crossSectionWidthStr.get()
		buttonCrossSectionWidth.config(state="disabled")
		buttonDuration.config(state="normal")
		global setPosition 
		setPosition+=1
		# print("succes")
	def setDuration():
		kayu.recordDuration = int(durationStr.get())
		buttonDuration.config(state="disabled")
		buttonWoodName.config(state="normal")
		global setPosition 
		setPosition+=1
		# print("succes")
	def setName():
		kayu.name = str(woodNameStr.get())
		buttonWoodName.config(state="disabled")
		buttonWeight.config(state="normal")
		global setPosition 
		setPosition=0
		# print("succes")


	buttonWeight = Button(frameInput, text="Set", command=setWeight)
	buttonWeight.grid(column=2, row=0)
	buttonLength = Button(frameInput, text="Set", state=DISABLED, command=setLength)
	buttonLength.grid(column=2, row=1)
	buttonCrossSectionLength = Button(frameInput, text="Set", state=DISABLED, command=setCrossSectionLength)
	buttonCrossSectionLength.grid(column=2, row=2)
	buttonCrossSectionWidth = Button(frameInput, text="Set", state=DISABLED, command=setCrossSectionWidth)
	buttonCrossSectionWidth.grid(column=2, row=3)
	buttonDuration = Button(frameInput, text="Set", state=DISABLED, command=setDuration)
	buttonDuration.grid(column=2, row=4)
	buttonWoodName = Button(frameInput, text="Set", state=DISABLED, command=setName)
	buttonWoodName.grid(column=2, row=5)

	def inputTextBox7():
		if setPosition == 0:
			inputTextBox(entryWeight, "7")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, "7")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, "7")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, "7")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, "7")
						else:
							inputTextBox(entryWoodName, "7")
	def inputTextBox8():
		if setPosition == 0:
			inputTextBox(entryWeight, "8")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, "8")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, "8")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, "8")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, "8")
						else:
							inputTextBox(entryWoodName, "8")
	def inputTextBox9():
		if setPosition == 0:
			inputTextBox(entryWeight, "9")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, "9")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, "9")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, "9")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, "9")
						else:
							inputTextBox(entryWoodName, "9")
	def inputTextBox4():
		if setPosition == 0:
			inputTextBox(entryWeight, "4")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, "4")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, "4")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, "4")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, "4")
						else:
							inputTextBox(entryWoodName, "4")
	def inputTextBox5():
		if setPosition == 0:
			inputTextBox(entryWeight, "5")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, "5")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, "5")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, "5")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, "5")
						else:
							inputTextBox(entryWoodName, "5")
	def inputTextBox6():
		if setPosition == 0:
			inputTextBox(entryWeight, "6")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, "6")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, "6")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, "6")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, "6")
						else:
							inputTextBox(entryWoodName, "6")
	def inputTextBox1():
		if setPosition == 0:
			inputTextBox(entryWeight, "1")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, "1")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, "1")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, "1")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, "1")
						else:
							inputTextBox(entryWoodName, "1")
	def inputTextBox2():
		if setPosition == 0:
			inputTextBox(entryWeight, "2")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, "2")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, "2")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, "2")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, "2")
						else:
							inputTextBox(entryWoodName, "2")
	def inputTextBox3():
		if setPosition == 0:
			inputTextBox(entryWeight, "3")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, "3")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, "3")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, "3")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, "3")
						else:
							inputTextBox(entryWoodName, "3")
	def inputTextBoxDot():
		if setPosition == 0:
			inputTextBox(entryWeight, ".")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, ".")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, ".")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, ".")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, ".")
						else:
							inputTextBox(entryWoodName, ".")	
	def inputTextBox0():
		if setPosition == 0:
			inputTextBox(entryWeight, "0")
		else:
			if setPosition == 1:
				inputTextBox(entryLength, "0")
			else:
				if setPosition == 2:
					inputTextBox(entryCrossSectionLength, "0")
				else:
					if setPosition ==3:
						inputTextBox(entryCrossSectionWidth, "0")
					else:
						if setPosition ==4:
							inputTextBox(entryDuration, "0")
						else:
							inputTextBox(entryWoodName, "0")

	def inputTextBoxDel():
		if setPosition == 0:
			deleteTextBox(entryWeight)
		else:
			if setPosition == 1:
				deleteTextBox(entryLength)
			else:
				if setPosition == 2:
					deleteTextBox(entryCrossSectionLength)
				else:
					if setPosition ==3:
						deleteTextBox(entryCrossSectionWidth)
					else:
						if setPosition ==4:
							deleteTextBox(entryDuration)
						else:
							deleteTextBox(entryWoodName)	


	button7 = Button(frameKeys, text="7", command=inputTextBox7)
	button7.grid(column=1, row=0)
	button8 = Button(frameKeys, text="8", command=inputTextBox8)
	button8.grid(column=2, row=0)
	button9 = Button(frameKeys, text="9", command=inputTextBox9)
	button9.grid(column=3, row=0)
	button4 = Button(frameKeys, text="4", command=inputTextBox4)
	button4.grid(column=1, row=1)
	button5 = Button(frameKeys, text="5", command=inputTextBox5)
	button5.grid(column=2, row=1)
	button6 = Button(frameKeys, text="6", command=inputTextBox6)
	button6.grid(column=3, row=1)
	button1 = Button(frameKeys, text="1", command=inputTextBox1)
	button1.grid(column=1, row=2)
	button2 = Button(frameKeys, text="2", command=inputTextBox2)
	button2.grid(column=2, row=2)
	button3 = Button(frameKeys, text="3", command=inputTextBox3)
	button3.grid(column=3, row=2)	
	buttonDot = Button(frameKeys, text=".", command=inputTextBoxDot)
	buttonDot.grid(column=1, row=3)
	button0 = Button(frameKeys, text="0", command=inputTextBox0)
	button0.grid(column=2, row=3)
	buttonDel = Button(frameKeys, text="Del", command=inputTextBoxDel)
	buttonDel.grid(column=3, row=3)	

	def quitInput():
		global setPosition 
		setPosition=0
		t.destroy();

	buttonExit = Button(frameKeys, text="Close", command=quitInput)
	buttonExit.grid(column=4, row=5)





# ON SCREEN KEYPAD
def inputTextBox(keys, theValue):
	keys.insert(END, theValue)

def deleteTextBox(keys):
	keys.delete(0, 'end')






