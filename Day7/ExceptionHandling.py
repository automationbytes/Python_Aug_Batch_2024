'''

Exception Handling

try - test a block of code for errors
except  - Handle the errors
else - it will be executed when there is no error
finally - irrespective of try/except finally will come into picture


'''
import traceback

#print(abc)
#abc = 123
try:
    print(abc)
except:
    print("Exception occured")
    traceback.print_exc()
else:
    print("ABC printed correctly")

print("Hello World")



try:
    print(10/0)
except NameError:
    print("Name error orrured")
except:
    print("Other exception")
    traceback.print_exc()

try:
    print("abc")
except:
    print("Exception occured")

else:
    print("Else executed")
finally:
    print("Finally called")


#raise keyword used to create user defined exception
#program to eligible on voting

age = 5
if age < 18:
    raise Exception("Sorry, Not Eligible")

print("Hello")