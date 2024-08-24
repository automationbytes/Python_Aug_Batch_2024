'''
Functions (Methods) - Block of code which will be executed only when its called
Parameterizing
Returning the values
Reusability

def funcName (any parameters):
    return

def - defn its a keyword used for declaring function
'''

def myFunc():
    print("Hello World")

myFunc() #Function name and parenthesis

def myFuncName(uname):
    print("Hello "+uname)

myFuncName("Tom")
myFuncName("Mahi")

def myFuncName(uname):
    return "Hello "+uname
x = myFuncName("Mahath!")
print(x, "Are u doing good?")

def sum(a,b):
    return a+b

print(sum(a= 5,b = 10))

print(sum(5,10))

def num(*any):
    print(any[2])

num(1,2,3,4)

def username(**name):
    print("First Name "+name["fname"])
    print("Last Name "+name["lname"])

username(fname="Tom",lname="Jerry",mname="Cartoon")

def mycountry(country = "India"):
    print(country)

mycountry("USA")
mycountry("UK")
mycountry()

def mylist(any):
    for x in any:
        print(x)

fruits = ["Apple","Banana","Grapes"]
mylist(fruits)

def printFruits (fname):
    print(fname)

for f in fruits:
    printFruits(f)