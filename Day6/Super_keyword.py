'''
super() returns a temp object of a parent class that allows to call a parent class methods inside the child class

'''

class College:
    name = "Tom"
    def College_Name(self):
        return "Devlabs"

class Student(College):


    def info(self):
        c_name = super().College_Name()

        print(super().name,"studing in",c_name)

s = Student()
s.info()