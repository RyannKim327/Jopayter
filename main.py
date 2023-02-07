import os
from back import Jopayter

# Execution of the code
def execute():
	jopay = Jopayter("index.json")
	keys = jopay.jsonFile().keys()
	file = jopay.jsonFile()
	if len(keys) > 0:
		print(keys)
		key = input("Enter the key: ")
		if file.get(key) == None:
			print("Please check the spelling, or the cases, or might be not existed to the dictionary.")
		else:
			jopay.execution(file.get(key))
	else:
		print("There is no code here")

# Write a new code
def write():
	jopay = Jopayter("index.json")
	file = jopay.jsonFile()
	code = []
	print("Please enter the code here, use line by line method, use 4 spaces as indentation:")
	c = input("")
	while c != "":
		code.append(f"{c}")
		c = input("")
		if c == "":
			break
	key = input("Enter the key name: ")
	file.update({f"{key}": code})
	jopay.reWriteJson(file)

def updateCode():
	jopay = Jopayter("index.json")
	print(jopay.jsonFile().keys())
	key = input("Enter the key to use: ")
	jopay.editJSON(key)

# Main method starts here
choice = 0

while choice != -1:
	if os.system("cls"):
		os.system("clear")
	print("Welcome to my Jopayter, here are some of the lists that exists to this program:\n1. Execute a code\n2. Add new code\n3. Update a code\n4. Exit")
	c = input("Enter a number of your choice: ")
	try:
		choice = int(c)
	except:
		choice = 0
	
	if choice == 1:
		execute()
		input("")
	elif choice == 2:
		write()
		input("")
	elif choice == 3:
		updateCode()
		input("")
	elif choice == 4:
		choice = -1
		print("Thank you...")
	
	if os.system("cls"):
		os.system("clear")