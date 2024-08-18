num = {1,4,5,6,7}
frset = frozenset(num)
print(frset)
print(type(frset))

num1 =  {1,6,9}

print(frset.union(num1))
print(frset)

print(frset.intersection(num1))

print(frset.symmetric_difference(num1))

print(frset.difference(num1))

print(frset.issubset(num1))

print(num1.issuperset(frset))