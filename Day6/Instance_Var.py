'''

Instance variables are declared inside a method using self keyword
WHen we use contructor we will be using it
'''


class Student:

    def __init__(self, name, age):
        #instance variable
        self.name = name
        self.age = age

    def readMethod(self):
        name = "Mahi"
        print("This is the read method of Student " + self.name)





s = Student("Jerry",7)
s.readMethod()
print(s.name)
print(s.age)

s.name = "Jerry"
s.age = 19
print(s.name,s.age)
#using getAttr
print(getattr(s,"name"))
print(getattr(s,"age"))
