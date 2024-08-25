'''

Constructor is a spl method used to initialize the object of the class.
When the object is created, constructor is automatically called
'''


class Student:

    def __init__(self, name, age):
        print("Constructor is Init")
        self.name = name
        self.age = age
        print("Object is init")

    def readMethod(self):
        name = "Mahi"
        print("This is the read method of Student " + self.name)
   #     print("This is the read method of Student " + name)

    def __del__(self):
        print("Destructor called")
        print("Object destroyed")


s = Student("Jerry",7)
s.readMethod()
s1 = s
del s
s1.readMethod()

s2 = Student("Virat",18)
s2.readMethod()