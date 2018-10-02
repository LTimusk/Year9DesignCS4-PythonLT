import tkinter as tk
import math 

def submit():

	print("submit pressed") 
	r = float(entr.get())
	h = float(enth.get())
	v = pi*r*r*h 
	v = round(v,3)


	output.insert(tk.INSERT, v)

root = tk.Tk()
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()
 


btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()










root.mainloop()

