#StringExample.py

#This file will go through the basics of
#String manipulation

#Strings are collections of characters 
#Strings are enclosed in "" or ''
# "Paul is cool"
# "Paul is cool!"
#Two things we ned to talk about
# when we think of strings
#Index - Always start at 0
#Length

#Example

# 0123      012345
# "paul"     "Monkey"

# len ("Paul") = 4
# len ("Monkey") = 6 

name = "Paul" 

print(name) 

sentence = name + " is cool!"
print(sentence)
print(sentence + "!")
 
fLetter = name[0]
print(fLetter)
letters1 = name[0:2]
print(letters1)
letters2 = name [2:]
print(letters2)
letters3 = name[:2]
print(letters3)


lname = len(name)
print(lname)

for i in range (len(name)):
	print(name[i])




