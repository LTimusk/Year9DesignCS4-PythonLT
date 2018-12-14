
import tkinter as tk
from PIL import ImageTk, Image


#************************* MY COMMANDS *****************************

def clicked1(event):
	print("Clicked - 1")
	x = event.x
	y = event.y

	#You need to write an if statement for every region
	
	if x > 0 and x < 15 or y > 0 and y < 33:
		print("OUT")
		aimLabel.config(text = "OUT")
		
	if x > 334 or y > 260:
		print("OUT")
		aimLabel.config(text = "OUT")
		
	if x > 16 and x < 120 and y > 33 and y < 140:
		print("position 4")
		aimLabel.config(text = "Aim = 4")
		
	if x > 120 and x < 220 and y > 33 and y < 140: 
		print("position 3")
		aimLabel.config(text = "Aim = 3")
		
	if x > 220 and x < 334 and y > 33 and y < 140:
		print("position 2")
		aimLabel.config(text = "Aim = 2")
	
	if x > 16 and x < 120 and y > 140 and y < 260:
		
		aimLabel.config(text = "Aim = 5")
		
	if x > 120 and x < 220 and y > 140 and y < 260:
		print("position 6")
		aimLabel.config(text = "Aim = 6")
		
	if x > 220 and x < 334 and y > 140 and y < 260:
		print("position 1 ")
		aimLabel.config(text = "Aim = 6")
		




	print("**************** END OF CODE *****************")

#________________________________________________________________________


def clicked2(event):
	print("Clicked - 2")
	#these variables only exisit inside the function 
	x = event.x
	y = event.y
	if x > 0 and x < 15 or y > 0 and y < 33:
		print("OUT")
		hitLabel.config(text = "OUT")
		
	if x > 334 or y > 260:
		print("OUT")
		hitLabel.config(text = "OUT")
		
	if x > 16 and x < 120 and y > 33 and y < 140:
		print("position 4")
		hitLabel.config(text = "Hit = 4")
	
	if x > 120 and x < 220 and y > 33 and y < 140: 
		print("position 3")
		hitLabel.config(text = "Hit = 3")

	if x > 220 and x < 334 and y > 33 and y < 140:
		print("position 2")
		hitLabel.config(text = "Hit = 2")

	if x > 16 and x < 120 and y > 140 and y < 260:
		print("position 5")
		hitLabel.config(text = "Hit = 5")
	
	if x > 120 and x < 220 and y > 140 and y < 260:
		print("position 6")
		hitLabel.config(text = "Hit = 6")

	if x > 220 and x < 334 and y > 140 and y < 260:
		print("position 1 ")
		hitLabel.config(text = "Hit = 1")
		




		


	print("**************** END OF CODE *****************")


def change(*args):
	print("changed")
#________________________________________________________________________

def setNamefnc():
	#entUN.config(state = "disabled")
	#print(setName["text"])
	if setName["text"] == "Change Name":
		setName.config(text = "Confirm Name")
		entUN.config(state = "normal")
	else:
		setName.config(text = "Change Name")
		currentName = entUN.get()
		print(currentName)
		entUN.config(state = "disabled")
		submit.config(state = "normal")
#________________________________________________________________________

	

def submit():
	print("submit")
	dataName.append(entUN.get())
	dataSpeed.append(var.get())

	if aimLabel["text"] != "OUT":
		dataAim.append(aimLabel["text"][-1]) #last character which is the number
	else:
		dataAim.append(aimLabel["text"])

	if aimLabel["text"] != "OUT":
		dataHit.append(hitLabel["text"][-1]) #last character which is the number
	else:
		dataHit.append(hitLabel["text"])

	

	print(dataName)
	print(dataSpeed)
	print(dataAim)
	print(dataHit)

	#Step 1: Loop through every element in the list.
	#Note, each list has the same lenght 
	#Use a technique called string construction: Build a string
	#and then paste it into the Text
	text = "Name\tSpeed\tAim\tHit\n\n"
	for i in range(0, len(dataName), 1):
		
		text = text + dataName[i] +"\t" +dataSpeed[i] +"\t"+ dataAim[i] +"\t"+ dataHit[i] +"\n"

	#Step 2: Paste it into the TExt
	entDATA.config(state = "normal")
	entDATA.delete("1.0",tk.END)
	entDATA.insert(tk.END,text)
	entDATA.config(state = "disabled")
#________________________________________________________________________


def Larger_Font(*args):
	#if checkVar = 1:
	#else:
		#print("off")



	#checkVar = tk.IntVar(window)
	#checkVar.set(0)

	if checkVar.get() == 0:
		print("on")
	else:
		print("off")

	if checkVar.get() != 0:
		labTITLE.config(background = '#55BCC9')
		window.configure(background = '#55BCC9')
		aimLabel.config(background = '#55BCC9')
		hitLabel.config(background = '#55BCC9')

	else:
		labTITLE.config(background = 'white')
		window.configure(background = 'white')
		aimLabel.config(background = 'white')
		hitLabel.config(background = 'white')
	

