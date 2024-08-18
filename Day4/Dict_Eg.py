'''
Dict - used to store in Key and Value pair
Will not allow duplicate Keys
3.7 - dict are ordered
Mutable (changable)
{}

'''

mydict = {
    "fruit" : "apple",
    "veggies" : "carrot",
    "lang" : "python",
    "veggies": "tomato",
    "colors" : {"Red","Green","Blue"}
}

print(mydict)

#type
print(type(mydict))

#len
print(len(mydict))

#accessing the dict
print(mydict.get("fruit"))

print(mydict["colors"])

#print
print(type(mydict.keys()))

#print values
print(mydict.values())

#items
print(mydict.items())

#for loop for iterating Keys
for k in mydict.keys():
    print(k, mydict[k])

#for loop iterating values
for v in mydict.values():
    print(v)

#iterating both using items
for k,v in mydict.items():
    print(k,v)


#for loop - will just iterate the keys
for v in mydict:
    print(v)
