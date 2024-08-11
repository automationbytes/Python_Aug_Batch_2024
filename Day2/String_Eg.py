#String - datatype - anything wit single quotes/double quotes

a = "Hello"
b = 'hello'
print(type(a))
print(type(b))
c = '123'
print(type(c))

multiline = """Python is one of the powerful programming lang
Python can be used for web, api, desktop development
It supports multiple OS
"""
print(multiline)

fruit = "mangofruit"
print(len(fruit))

#indexing
#m -0 a -1 n-2 g-3 o -4
print(fruit[3])

#negative indexing
#m -5 a -4 n -3 g -2 o -1
print(fruit[-3])

#slicing
print(fruit[2:5]) #ngo #m-0 a-1 n-2 g-3 o-4 f-5 r-6 u-7 i-8 t-9
print(fruit[2:])# print till the last value
print(fruit[:5])#start index willbe 0
print(fruit[:])

#negative slicing
print(fruit[-9:-6])# m-10 a-9 n-8 g-7 o-6 f-5 r-4 u-3 i-2 t-1
print(fruit[-9:])
print(fruit[:-6])

print(fruit[2:9:2])#step 2 #m-0 a-1 n-2 g-3 o-4 f-5 r-6 u-7 i-8 t-9

#strip - used to trim down the white spaces
a = "   Hello     world    "
print(a.strip()) #trim white spaces on both sides
print(a.lstrip()) #trim white spaces in left side
print(a.rstrip()) #trim white spaces in right side

#lower
a = "Hello wORLD"
print(a.lower())

#upper
print(a.upper())

#cap
print(a.capitalize())

#title
print(a.title())

#swapcase
print(a.swapcase())

#casefold - to lower letter ->
a = "GRaß"
print(a.lower())
print(a.casefold())

#replace
b = "Python is one of the powerful programming lang. Python is used in AI"
print(b.replace("Python","Java"))
print(b.replace("ming lang","   "))

print(b.replace("o","0"))

#split
words = b.split(" ")
print(words)

#concat
a = "Hello"
b = "world"
c = 5
print(a+b)
print(a+format(c))
print(a+str(c))

b = "Python is one of the powerful programming lang. Python is used in AI"
print(b.startswith("Python"))
print(b.endswith("Python"))

#count
print(b.count("o"))

#find
print(b.find("h"))
print(b.find("lang"))
print(b[42])
#index
print(b.index("h"))

print(b.find("z")) #-1
#print(b.index("z")) #throw an error when the value is not available

num = "123"
print(num.isdigit())

a = "abc"
print(a.isalpha())

a = "GRaß"
print(a.isascii())

a = "python314"
print(a.isalnum())

#join
fruit = ["apple","banana","orange"]
print(fruit)
x = ",".join(fruit)
print(x)

#zfill
acctnum = "65446469"
print(acctnum.zfill(16))

b = "Python is one of the powerful programming lang. Python is used in AI"
#split
words = b.split(" ")
print(words)

x = "_".join(words)
print(x)