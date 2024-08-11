num = 123
sum = 0

while num > 0:
    digit = num % 10 #3 #2 #1
    sum = sum+digit #3 #3+2=5 #5+1 = 6
    num = num//10 #12#1#0
print(sum)

num = 5
fact = 1
i = 1
while i<=num:
    fact = fact*i
    i = i+1
print(fact)