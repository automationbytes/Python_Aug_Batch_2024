
class Employee:
    def __init__(self,name, salary):
        #public
        self.name = name
        self.__salary = salary #private

    def toPrint(self):
        print("Name: ",self.name, "Salary: ",self.__salary)

emp = Employee("Tom","12000")
emp.toPrint()
print(emp.name)
print(emp.__salary)

