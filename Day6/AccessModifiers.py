"""

Public Member - Available for everyone. Accessible anywhere from outside
Private Member - Accessible within the class
Protected Member - Accessible with the class and Subclass


"""

class Employee:
    def __init__(self,name, salary):
        #public
        self.name = name
        self.salary = salary

    def toPrint(self):
        print("Name: ",self.name, "Salary: ",self.salary)

emp = Employee("Tom","12000")
emp.toPrint()
print(emp.name)
print(emp.salary)
