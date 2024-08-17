'''
Tuple - Ordered
and Unchangeable (Unmutable)
Duplicated are allowed
() - without brackets


'''

veggies = ("Apple","Carrot","EggPlant","Drumstick","Beetroot")
print(veggies)

print(type(veggies))


veggies = "Apple","Carrot","EggPlant","Drumstick","Beetroot"
print(veggies)
print(type(veggies))

# fruits = ["Apple","Mango","Banana","Grapes","Mango"]
# print(fruits)
# print(fruits[1:4])
# print(fruits)
print(veggies[1])
print(veggies[-1])

print(veggies[1:3])
print(veggies[-4:-1])

#updating the tuple
#veggies[1] = "Pumpkin"
#print(veggies)

newlist = list(veggies)
newlist[1] = "Pumpkin"
veggies = tuple(newlist)
print(veggies)

#add item
#remove item
#
# del veggies
# print(veggies)

fruits = ("apple","mango","banana") #packing
(red,green,yellow) = fruits #unpacking

print(yellow)
print(red)
print(type(yellow))


fruits = ("apple","mango","Guava","Pears","banana") #packing
(red,yellow,*green) =fruits

print(red)
print(green)
print(type(green))

print(green[0])
#print(yellow)
print(fruits)