i =1
while i <= 10:
    print(i)
    #i +=1
    i = i+1

#reverse a number

num = 1234 #4321
rev = 0

while num > 0:
    remainder = num % 10 #1234%10 = 4; 123%10-3
    rev = rev * 10 + remainder #0+4-> 4; 40+3->43
    num = num//10
    print(rev)
print(rev)
print(type(rev), "rev")
num = 1234
numstr = str(num)

print(type(numstr), "numstr")

#find the sum of number -123 -> 6
#factorial - 5 -> 5*4*3*2*1



