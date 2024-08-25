from abc import ABC

class car(ABC):
    def horn(self):
        pass


class BMW(car):
    def horn(self):
        print("BMW method")


class Tesla(car):
    def horn(self):
        print("Tesla method")

B = BMW()
B.horn()

'''

parent
    marriage - abc (6 months)
    gift - house

child
    marriage -xyz (

'''