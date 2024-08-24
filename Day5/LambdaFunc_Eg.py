'''
A lambda function is a small anonymous function
It can take any number of arg, but can have only one exp

'''

sum = lambda a,b: a+b
print(sum(a=10,b=5))

def myfunc(n):
    return lambda a : n*n

print(myfunc(5)(None))