import json

def jsonFile(filename):
	file = open(filename)
	return json.loads(file.read())

def execution(program):
	for i in program:
		print(eval(i))


data = jsonFile("index.json")
# print(data['code'])
execution(data['code'])