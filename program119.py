#  We can also split lines using file handling in Python.
#  This splits the variable when space is encountered.
#  You can also split using any characters as we wish. Here is the code:
# Python code to illustrate split() function
with open(r"C:\Users\DELL\Desktop\python\day13\program9.txt", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)
