'''
List is very similar to arrays in other lang
In simple words- multiple values in a single variable
It is mutable (modifiable)
List alloes duplicates (values)
Hetrogeneous - Both similar and different datatypes
Element will be stored on index based. And also accessed via index
[] - store a list

'''

fruits = ["Apple","Mango","Banana","Grapes","Mango"]
print(fruits)

#length of list
print(len(fruits))

#indexing - starts with 0
#Apple - 0 Mango - 1 Banana -2 Grapes -3 Mango -4
print(fruits[1])

#negative indexing
#Apple-5 Mango-4 Banana-3 Grapes-2 Mango -1
print(fruits[-2])

#slicing - cutting down the list into small list
print(fruits[1:4]) #starts wit 1 and end in 3

#starts from 2 and print till the end
print(fruits[2:])

#starts from 0 and go till the index value
print(fruits[:3])

#negative slicing
#Apple-5 Mango-4 Banana-3 Grapes-2 Mango -1
print(fruits[-5:-2])

print(fruits[:-1])

print(fruits[-3:])

print(fruits[:])
#reversing a list
print(fruits[::-1])
#Apple - 0 Mango - 1 Banana -2 Grapes -3 Mango -4
print(fruits[1:4:2])