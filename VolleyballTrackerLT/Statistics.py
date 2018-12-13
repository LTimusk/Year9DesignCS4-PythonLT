import tkinter as tk

file = open("Statistics.py", "a")# the a is for append
temps = file.append()
statslist = temps.split("\n")
statslist.sort()
print(statslist)



