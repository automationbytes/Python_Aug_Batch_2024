
fruits = ["Apple","Mango","Cherry","Grapes","Kiwi"]
newlist = []

for f in fruits:
    if "e" in f:
        newlist.append(f)

print(newlist)

#comprehension
fruits = ["Apple","Mango","Cherry","Grapes","Kiwi"]
newlist = [f for f in fruits if "e" in f]
print(newlist)

fruits = ["Apple","Kiwi","Mango","Cherry","Grapes","Kiwi","Banana","Kiwi"]
newlist = [f for f in fruits if f != "Kiwi"]
print(newlist)

newlist = [f.upper() for f in fruits]
print(newlist)