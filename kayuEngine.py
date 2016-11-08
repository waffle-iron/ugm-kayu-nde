from tkinter import *
from tkinter import ttk
from numpy import arange, sin, pi #need to be customized
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

setPosition = 0

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


class Wood:
	def __init__(self, weight, length, crossSectionLength, crossSectionWidth):
		self.length = float(length)
		self.weight = float(weight)
		self.crossSectionWidth = float(crossSectionWidth)
		self.crossSectionLength = float(crossSectionLength)
		self.density = float(weight)/(float(length)*float(crossSectionLength)*float(crossSectionWidth))


# USERDEFINED METHOD START
def newWindow(root, title):
	
	t = Toplevel(root)
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
		global setPosition 
		setPosition+=1
		# print("succes")


	buttonWeight = Button(frameInput, text="Set", command=setWeight)
	buttonWeight.grid(column=2, row=0)
	buttonLength = Button(frameInput, text="Set", state=DISABLED, command=setLength)
	buttonLength.grid(column=2, row=1)
	buttonCrossSectionLength = Button(frameInput, text="Set", state=DISABLED, command=setCrossSectionLength)
	buttonCrossSectionLength.grid(column=2, row=2)
	buttonCrossSectionWidth = Button(frameInput, text="Set", state=DISABLED, command=setCrossSectionWidth)
	buttonCrossSectionWidth.grid(column=2, row=3)

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
					inputTextBox(entryCrossSectionWidth, "7")
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
					inputTextBox(entryCrossSectionWidth, "8")
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
					inputTextBox(entryCrossSectionWidth, "9")
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
					inputTextBox(entryCrossSectionWidth, "4")
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
					inputTextBox(entryCrossSectionWidth, "5")
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
					inputTextBox(entryCrossSectionWidth, "6")
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
					inputTextBox(entryCrossSectionWidth, "1")	
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
					inputTextBox(entryCrossSectionWidth, "2")
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
					inputTextBox(entryCrossSectionWidth, "3")
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
					inputTextBox(entryCrossSectionWidth, ".")	
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
					inputTextBox(entryCrossSectionWidth, "0")

	


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
	buttonDel = Button(frameKeys, text="Del")# command=inputTextBoxDel)
	buttonDel.grid(column=3, row=3)	





# ON SCREEN KEYPAD
def inputTextBox(keys, theValue):
	keys.insert(END, theValue)







# GLOBAL VARIABLES START
kayu = Wood(1.2,1.3,1.4,1.5) #initial instance of Wood
# GLOBAL VARIABLES END