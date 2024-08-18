#add
mydict = {
    "fruit" : "apple",
    "veggies" : "carrot",
    "lang" : "python",
    "veggies": "tomato",
    "colors" : {"Red","Green","Blue"}
}

mydict["csk"] = "Yellow"
print(mydict)

#update
mydict.update({"csk":"dhoni"})
print(mydict)

#setdefault
mydict.setdefault("csk","chennai super kings")
print(mydict)
mydict.setdefault("ipl","chennai super kings")
print(mydict)

#pop
mydict.pop("csk")
print(mydict)

#popitem -remove the last value
mydict.popitem()
print(mydict)

#del mydict
# print(mydict)

del mydict["lang"]
print(mydict)

# mydict.clear()
# print(mydict)

#copy
newdic = mydict.copy()
print(newdic)

newdic1 = dict(mydict)
print(newdic1)


mydict = {
    "ipl" : {
        "csk" : "dhoni",
        "rcb" : "kohli",
        "mi" : "rohit"
    },
    "fruit": {
        "red": "apple",
        "yellow": "banana",
        "green": "grapes"
    }
}

print(mydict["ipl"]["mi"])

for k,v in mydict.items():
    print(k)

    for x,y in v.items():
        print(x, y)