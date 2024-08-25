class Employee:
    company = "Devlabs"

    def __init__(self,name, salary):
        self.name = name
        self.salary = salary


    @classmethod
    def get_companyName(cls):
        return  cls.company

    @classmethod
    def set_companyName(cls,Company):
        cls.company = Company


print(Employee.get_companyName())
Employee.set_companyName("ABC")
print(Employee.get_companyName())