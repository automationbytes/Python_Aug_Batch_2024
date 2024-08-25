'''

OOPS - Object Oriented Programming Structure

attributes
    age
    name
    email
behavior
    learning()
    reading()

A class is a blueprint of the object. To create a object we require a model/blueprint

Object is an instance of a class. Object is an entity that has a state and behavior

'''

class Student:
    name = "Tom"
    age = 10

    def readMethod(self):
        name = "Mahi"
        print("This is the read method of Student " + self.name)
        print("This is the read method of Student " + name)


s = Student() #default construtor
s.readMethod()
s1 =Student()
s1.readMethod()