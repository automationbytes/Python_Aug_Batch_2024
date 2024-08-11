# fruits = ["apple","banana","grapes","berry","cherry"]
# for q in fruits:
#     print(q)
#
# str = "Hello World"
# for i in str:
#     print(i)

#print 5 table

#print number from 1-100
#if divisible by 3 print hello
#if divisible by 5 print world
#if divisible by 5 and 3 print hello world


for i in range(1,101,1):
    if i % 3 == 0 and i % 5 == 0:
        print("Hello World", i)
    elif i % 3 == 0:
        print("Hello", i)
    elif i % 5 == 0:
        print("World", i)

    else:
        print(i)

#nested for loop
for i in range(1,5,1):
    print("outer", i)
    for j in range(1,3,1):
        print("inner",j)


fruits = ["apple","banana","grapes","berry","cherry"]
veg = ["tomato","onion"]
for q in fruits:
    print(q)
    for v in veg:
        print(v)