#________________________________________________________________________

def BigFont(*args):
	global p
	p += 1 
	if p%2==0:
		entDATA.config(font = ("Helvetica", 20))
		labUN.config(font = ("Helvetica", 20))
		labFont.config(font = ("Helvetica", 20))
		bigButton.config(text = "Smaller Font")

	else: 
		entDATA.config(font = ("Helvatica", 14))
		bigButton.config(text = "Larger Font")
		labUN.config(font = ("Helvatica", 14))
		labFont.config(font = ("Helvatica", 14))
		bigButton.config(font = ("Helvatica", 14))









#________________________________________________________________________


#**************************** COLLECTION OF DATA *************************

ctr = 0
currentName = ""
dataName = []
dataSpeed = []
dataAim = []
dataHit = []



window = tk.Tk()

checkVar = tk.IntVar(window)
checkVar.set(0)


#************************* USE OF DATA *************************************




#************************* ALL OF MY WIDGITS *******************************
 

labTITLE = tk.Label(window, text = "Serve Tracker", font =("Helvetica" "italics", 50))
labTITLE.config(background = '#55BCC9')
labTITLE.grid(row = 0, column = 0, columnspan = 4)

#________________________________________________________________________

labUN = tk.Label(window, text = "Player Name", background = 'white')
labUN.grid(row = 1, column = 0)

#________________________________________________________________________

entUN = tk.Entry(window)
entUN.grid(row = 2, column = 0) 

#________________________________________________________________________

entDATA = tk.Text(window, state = "disabled", height = 10, width = 50, font = ("Helvetica", 14))
entDATA.grid(row = 10, column = 0, columnspan = 6, sticky = "NESW")

#________________________________________________________________________

labUN = tk.Label(window, text = "Speed", background = 'white')
labUN.grid(row = 1, column = 1)

#________________________________________________________________________

labFont = tk.Label(window, text = "Contrast Mode", background = 'white')
labFont.grid(row = 1, column = 3)



#________________________________________________________________________

setName = tk.Button(window, text = "Confirm Name", command = setNamefnc)
setName.grid(column = 0, row = 7, columnspan = 2, sticky = "NESW")

#________________________________________________________________________

submit = tk.Button(window, text = "Submit", command = submit)
submit.config(state = "disabled")
submit.grid(column = 2, row = 7, columnspan = 2, sticky = "NESW")

#________________________________________________________________________

#labTITLE = tk.Label(text = "Serve Tracker", font =("Helvetica" "italics", 50))
#labTITLE.config(background = '#55BCC9')
#labTITLE.grid(row = 0, column = 0, columnspan = 4)

aimLabel = tk.Label(window, text = "AIM = ?")
aimLabel.config(background = '#55BCC9')
aimLabel.grid(column = 0, row = 6, columnspan = 2)


#________________________________________________________________________

hitLabel = tk.Label(window, text = "HIT = ?")
hitLabel.config( background = '#55BCC9')
hitLabel.grid(column = 2, row = 6, columnspan = 2, sticky = "NESW")

#________________________________________________________________________

#analyzeLabel = tk.Label(window, text = "Analyze Data")
#analyzeLabel.config(background = 'white')
#analyzeLabel.grid(column = 0, row = 8, columnspan = 3, pady = 15)

#________________________________________________________________________

displayLabel = tk.Label(window, text = "Data Display:")
displayLabel.grid(column = 0, row = 9, columnspan = 3, pady = 10)

#________________________________________________________________________
 

bigButton = tk.Button(window, text = "Larger Font", command = BigFont)
bigButton.grid(column = 0, row = 12, columnspan = 3, padx = 10, pady = 10)
p = 1
#________________________________________________________________________


checkVar.trace("w",Larger_Font)
checkbox = tk.Checkbutton(window, command = Larger_Font(), var = checkVar, offvalue = 1, onvalue = 0) 
checkbox.grid(row = 2, column = 3)
#*******************OPTION MENU***************************

#YOU CREATE A 2D LIST THAT HAS WHAT APPEARS IN THE OPTION BOX
SPEED = [
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
	"10"
]

var = tk.StringVar() #This is a variable that is attached to the drop down
var.set(SPEED[0]) #This sets the variable to our first option
var.trace("w",change) #This binds a change function is called when var changes

dropdownSP = tk.OptionMenu(window, var, SPEED[0], SPEED[1], SPEED[2], SPEED[3], SPEED[4], SPEED[5], SPEED[6], SPEED[7], SPEED[8], SPEED[9])
dropdownSP.grid(row = 2, column = 1)


#****************** OPTION MENU 2 ****************************




#^^^^^^^^^^^^^^^ OPTION MENU ^^^^^^^^^^^^^^^^^

window.title("Volleyball Tracker")
window.configure(background = '#55BCC9')

path = "VBPositions.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.grid(row = 5, column = 0, columnspan = 4, sticky ="NESW")
panel.bind("<Button-1>",clicked1)
panel.bind("<Button-2>",clicked2)


checkVar.set(1)
#Start the GUI
window.mainloop()


