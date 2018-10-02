#A loop is a programming structure that can repeat a section of code. 
#A loop can run the same code exactly over and over or 
#With some though it can generate a pattern.
#
#There are two broad categories of loops
# Conditional loops: There loop as long as the condition is true
# Counted Loops: There loop using a counter to keep tract of how many 
#                 Times the loop has run
#
# You can use any loop in any situaton, but usually from a design 
# Perspective there is a better loop in terms of coding.
#
# If you know in advance how many times a loop should run a COUNTED LOOP
# Is usually the better choice.
#
#If you don't know how many times a loop should run a CONDITIONAL LOOP
#Is usually the better choice.
#
print("*************************************************")
#Taking inputs

# we have to declare and initionalize word so it fails the while loop
word = ""


#A while loop evaluated a condition when it is first reached
#If the condition is true it enters the loop back

while len(word) < 6 or word.isalpha() == False:

	word = input("Print input a word larger than 5 letters: ")
	print(word.isalpha())
	if (len(word) < 6): 
		print("My big money man, are u stupid i said LONGER u uncultured swine")

	if (word.isalpha() == False):
		print("My big money man i said a LONG WORD")

#When we reach the bottom of the loop block we check the condition again.
#If it is true, we go back to the top of the block and run it again
print(word+" is a seriously long word!")

#CAUTION: DO NOT USE WHILE LOOPS TO CONTROL INPUTS WITH GUI PROGRAMS
