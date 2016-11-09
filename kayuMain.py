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

# DEFINING A CLASS OF WOOD
def windowSettings():
	command=newWindow(root, "Input the wood data")
def recordingInAction():
	global t, s, f, lines, data
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
	print("* recording")

	frames = []
	for i in range(0, int(RATE / CHUNK * kayu.recordDuration)):
	    data = stream.read(CHUNK)
	    frames.append(data)
	    

	print("* done recording")
	stream.stop_stream()
	stream.close()
	p.terminate()
	WAVE_OUTPUT_FILENAME = timeNow() + "name" + kayu.name + ".wav"
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	rate, data = wav.read(WAVE_OUTPUT_FILENAME)
	t = arange(len(data))
	lines = Graph('modify', lines, t, data, f)
	buttonToggle.config(state="normal")
def toggleSpectrumTime():
	global toggleState
	toggleState

# USERDEFINED METHOD END


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

# CREATE THE SIDE BAR
# botton for Input
buttonSettings = Button(frameToolbar, text="S", command=windowSettings, width=1)	#buttonInput
buttonSettings.pack(side=TOP, expand=NO, anchor=NE)
# button for the Record
buttonRecord = Button(frameToolbar, text="R", width=1, command=recordingInAction)	#buttonRecord
buttonRecord.pack(side=TOP,  expand=NO, anchor=NE)
#button for the Spectrum/Time toggle
buttonToggle = Button(frameToolbar, text="F", width=1, state="disabled")
buttonToggle.pack(side=TOP, expand=NO, anchor=NE)
# button for the Pick
buttonPick = Button(frameToolbar, text="P", width=1)	#buttonPick
buttonPick.pack(side=TOP,  expand=NO, anchor=NE)
# button for the Calculate
buttonCalc = Button(frameToolbar, text="C", width=1)	#buttonPick
buttonCalc.pack(side=TOP,  expand=NO, anchor=NE)

# EMBEDDING THE GRAPH
canvas = FigureCanvasTkAgg(f, master=frameTop)
canvas.get_tk_widget().pack(side=LEFT,  expand=NO, anchor=NW)

# creating the toolbar
toolbar = NavigationToolbar2TkAgg(canvas, frameBottom).pack(side=LEFT)




# s = t*sin(1/2*t)
# lines = Graph('modify', lines, t, s, f)

# Graph('destroy', lines, t, s, f)

# t = arange(-2.0, 1.0, 0.001)
# s = t*sin(1/t)
# lines = Graph('create', lines, t, s, f)




# run the program
root.mainloop()