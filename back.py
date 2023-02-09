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
	def editCode(self, key, messge = "Data Modified", error = "Key was not existed"):
		'''This is to modify the current version of the file'''
		file = self.getJSON()
		if key != "":
			prog = file.get(key)
			if prog == None:
				print(error)
			else:
				for i in range(len(prog)):
					x = input(f"{prog[i]}\n")
					if x != "":
						prog[i] = x
				x = input("")
				while x != "":
					prog.append(x)
					x = input()
				file.update({key: prog})
				print(messge)
				self.addCode(file)
		else:
			print("Invalid key")

	# Deleting a code
	def deleteCode(self, key, success = "Code deleted sucessfully", error = "Undefined Key"):
		'''To delete a code existed to the file'''
		file = self.getJSON()
		prog = file.get(key)
		if prog == None:
			print(error)
		else:
			file.pop(key)
			print(success)
			self.addCode(file)

	# String execution line by line
	def execCode(self, program: list[str]):
		'''This is to execute the program from array'''
		x = ""	
		for i in program:
			x += i + "\n"
		exec(x)