import json

'''
json.dumps - converts a python object to Json String
json.dump - converts a python object to Json file

json.loads - parses a json string to python object
json.load - parses a json file into python object


'''



x = {
"fruit" : "apple",
    "veggies" : "carrot",
    "lang" : "python",
    "veggies": "tomato"
}
print(type(x))
a = json.dumps(x, indent= 4, sort_keys= True )
print(a)
print(type(a))

with open("data.json", "w") as f:
    json.dump(x,f, indent=4)


#parsing json file
with open("data.json") as f:
    data = json.load(f)
print(data)

#parsing a json string

jsonstring = '{"fruit" : "apple","veggies" : "carrot","lang" : "python"}'

data = json.loads(jsonstring)
print(data)
print(data["fruit"])