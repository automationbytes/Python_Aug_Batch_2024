a = 10
b = 20

if a > b:
    print("A is greater than B")
else:
    print("B is greater than A")

#short-hand way
print("A is greater than B") if a > b else print("B is greater than A")

a = 5
if a == 5: print("A is 5")


a = 50
b = 10
c = 20

if a<b and a<c:
    print("A is lesser")
elif b<a and b<c:
    print("B is lesser")
else:
    print("C is lesser")


print("A is lesser") if  a<b and a<c else print("B is lesser") if b<a and b<c else print("C is lesser")

'''
number odd/even
positive/negative/zero
voting

marklist - m1,m2,m3
sum and average
avg greater than 80 - Grade A
60-79 - Grade B
40-59- Grade C
else - Fail


'''