
fruits = ["Apple","Mango","Banana","Grapes","Mango"]
veggies = ["Onion","Potato","Tomato","Carrot","Beetroot"]

#Adding

#append - at the end of the list

fruits.append("Orange")
print(fruits)

fruits.append(veggies)
print(fruits)

print(fruits[6])
print(fruits[6][2])

#extend - add the values from the list to existing list
fruits = ["Apple","Mango","Banana","Grapes","Mango"]
veggies = ["Onion","Potato","Tomato","Carrot","Beetroot"]
fruits.extend(veggies)
print(fruits)

#insert - add item in a mentioned index
fruits = ["Apple","Mango","Banana","Grapes","Mango"]
fruits.insert(-2,"Orange")
print(fruits)

veggies = ["Onion","Potato","Tomato","Carrot","Beetroot"]
fruits.append(veggies)
fruits.insert(6,fruits)
print(fruits)

#remove - based on value
veggies = ["Onion","Carrot","Beetroot","Potato","Tomato","Carrot","Beetroot"]
veggies.remove("Carrot")
print(veggies)

# #del
# del (veggies)
# print(veggies)

#pop - remove based on index
veggies.pop(2)
print(veggies)

veggies.pop(-2)
print(veggies)

veggies.pop() #removes the last value
print(veggies)


#clear - list will be emptied
veggies.clear()
print(veggies)

#update
veggies = ["Onion","Carrot","Beetroot","Potato","Tomato","Carrot","Beetroot"]
veggies[1] = "Drumstick"
print(veggies)

veggies[:] = ["Ladies Finger","Brinjal"]
print(veggies)



veggies = ["Onion","Carrot","Beetroot","Potato","Tomato","Carrot","Beetroot"]
print(veggies.count("Carrot"))


veggies = ["Apple","Carrot","EggPlant","Drumstick","Beetroot"]
#sorting
veggies.sort()
print(veggies)

#des sorting
veggies.sort(reverse=True)
print(veggies)


