class Myclass:

    class_var = "Class Variable"

    def __init__(self,instance_var):
        self.instance_var = instance_var

    @classmethod
    def classMethd(cls,instance_var):
        print(cls.class_var)

    @staticmethod
    def staticMethd():
        print("static method")

# Myclass.classMethd()
# Myclass.staticMethd()

class MySubClass(Myclass):

    @classmethod
    def classMethd(cls):
        print("Over Ridden method")

    @staticmethod
    def staticMethd():
        print("overridden method")


MySubClass.classMethd()
MySubClass.staticMethd()

#Myclass.staticMethd(Myclass.class_var)
Myclass.classMethd(Myclass.class_var)
