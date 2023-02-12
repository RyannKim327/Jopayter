import json

class Jopayter:
	def __init__(self, filename: str):
		'''This is to initiate the data (json file)'''
		self.filename = filename

	# File import and load as JSON
	def getJSON(self):
		'''This is to get the value or the data of the entire json file, and returns as dictionary'''
		file = open(self.filename)
		return json.loads(file.read())

	# Creating new Data
	def addCode(self, data, message = "New Data Added"):
		'''This is to overwrite the data that the (json file) has'''
		file = open(self.filename, "w")
		file.write(json.dumps(data))
		print(message)

	# Edit the code line by line
	def editCode(self, key, message = "Data Modified", error = "Key was not existed"):
		'''This is to modify the current version of the file'''
		print("Use the keyword \"cls\" in all lowercase to remove the text in a specific line.")
		file = self.getJSON()
		if key != "":
			prog = file.get(key)
			if prog == None:
				print(error)
			else:
				j = 1
				for i in range(len(prog)):
					x = input(f"{j}: {prog[i]}\n").replace("\t", "    ")
					if x != "":
						if x == "cls":
							prog[i] = ""
						else:
							prog[i] = x
					j += 1
				x = input(f"{j}: ").replace("\t", "    ")
				while x != "":
					if x == "cls":
						prog.append("")
					else:
						prog.append(x)
					j += 1
					x = input(f"{j}")
				file.update({key: prog})
				self.addCode(file, message=message)
		else:
			print("Invalid key")

	# Creating a code
	def createCode(self):
		'''This is to create a new code'''
		file = self.getJSON()
		code = []
		print("Please enter the code here, use line by line method, use 4 spaces as indentation:")
		x = 1
		c = input(f"{x}: ").replace("\t", "    ")
		while c != "":
			code.append(f"{c}")
			x += 1
			c = input(f"{x}: ").replace("\t", "    ")
			if c == "":
				break
		key = input("Enter the key name: ")
		if key == "":
			print("Enter invalid key")
		else:
			file.update({f"{key}": code})
			self.addCode(file)

	# Deleting a code
	def deleteCode(self, key, success = "Code deleted sucessfully", error = "Undefined Key"):
		'''To delete a code existed to the file'''
		file = self.getJSON()
		prog = file.get(key)
		if prog == None:
			print(error)
		else:
			file.pop(key)
			self.addCode(file, message=success)

	def checkCode(self, key):
		file = self.getJSON()
		if file.get(key):
			return file.get(key)
		else:
			return [ "Invalid key, or not found." ]

	# String execution line by line
	def execCode(self, program: list[str]):
		'''This is to execute the program from array'''
		x = ""
		for i in program:
			x += i + "\n"
		exec(x)