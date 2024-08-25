
class Employee:
    def __init__(self,name, salary):
        #public
        self.name = name
        self._salary = salary #protected

    def toPrint(self):
        print("Name: ",self.name, "Salary: ",self._salary)

emp = Employee("Tom","12000")
emp.toPrint()
print(emp.name)
print(emp._salary)

