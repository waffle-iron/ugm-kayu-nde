#!/bin/python3
# REQUIRED LIBRARY
# 1. Tkinter
# 2. NumPy
# 3. Matplotlib
# 4. PyAudio
# 5. SciPy
# 6. KayuEngine
# 7. Wave library

# IMPORT ALL THE REQUIRED LIBRARY
# ALL THE LIBRARY IMPORTED IN kayueEngine
from kayuEngine import *

# DEFINING SOME REQUIRED FUNCTIONS/CLASSES
# create window for application setting
def windowSettings():
	command=newWindow(root, "Input the wood data")

# record a sound
def recordingInAction():
	global t, s, f, lines, data	# import global variable
	p = pyaudio.PyAudio()		# create pyaudio object
	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
	print("* recording")		# print recording status to the terminal

	frames = []					# container for the raw sound data
	for i in range(0, int(RATE / CHUNK * kayu.recordDuration)):
	    data = stream.read(CHUNK)
	    frames.append(data)
	print("* done recording")	# print recording status to the terminal
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
	canvas.draw()

# INI PR KITA!
def toggleSpectrumTime():
	global toggleState, data, lines
	if toggleState == 0: #artinya kalau mau nampilin F
		fft_out = fft(data)
		N = len(data)
		T = 1.0 / 44100
		xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
		x = xf[1:N/2]
		y = 2.0/N * np.abs(fft_out[1:N/2])
		lines = Graph('modify', lines, x, y, f)
		canvas.draw()
		buttonToggle.config(text="T")
		toggleState = 1
	elif toggleState == 1:
		lines = Graph('modify', lines, t, data, f)
		canvas.draw()
		buttonToggle.config(text="F")
		toggleState = 0

def manualInput():
	global t, s, f, lines, data	# import global variable
	rate, data = wav.read('audiocheck.net_sin_2400Hz_-3dBFS_3s.wav')
	t = arange(len(data))
	lines = Graph('modify', lines, t, data, f)
	buttonToggle.config(state="normal")
	canvas.draw()



# PREPARE THE ROOT WINDOW
root = Tk()
rootTitle = root.title("Kayu: Open Wood NDT")
root.attributes('-fullscreen', True)
winCenter(root, 480, 320)

# METHOD FOR EXITTING THE ROOT WINDOW
def exitInput():
		root.destroy();


# MEMBUAT BEBERAPA FRAMES INTERFACE
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
buttonToggle = Button(frameToolbar, text="F", width=1, state="disabled", command=toggleSpectrumTime)
buttonToggle.pack(side=TOP, expand=NO, anchor=NE)
# button for the Pick
buttonPick = Button(frameToolbar, text="P", width=1)	#buttonPick
buttonPick.pack(side=TOP,  expand=NO, anchor=NE)

# button for the Manual
buttonManu = Button(frameToolbar, text="M", width=1, command=manualInput)	#buttonPick
buttonManu.pack(side=TOP,  expand=NO, anchor=NE)

# button for the Calculate
buttonCalc = Button(frameToolbar, text="C", width=1,command=exitInput)	#buttonPick
buttonCalc.pack(side=TOP,  expand=NO, anchor=NE)



# EMBEDDING THE GRAPH
canvas = FigureCanvasTkAgg(f, master=frameTop)
canvas.get_tk_widget().pack(side=LEFT,  expand=NO, anchor=NW)

# creating the toolbar
toolbar = NavigationToolbar2TkAgg(canvas, frameBottom).pack(side=LEFT)





# run the program
root.mainloop()
