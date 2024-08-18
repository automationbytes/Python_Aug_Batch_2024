fruits = {"Apple","Banana","Grapes","Mango","Apple"}
print(fruits)

fruits.add("Orange")
print(fruits)

#update - extend new set (it can be list)
newfruits = {"Kiwi","Guava","Pears"}
fruits.update(newfruits)
print(fruits)

#remove - remove specified value
fruits.remove("Apple")
print(fruits)

#discard - remove the values - discard will not throw any error if we dont hav value
fruits.discard("Apple")
print(fruits)

# fruits.remove("Apple")
# print(fruits)

newfruits = fruits.copy()
print(newfruits , "new fruits")
print(fruits, "fruits")
#clear
newfruits.clear()
print(newfruits)

#del
# del (newfruits)
# print(newfruits)


fruits = {"Apple","Banana","Grapes","Mango","Apple"}
newfruits = {"Kiwi","Guava","Pears","Banana","Grapes"}


print(fruits.intersection(newfruits)) # it will not alter the fruits
print(fruits)

fruits.intersection_update(newfruits) #existing set will be altered
print(fruits)

fruits = {"Apple","Banana","Grapes","Mango","Apple"}
newfruits = {"Kiwi","Guava","Pears","Banana","Grapes"}
print(fruits.symmetric_difference(newfruits))
print(fruits)
print(newfruits)

#sym_update
newfruits.symmetric_difference_update(fruits)
print(fruits)
print(newfruits)

fruits = {"Apple","Banana","Grapes","Mango","Apple"}
newfruits = {"Kiwi","Guava","Pears","Banana","Grapes"}

print(fruits.union(newfruits))

fruits.update(newfruits)
print(fruits)


fruits = {"Apple","Banana","Grapes","Mango","Apple"}
newfruits = {"Kiwi","Guava","Pears","Banana","Grapes"}
print(fruits.difference(newfruits))

print(newfruits.difference(fruits))

fruits.difference_update(newfruits)
print(fruits)

#remove random value from set
fruits.pop()
print(fruits)
newfruits = {"Apple","Banana","Grapes","Mango","Apple"}
print(fruits.issubset(newfruits))
print(newfruits.issuperset(fruits))











