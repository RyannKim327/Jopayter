import json

# File import and load as JSON
def jsonFile(filename):
	file = open(filename)
	return json.loads(file.read())


# String execution line by line
def execution(program):
	for i in program:
		eval(i)


data = jsonFile("index.json")
execution(data['code'])