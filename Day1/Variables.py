'''
Variables - Always starts with an alphabets or underscore
Shouldnt contains any special chars (#,$)
Variables shouldnt have any spaces in between
Variables are case sensitive
a = 10
A = 5

Datatypes - type of data which we are going to store in variable
number - int, float, complex
string - char, string
boolean - true/false


'''

a = 5
#a- variable
# 5 - value
# = ->operator
print(a)
A = 10
#type - type of variable
print(type(a))
'''
int - numbers without decimal point
float - numbers with decimal point
complex - numbers with real and imaginary part
'''

b = 53.5
print(type(b))
c = 5+6j
print(type(c))

st = "Hello"
s = '123'
print(type(st))
print(type(s))

#isinstance -> return true/false based on variable we provided
print(isinstance(s,str))
print(isinstance(s,int))

'''
list
set
tuple
dict 

binary datatypes - bytes, bytearray, memoryview (not needed)
None datatype - NoneType

'''

boole = True
boole1 = False
print(type(boole))
print(type(boole1))

b = b'Hello'
print(b)
print(type(b))

c = bytearray(10)
print(c)
print(type(c))

d = memoryview(bytes(3))
print(d)

x = None
print(x)
print(type(x))

'''
Type casting - converting from one datatype to another
int - float - str
'''

x = 10
y = float(x)
print(type(x))
print(type(y))

st = '100'
i = int(st)
print(i)
print(type(i))

st = 'a'
i = int(st)
print(i)
print(type(i))
print("Hello")
