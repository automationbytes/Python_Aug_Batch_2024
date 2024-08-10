'''
Operators - used to perform some operations either on variables/datatypes
Arthimetic Operator - used to perform basic mathematical operations


'''

a = 10
b = 6
print(a+b)
#+ -> operator
#a,b - operand
print(a-b)
print(a*b) #mu;
print(a/b) #div
print(a**b) #exp
print(a%b) #remainder
print(int(a/b)) #normal
print(a//b) #quotient

'''
comparison Operator - comaparing two values/variables- gives true/false
== !=
'''

print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
print(a < b)
print(a > b)

'''
Assignment operator - to assign values to variables
'''
#a = a+10
a += 10
print(a)


a = 5
b = 3
c = 10


print(a>b and a>c)
print(a>b or a>c)

print(not(a == b))
'''
true and true - true
true and false - false
false and true - false
false and false - false

true or true = true
true or false = true
false or true = true
false or false = false
'''


'''
Identity Operator - is

'''
fruits = ["apple","banana"]
newfruits = ["apple","banana"]
print(fruits is newfruits)
f = fruits
print(f is fruits)
print(fruits is f)

print(f is not fruits)

"""
Membership operator - in

"""
print("apple" in fruits)
print("Mango" in fruits)

print("Mango" not in fruits)
