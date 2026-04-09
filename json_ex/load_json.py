import json
file = open("emp.json")
var = json.loads(file.read())

print(type(var))
