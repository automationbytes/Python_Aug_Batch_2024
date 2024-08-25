'''
Process of Inheriting the parent properties to child class
Parent class - Super class
Child class - sub class


Single Inheritance
Multilevel Inheritance
Hierarchial Inhertance
Multiple Inheritance
Hybrid Inheritance



'''

class animal:
    def eat(self):
        print("Animal Eat Method")

class dog():
    def bark(self):
        print("Dog bark method")

d = dog()
d.eat()
d.bark()