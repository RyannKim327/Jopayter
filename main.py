import os
from back import Jopayter

# Execution of the code
def execute():
	jopay = Jopayter("index.json")
	keys = jopay.getJSON().keys()
	file = jopay.getJSON()
	if len(keys) > 0:
		print(keys)
		key = input("Enter the key: ")
		if file.get(key) == None:
			print("Please check the spelling, or the cases, or might be not existed to the dictionary.")
		else:
			jopay.execCode(file.get(key))
	else:
		print("There is no code here")

# Write a new code
def write():
	jopay = Jopayter("index.json")
	jopay.createCode()

def updateCode():
	jopay = Jopayter("index.json")
	print(jopay.getJSON().keys())
	key = input("Enter the key to use: ")
	jopay.editCode(key)

def deleteCode():
	jopay = Jopayter("index.json")
	print(jopay.getJSON().keys())
	key = input("Enter the key to use: ")
	jopay.deleteCode(key)

# Main method starts here
choice = 0

while choice != -1:
	if os.system("cls"):
		os.system("clear")
	print("\033[33m")
	print("+------------------------------------------------------------------------------+")
	print("| Welcome to \033[32mJopayter\033[33m, here are some of the lists that exists to this program: |")
	print("| 1. Execute a code                                                            |")
	print("| 2. Add new code                                                              |")
	print("| 3. Update a code                                                             |")
	print("| 4. Delete a code                                                             |")
	print("| 5. Exit                                                                      |")
	print("+------------------------------------------------------------------------------+")
	c = input("Enter a number of your choice: ")
	print("\033[37m")
	if os.system("cls"):
		os.system("clear")
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
		deleteCode()
		input("")
	elif choice == 5:
		choice = -1
		print("Thank you...")
	
	if os.system("cls"):
		os.system("clear")