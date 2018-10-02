print("**********************************************************")
print("Counted Loops: For")

print("0")
print("1")
print("2")
print("3")

#When we think of a for loop I want you to think about:
# Count: The variable that holds the current count
# Check: The check that is done each time the loop runs
# Change: The change applied to the count each tume the loop runs

#for <count var> in range (<initial value>, <check value>, <change>) :
print("**********************************************************")
#i = 0 0 < 4, TRUE run loop
#i = 1 1 < 4, TRUE run loop
#i = 2 2 < 4, TRUE run loop
#i = 3 3 < 4, TRUE run loop
#i = 4 4 < 4, FALSE exit can continue 

for i in range(0,4,1):
	print(i)

print ("**********************************************************")
#Change the loop perameters so it prints -44 to 136

for i in range(-44,137,1):
	print(i)
	if ( i % 2 == 0):
		print(str(i)+" is even")
	else:
		print(str(i)+" is odd")